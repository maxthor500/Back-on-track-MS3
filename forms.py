from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    email = StringField('Email Address', validators=[Length(min=6, max=35),
                                                     Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('password2',
                                         message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')
