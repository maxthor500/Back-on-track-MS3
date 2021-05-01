import os
from datetime import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from forms import RegisterForm, LoginForm, CreatePostForm, CreateCommentForm
import bcrypt
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route('/home')
def index():
    """Render index template and when the user is logged every post is shown"""
    #get posts
    posts = get_posts()
    #if logged get profile's image - to prevent key error
    if session.get('logged_in'):
        if session['logged_in'] is True:
            image = mongo.db.users.find_one({"username": session["username"]})['image_profile']
            return render_template('index.html', title='Home', 
                                    image=image, posts=posts)    
    #if not logged return template without user image 
    return render_template('index.html', title='Home', posts=posts)


@app.route("/get_posts")
def get_posts():
    """Return every posts with reserve order"""
    posts = mongo.db.posts.find().sort("post_date", -1)
    return posts


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
        db_user = users.find_one({'username': request.form['username']})
        
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
                    'image_profile': '/static/images/anonymity.png',
                    'linkedin_url': '',
                    'website_url': '',
                    'share_profile': 'off'
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


@app.route('/about')
def about():
    """Render About template to use LeafletJS"""
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    """Render Contact template to use EmailJS"""
    return render_template('contact.html', title='Contact')


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


@app.route('/get_date')
def get_date():
    """get now date with a specific format"""
    now = datetime.now()
    format = "%Y %b %d %I:%M %p"
    post_date = now.strftime(format)
    return post_date


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Render User profile if in session"""
    # grab the session user from db
    username = mongo.db.users.find_one({"username": session["username"]})['username']
    image = mongo.db.users.find_one({"username": session["username"]})['image_profile']
    if session["username"]:
        return render_template("profile.html", username=username, image=image)
    return redirect(url_for("login"))


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
        return redirect(url_for('index', title='Post Edited'))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('edit_post.html', post=post_db, form=form, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    """Allows logged in user to delete one of their posts"""
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")
    return redirect(url_for("index"))


@app.route("/add_comment/<post_id>", methods=['GET', 'POST'])
def add_comment(post_id):
    post_db = mongo.db.posts.find_one_or_404({'_id': ObjectId(post_id)})
    form = CreateCommentForm(request.form)
    comment_date = get_date()
    if request.method == "POST":
        comment = {
            'post_id': post_db,
            'created_by': session['username'],
            'comment_description': request.form["post_description"],
            'comment_date': comment_date
        }
        if form.validate_on_submit():
            # set the collection
            comments_db = mongo.db.comments
            # insert the new post
            comments_db.insert_one(comment)
            flash("Comment Successfully Added")
            return redirect(url_for('index', title='New Comment Added' , comment=comments_db))
        else:
            flash("Something wrong! Comment not Added")
    return render_template('add_comment.html', title='Comment', post=post_db, form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
