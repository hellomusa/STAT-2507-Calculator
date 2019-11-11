from flask import render_template, url_for, flash, redirect, request
from statsapp import app, db
from statsapp.forms import DataForm
from statsapp.models import Data
from statsapp.funcs import *

choices = { 'Mean' : 'mean',
			'Median': 'median',
			'Mode': 'mode',
			'Sample Variance': 'samplevariance',
			'Population Variance': 'populationvariance',
			'Sample Standard Deviation': 'samplesd',
			'Population Standard Deviation': 'populationsd',
			'Z-Score' : 'zscore',
			'Percentile' : 'percentile',
			'Interquartile Range' : 'iqr',
			'Five Number Summary' : 'fivenumsumm',
			'Combination' : 'combination',
			'Permutation' : 'permutation'
}

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', choices=choices)


@app.route('/about')
def about():
    return render_template('layout.html', title='about')


@app.route('/mean', methods=['GET', 'POST'])
def mean():
	form = DataForm()

	# If valid data entered
	if form.validate_on_submit():
		data = [float(i) for i in form.body.data.split(',')]
		print(data)
		result = round(get_mean(data), 2)
		return render_template('mean.html', title='mean', form=form, operation='Mean', result=result)

	return render_template('mean.html', title='mean', form=form, operation='Mean')


@app.route('/median')
def median():
	return render_template('median.html', title='median')


@app.route('/mode')
def mode():
	return render_template('mode.html', title='mode')


@app.route('/samplevariance')
def samvar():
	return render_template('samvar.html', title='sample variance')


@app.route('/populationvariance')
def popvar():
	return render_template('popvar.html', title='population variance')


@app.route('/samplesd')
def samsd():
	return render_template('samsd.html', title='sample standard deviation')


@app.route('/populationsd')
def popsd():
	return render_template('popsd.html', title='population standard deviation')


@app.route('/zscore')
def zscore():
	return render_template('zscore.html', title='z-score')


@app.route('/percentile')
def percentile():
	return render_template('percentile.html', title='percentile')


@app.route('/iqr')
def iqr():
	return render_template('iqr.html', title='iqr')


@app.route('/fivenumsumm')
def fivenumsumm():
	return render_template('fivenum.html', title='five number summary')


@app.route('/combination')
def combination():
	return render_template('combination.html', title='combination')


@app.route('/permutation')
def permutation():
	return render_template('permutation.html', title='permutation')
