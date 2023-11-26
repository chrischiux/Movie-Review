from app import db
from flask_login import UserMixin
from sqlalchemy import UniqueConstraint

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    user = db.relationship('Users', backref=db.backref('reviews', lazy='dynamic'))
    movie = db.relationship('Movies', backref=db.backref('reviews', lazy='dynamic'))

    __table_args__ = (UniqueConstraint('user_id', 'movie_id', name='_user_movie_uc'),)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    name = db.Column(db.String(64))
    collection = db.relationship('Movies', secondary='collection')

    def has_liked_movie(self, movie):
        return movie in self.collection


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.String(64))
    liked_users = db.relationship('Users', secondary='collection', overlaps='collection')


collection = db.Table('collection', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'))
)