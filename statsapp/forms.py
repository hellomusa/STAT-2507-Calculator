from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import wtforms

class DataForm(FlaskForm):
	body = StringField('<h5>Enter Data: (seperated by commas)</h5>', validators=[DataRequired()])

class ArgForm(FlaskForm):
	body = StringField('<h5>Enter Data: (seperated by commas)</h5>', validators=[DataRequired()])
	arg = StringField('<h5>Enter Argument: </h5>', validators=[DataRequired(), Length(max=1)])
	x = StringField('<h5>Enter Raw Score (x): </h5>', validators=[DataRequired(), Length(max=1)])
	mean = StringField('<h5>Enter Mean: </h5>', validators=[DataRequired(), Length(max=1)])
	sd = StringField('<h5>Enter Population Standard Deviation: </h5>', validators=[DataRequired(), Length(max=1)])
