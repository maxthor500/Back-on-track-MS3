from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import (
    StringField, SelectField, PasswordField, BooleanField,
    TextAreaField, SubmitField, DateTimeField)
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email Address', validators=[DataRequired(),
                                                     Length(min=6, max=35),
                                                     Email()])
    regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
    message_error = """Password must contain at least 8 characters
                     long and contain at least one number,
                     an uppercase letter and one special character!"""
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Regexp(regex, message=message_error),
                                         EqualTo('password2',
                                         message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')


class CreatePostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired()])
    category_name = SelectField("Category", validators=[DataRequired()], validate_choice=False)
    post_description = TextAreaField('Post Description',
                                     validators=[DataRequired()])
    share_post = BooleanField()
    submit = SubmitField('Add Post')


class CreateCommentForm(FlaskForm):
    comment = StringField('Write a comment',validators=[DataRequired()])
    submit = SubmitField('Add Comment')