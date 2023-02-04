import os
from datetime import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from forms import (
    RegisterForm, LoginForm, CreatePostForm,
    CreateCommentForm, UpdateProfileForm,
    ConfirmDeleteAccount)
import bcrypt
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# index section
@app.route("/")
@app.route('/home')
def index():
    """Render index template and when the user is logged every post is shown"""
    # get posts
    posts = get_posts()
    return render_template('index.html', title='Home', posts=posts)


@app.route("/get_posts")
def get_posts():
    """Return every posts with reserve order"""
    posts = mongo.db.posts.find().sort("post_date", -1)
    return posts


# login user section
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login handler"""
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index', title='Home'))

    form = LoginForm()

    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # try and get one with same name as entered
        db_user = users.find_one(
                    {'username': request.form['username'].lower()})
        if db_user:
            # check password using hashing
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                             db_user['password']) == db_user['password']:
                session['username'] = request.form['username'].lower()
                session['logged_in'] = True
                # successful redirect to home logged in
                return redirect(url_for('index', title="Sign In", form=form))
            # must have failed set flash message
            flash('Invalid email/password combination')
    return render_template("login.html", title="Login", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles registration functionality"""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # get all the users
        users = mongo.db.users
        # see if we already have the entered username
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            # hash the entered password
            hash_pass = bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                      bcrypt.gensalt())
            # user object
            user = {
                    'email': request.form['email'],
                    'password': hash_pass,
                    'username': request.form['username'],
                    'linkedin_url': '',
                    'website_url': ''
                    }
            # insert the user to DB
            users.insert_one(user)
            session['username'] = request.form['username'].lower()
            return redirect(url_for('index'))
        # duplicate username set flash message and reload page
        flash('Sorry, that username is already registered - try to login')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    """Clears session and redirects to home"""
    session.clear()
    return redirect(url_for('index'))


@app.route('/get_date')
def get_date():
    """get now date with a specific format"""
    now = datetime.now()
    format = "%Y %b %d %I:%M %p"
    post_date = now.strftime(format)
    return post_date


# about
@app.route('/about')
def about():
    """Render About template to use LeafletJS"""
    return render_template('about.html', title='About')


# contact
@app.route('/contact')
def contact():
    """Render Contact template to use EmailJS"""
    return render_template('contact.html', title='Contact')


