import sqlite3
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from sqlalchemy import desc
from .forms import *
from .models import *
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
import hashlib, json, sys

@app.route('/')
@login_required
def index():

    movie_list = Movies.query.order_by(desc(Movies.year)).all()

    return render_template('index.html', name=current_user.name, movies=movie_list)

@app.route('/movie/<int:id>', methods=['GET', 'POST'])
def moviePage(id):
    movie_details = Movies.query.filter_by(id=id).first()

    return render_template('movie.html', movie=movie_details)

@app.route('/manage-collection', methods=['POST'])
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
        except(ValueError):
            pass

    return json.dumps({'status': 'OK'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        user = Users.query.filter_by(email=loginForm.email.data).first()
        password_hash = hashlib.sha256(loginForm.password.data.encode()).hexdigest()
        if user != None and user.password == password_hash:
            flash('Logged in successfully.')
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash(password_hash)

    return render_template('login.html', form=loginForm)

