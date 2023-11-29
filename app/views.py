import sqlite3
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from .forms import *
from .models import *
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
import hashlib
import json
import sys


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        user = Users.query.filter_by(email=loginForm.email.data).first()
        password_hash = hashlib.sha256(
            loginForm.password.data.encode()).hexdigest()
        if user != None and user.password == password_hash:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password.", 'danger')

    return render_template('login.html', form=loginForm, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()

    if registerForm.validate_on_submit():

        user = Users(name=registerForm.name.data, email=registerForm.email.data, password=hashlib.sha256(registerForm.password.data.encode()).hexdigest())
        try:
            db.session.add(user)
            db.session.commit()
            flash('User registered successfully.', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Email already registered, please use another email!', 'danger')

    return render_template('register.html', form=registerForm, title='Register')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')

    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():

    movie_list = Movies.query.order_by(desc(Movies.year)).all()

    return render_template('list_view.html', movies=movie_list, title='Home', route='home', user=current_user)


@app.route('/liked')
@login_required
def liked():

    movie_list = Users.query.filter_by(id=current_user.id).first().collection

    return render_template('list_view.html', name=current_user.name, movies=movie_list, title='My liked movies', table_caption='List of liked movies')


@app.route('/movie/<int:id>', methods=['GET', 'POST'])
@login_required
def moviePage(id):
    form = ReviewForm()

    movie_details = Movies.query.filter_by(id=id).first()
    movie_reviews = movie_details.reviews.all()

    if form.validate_on_submit():

        try:
            review = Reviews(content=form.content.data,
                             user_id=current_user.id, movie_id=id)
            db.session.add(review)
            db.session.commit()
            flash('Review added successfully.', 'success')
            return redirect(url_for('moviePage', id=id))
        except IntegrityError:
            db.session.rollback()
            flash('You have already reviewed this movie.', 'danger')

    return render_template('movie.html', movie=movie_details, form=form, reviews=movie_reviews, title=movie_details.title)


@app.route('/delete_review/<int:review_id>', methods=['GET', 'POST'])
@login_required
def deleteReview(review_id):
    review = Reviews.query.filter_by(id=review_id).first()
    movie_id = review.movie_id
    if review.user_id != current_user.id:
        flash('You cannot delete reviews that are not yours.', 'danger')
        return redirect(url_for('moviePage', id=movie_id))
    db.session.delete(review)
    db.session.commit()
    flash('Review deleted successfully.', 'success')

    return redirect(url_for('moviePage', id=movie_id))


@app.route('/manage-collection', methods=['POST'])
@login_required
def collection():
    data = json.loads(request.data)
    movie_id = int(data.get('movie_id'))
    movie = Movies.query.filter_by(id=movie_id).first()
    if data.get('action') == 'add':
        current_user.collection.append(movie)
        db.session.commit()
    else:
        try:
            current_user.collection.remove(movie)
            db.session.commit()
        except (ValueError):
            pass

    return json.dumps({'new_like_count': len(movie.liked_users)})
