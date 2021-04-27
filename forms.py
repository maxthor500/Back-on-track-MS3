from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import (
    StringField, SelectField, PasswordField, BooleanField,
    TextAreaField, SubmitField, DateTimeField)
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
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
    post_date = DateTimeField("Enter Date", default=datetime.utcnow,
                              format="%d/%m/%Y")
    share_post = BooleanField(default="on")
    submit = SubmitField('Add Post')
