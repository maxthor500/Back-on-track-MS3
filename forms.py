from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
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
    message_error = """The password must contain at least 8 characters
                     long and contain at least one number,
                     un uppercase letter and one special character!"""
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Regexp(regex, message=message_error),
                                         EqualTo('password2',
                                         message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')
