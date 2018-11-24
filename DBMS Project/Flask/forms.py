from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import database


def name_exists_register(form, field):
	if (field.data in database.select_users()):
		raise ValidationError('Email already exists.')

def name_exists_login(form, field):
	if (field.data not in database.select_users()):
		raise ValidationError("Email doesn't exist. Check email or register")

class RegistrationForm(FlaskForm):
	firstname = StringField('First Name *', validators=[DataRequired()])
	lastname = StringField('Last Name *', validators=[DataRequired()])
	email = StringField('Email *', validators=[DataRequired(), Email(), name_exists_register])
	password = PasswordField('Password *',validators=[DataRequired()])
	confirm_password = PasswordField('Confirm password *',validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email(), name_exists_login])
	password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Login')