# profile section
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Render User profile if in session"""
    user = get_user(username)
    posts = get_posts()
    # grab the session user from db
    username = mongo.db.users.find_one(
                {"username": session["username"]})['username']
    if session["username"]:
        return render_template("profile.html", title="My Profile",
                               username=username, user=user, posts=posts)
    return redirect(url_for("login", title="Home"))


@app.route('/update_profile/<username>', methods=['GET', 'POST'])
def update_profile(username):
    """Allows logged in user to update their own profile"""
    user = get_user(username)
    posts = get_posts()
    user_id = mongo.db.users.find_one({"username": session["username"]})['_id']
    username = mongo.db.users.find_one(
        {"username": session["username"]})['username']
    # get user
    if request.method == 'GET':
        form = UpdateProfileForm(data=user)
        return render_template('update_profile.html', title="Update Profile",
                               user=user, username=username, form=form)
    form = UpdateProfileForm(request.form)
    if form.validate_on_submit():
        users_db = mongo.db.users
        users_db.update_one({
            '_id': ObjectId(user_id),
        }, {
            '$set': {
                'email': request.form["email"],
                'linkedin_url': request.form["linkedin_url"],
                'website_url': request.form["website_url"]
            }
        })
        flash("Profile Successfully Updated")
        return redirect(url_for('profile', title="Profile Updated",
                                user=user, posts=posts,
                                username=username, form=form))
    return render_template('update_profile.html', title="Update Profile",
                           user=user, username=username, form=form)


@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    '''
    DELETE.
    Remove user's account from the database as well as all
    posts and comments created by this user.
    Before deletion of the account, user is asked
    to confirm it by entering password.
    '''
    delete_form = ConfirmDeleteAccount(request.form)
    # get all users
    users = mongo.db.users
    # try and get one with same name as entered
    db_user = users.find_one({'username': username})
    if delete_form.validate_on_submit():
        if db_user:
            # check password using hashing
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                             db_user['password']) == db_user['password']:
                db_post = mongo.db.posts.find({'created_by': username})
                db_comment = mongo.db.comments.find({'created_by': username})
                for post in list(db_post):
                    post_id = post["_id"]
                    for comment in list(db_comment):
                        comment_id = comment["post_id"]
                        if comment_id == ObjectId(post_id):
                            mongo.db.comments.delete_one(
                                {"post_id": comment_id})
                        mongo.db.comments.delete_many({"created_by": username})
                        mongo.db.posts.delete_one({"_id": ObjectId(post_id)})
                mongo.db.users.delete_one({"_id": ObjectId(db_user["_id"])})
                logout()
                flash("Account Successfully Deleted")
                # successful redirect to home logged in
                return redirect(url_for('index', title="Home"))
            else:
                # must have failed set flash message
                flash("Password is incorrect! Please try again")
    return render_template("delete_account.html",
                           username=username, form=delete_form)


@app.route('/get_user/<username>', methods=['GET', 'POST'])
def get_user(username):
    user_id = mongo.db.users.find_one_or_404(
                                {"username": session["username"]})['_id']
    user_db = mongo.db.users.find_one_or_404({'_id': ObjectId(user_id)})
    return user_db


# posts section
@app.route('/add_posts', methods=['GET', 'POST'])
def add_posts():
    """Creates a posts and enters into my collection"""
    form = CreatePostForm(request.form)
    post_date = get_date()
    if request.method == "POST":
        share_post = "on" if request.form.get("share_post") else "off"
        post = {
            'post_title': request.form["post_title"],
            'created_by': session['username'],
            'post_description': request.form["post_description"],
            'share_post': share_post,
            'category_name': request.form["category_name"],
            'post_date': post_date
        }
        if form.validate_on_submit():
            # set the collection
            posts_db = mongo.db.posts
            # insert the new post
            posts_db.insert_one(post)
            flash("Post Successfully Added")
            return redirect(url_for('index', title='New Post Added'))
        else:
            flash("Something wrong! Post not Added")
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('create_posts.html',
                           title='add a post', form=form,
                           categories=categories)


@app.route('/edit_post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    """Allows logged in user to edit their own posts"""
    post_db = mongo.db.posts.find_one_or_404({'_id': ObjectId(post_id)})
    post_date = get_date()
    # get post
    if request.method == 'GET':
        form = CreatePostForm(data=post_db)
        return render_template('edit_post.html', post=post_db, form=form)
    # update post
    form = CreatePostForm(request.form)
    if form.validate_on_submit():
        share_post = "on" if request.form.get("share_post") else "off"
        posts_db = mongo.db.posts
        posts_db.update_one({
            '_id': ObjectId(post_id),
        }, {
            '$set': {
                'post_title': request.form["post_title"],
                'created_by': session['username'],
                'post_description': request.form["post_description"],
                'share_post': share_post,
                'category_name': request.form["category_name"],
                'post_date': post_date
            }
        })
        flash("Post Successfully Edited")
        return redirect(url_for('index', title='Post Edited'))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('edit_post.html',
                           post=post_db, form=form, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    """Allows logged in user to delete one of their posts"""
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")
    return redirect(url_for("index"))


# comments section
@app.route("/add_comment/<post_id>", methods=['GET', 'POST'])
def add_comment(post_id):
    post_db = mongo.db.posts.find_one_or_404(
                            {'_id': ObjectId(post_id)})
    form = CreateCommentForm(request.form)
    comment_date = get_date()
    comments = get_comments()
    if request.method == "POST":
        comment = {
            'post_id': post_db['_id'],
            'created_by': session['username'],
            'comment_description': request.form["comment"],
            'comment_date': comment_date
        }
        if form.validate_on_submit():
            # set the collection
            comments_db = mongo.db.comments
            # insert the new post
            comments_db.insert_one(comment)
            flash("Comment Successfully Added")
            return redirect(url_for('index', title='New Comment Added',
                                    comment=comments_db))
        else:
            flash("Something wrong! Comment not Added")
    return render_template('add_comment.html', title='Comment',
                           post=post_db, form=form, comments=comments)


@app.route("/get_comments")
def get_comments():
    """Return every comments"""
    comments = mongo.db.comments.find().sort("post_date", 1)
    return comments


@app.route("/delete_comment/<post_id>")
def delete_comment(post_id):
    """Allows logged in user to delete one of their comments"""
    mongo.db.comments.remove({"_id": ObjectId(post_id)})
    flash("Comment Successfully Deleted")
    return redirect(url_for("index"))


# error handle
@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

