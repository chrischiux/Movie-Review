from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, DecimalField
from wtforms.validators import InputRequired, Length, NumberRange, Optional


class TransactionForm(FlaskForm):
    name = StringField('name',
                       validators=[InputRequired(
                           "Transaction name can't be empty."),
                                   Length(min=1, max=30)])
    amount = DecimalField('amount',
                          validators=[InputRequired(
                              "Please enter transaction amount."),
                                      NumberRange(min=0.01,
                                                  message="Transaction\
                                                      amount must be > 0.01")])
    id = HiddenField('id',
                     id='recordID',
                     default=-1,
                     validators=[Optional()])


class GoalForm(FlaskForm):
    name = StringField('name',
                       validators=[Optional(),
                                   Length(min=0, max=30)])
    amount = DecimalField('amount',
                          validators=[InputRequired(
                              "Goal amount can't be empty."),
                                      NumberRange(min=0.01,
                                                  message="Goal amount must\
                                                    be > 0.01")])
    id = HiddenField('id',
                     id='recordID',
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
