from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, DecimalField
from wtforms.validators import InputRequired, Length, NumberRange, Optional


class ReviewForm(FlaskForm):
    content = StringField('review',
                       validators=[InputRequired(
                           "review can't be empty."),
                                   Length(min=1, max=500)])
    id = HiddenField('id',
                     id='movieID',
                     default=-1,
                     validators=[Optional()])


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[InputRequired(
                            "Please enter your email address."),
                                    Length(min=1, max=64)])
    password = StringField('password',
                           validators=[InputRequired(
                               "Please enter your password."),
                                       Length(min=1, max=64)])