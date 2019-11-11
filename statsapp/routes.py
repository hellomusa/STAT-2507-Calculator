from flask import render_template, url_for, flash, redirect, request
from statsapp import app

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('layout.html', title='about')

@app.route('/mean')
def mean():
	return render_template('mean.html', title='mean')


@app.route('/median')
def median():
	return render_template('median.html', title='median')
