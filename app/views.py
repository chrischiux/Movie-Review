import sqlite3
from flask import render_template, flash, redirect, url_for
from app import app, db
from sqlalchemy import func, exc
from .forms import *
from .models import *
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
import hashlib

@app.route('/')
@login_required
def index():

    return render_template('index.html', name=current_user.name)

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