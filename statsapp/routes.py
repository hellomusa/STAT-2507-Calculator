from flask import render_template, url_for, flash, redirect, request
from statsapp import app, db
from statsapp.forms import DataForm, ArgForm
from statsapp.models import Data
from statsapp.funcs import *

choices = { 'Go Home': 'home',
			'Mean' : 'mean',
			'Median': 'median',
			'Mode': 'mode',
			'Sample Variance': 'samplevariance',
			'Population Variance': 'populationvariance',
			'Sample Standard Deviation': 'samplesd',
			'Population Standard Deviation': 'populationsd',
			'Z-Score' : 'zscore',
			'Percentile' : 'percentile',
			'Interquartile Range' : 'iqr',
			'Five Number Summary' : 'fivenumsumm'
}

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', choices=choices)


@app.route('/about')
def about():
    return render_template('index.html', title='about')


@app.route('/mean', methods=['GET', 'POST'])
def mean():
	form = DataForm()

	if form.validate_on_submit():
		data = [float(i) for i in form.body.data.split(',')]
		result = round(get_mean(data), 2)
		return render_template('mean.html', choices=choices, title='mean', form=form, operation='Mean', result=result)

	return render_template('mean.html', choices=choices, title='mean', form=form, operation='Mean')


@app.route('/median', methods=['GET', 'POST'])
def median():
	form = DataForm()

	if form.validate_on_submit():
		result = get_median([float(i) for i in form.body.data.split(',')])[1]
		return render_template('median.html', choices=choices, title='median', form=form, operation='Median', result=result)
	return render_template('median.html', choices=choices, title='median', form=form, operation='Median')


@app.route('/mode', methods=['GET', 'POST'])
def mode():
	form = DataForm()

	if form.validate_on_submit():
		try:
			result = get_mode([float(i) for i in form.body.data.split(',')])
			return render_template('mode.html', choices=choices, title='mode', form=form, operation='Mode', result=result)

		except statistics.StatisticsError:
			return render_template('mode.html', choices=choices, title='mode', form=form, operation='Mode', result='No unique mode')

	return render_template('mode.html', choices=choices,  title='mode', form=form, operation='Mode')


@app.route('/samplevariance', methods=['GET', 'POST'])
def samvar():
	form = DataForm()

	if form.validate_on_submit():
		result = get_sam_variance([float(i) for i in form.body.data.split(',')])
		return render_template('samvar.html', choices=choices, title='sample variance', form=form, operation='Sample Variance', result=result)

	return render_template('samvar.html', choices=choices, title='sample variance', form=form, operation='Sample Variance')


@app.route('/populationvariance', methods=['GET', 'POST'])
def popvar():
	form = DataForm()

	if form.validate_on_submit():
		result = get_pop_variance([float(i) for i in form.body.data.split(',')])
		return render_template('popvar.html', choices=choices, title='population variance', form=form, operation='Population Variance', result=result)

	return render_template('popvar.html', choices=choices, title='population variance', form=form, operation='Population Variance')


@app.route('/samplesd', methods=['GET', 'POST'])
def samsd():
	form = DataForm()

	if form.validate_on_submit():
		result = get_sam_sd([float(i) for i in form.body.data.split(',')])
		return render_template('samsd.html', choices=choices, title='sample standard deviation', form=form, operation='Sample Standard Deviation', result=result)

	return render_template('samsd.html', choices=choices, title='sample standard deviation', form=form, operation='Sample Standard Deviation')


@app.route('/populationsd', methods=['GET', 'POST'])
def popsd():
	form = DataForm()

	if form.validate_on_submit():
		result = get_pop_sd([float(i) for i in form.body.data.split(',')])
		return render_template('popsd.html', choices=choices, title='population standard deviation', form=form, operation='Population Standard Deviation', result=result)

	return render_template('popsd.html', choices=choices, title='population standard deviation', form=form, operation='Population Standard Deviation')


@app.route('/zscore', methods=['GET', 'POST'])
def zscore():
	form = ArgForm()

	if form.validate_on_submit():
		result = get_zscore([float(i) for i in form.body.data.split(',')], float(form.arg.data))
		return render_template('zscore.html', choices=choices, title='zscore', form=form, operation='Z-Score', result=result)

	return render_template('zscore.html', choices=choices, title='zscore', form=form,operation='Z-Score')


@app.route('/percentile', methods=['GET', 'POST'])
def percentile():
	form = ArgForm()

	if form.validate_on_submit():
		result = get_percentile([float(i) for i in form.body.data.split(',')], float(form.arg.data))
		percentile = int(form.arg.data)
		return render_template('percentile.html', choices=choices, title='percentile', form=form, percentile=percentile, operation='Percentile', result=result)

	return render_template('percentile.html', choices=choices, title='percentile', percentile='p', form=form, operation='Percentile')


@app.route('/iqr', methods=['GET', 'POST'])
def iqr():
	form = DataForm()

	if form.validate_on_submit():
		result = get_iqr([float(i) for i in form.body.data.split(',')])
		return render_template('iqr.html', choices=choices, title='Interquartile Range', form=form, operation='Interquartile Range', result=result)

	return render_template('iqr.html', choices=choices, title='Interquartile Range', form=form, operation='Interquartile Range')


@app.route('/fivenumsumm', methods=['GET', 'POST'])
def fivenumsumm():
	form = DataForm()

	if form.validate_on_submit():
		result = get_five_num_summary([float(i) for i in form.body.data.split(',')])
		return render_template('fivenum.html', choices=choices, title='five num summary', form=form, operation='Five Number Summary', result=result)

	return render_template('fivenum.html', choices=choices, title='five num summary', form=form, operation='Five Number Summary')

