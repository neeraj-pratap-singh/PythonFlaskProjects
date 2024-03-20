from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import User

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # Your signup logic here
    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Your login logic here
    return render_template('login.html')

@app.route("/")
def home():
    return render_template('home.html')
