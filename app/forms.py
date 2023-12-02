from flask_wtf import FlaskForm
from wtforms import HiddenField, TextAreaField, EmailField, PasswordField, StringField
from wtforms.validators import InputRequired, Length, Optional


class ReviewForm(FlaskForm):
    content = TextAreaField('review',
                            validators=[InputRequired(
                                "review can't be empty."),
                                Length(min=1, max=500)])
    id = HiddenField('id',
                     id='movieID',
                     default=-1,
                     validators=[Optional()])


class LoginForm(FlaskForm):
    email = EmailField('email',
                       validators=[InputRequired(
                           "Please enter your email address."),
                           Length(min=1, max=64)])
    password = PasswordField('password',
                             validators=[InputRequired(
                                 "Please enter your password."),
                                 Length(min=1, max=64)])


class RegisterForm(FlaskForm):
    name = StringField('name',
                       validators=[InputRequired(
                           "Please enter your name."),
                           Length(min=1, max=64)])
    email = EmailField('email',
                       validators=[InputRequired(
                           "Please enter your email address."),
                           Length(min=1, max=64)])
    password = PasswordField('password',
                             validators=[InputRequired(
                                 "Please enter your password."),
                                 Length(min=1, max=64)])
