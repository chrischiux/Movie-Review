from app import db
from flask_login import UserMixin

movieRatings = db.Table('movieRatings', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('rating', db.Integer)
)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    name = db.Column(db.String(64))
    collection = db.relationship('Movies', secondary='collection')

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.String(64))
    # director = db.Column(db.String(64))
    # actors = db.Column(db.String(64))
    # plot = db.Column(db.String(64))
    poster = db.Column(db.String(64))
    liked_users = db.relationship('Users', secondary='collection', overlaps='collection')
    # imdbRating = db.Column(db.String(64))
    # imdbID = db.Column(db.String(64))
    # type = db.Column(db.String(64))

collection = db.Table('collection', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'))
)