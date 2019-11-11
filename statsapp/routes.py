from flask import render_template, url_for, flash, redirect, request
from statsapp import app

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html', title='about')

@app.route('/mean')
def mean():
