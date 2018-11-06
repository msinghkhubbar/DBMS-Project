from flask import Flask, render_template,url_for,flash, redirect
from forms import RegistrationForm, LoginForm
from database import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '0f2f57c293cf38d00e0d55b510360807'

#===================================================================================================================================
#functions to take inputs

def search_intake_service():
	# print(service)
	Actor = request.form['actor']
	Director = request.form['director']
	Genre = request.form['genre']
	Year = request.form['year']
	

# def search_intake(service = 'null'):
# 	Actor = request.form['actor']
# 	Director = request.form['director']
# 	Genre = request.form['genre']
# 	Year = request.form['year']
	

def search_intake_name():
	Name = request_form['name']	

#=====================================================================================================================================

@app.route("/")
@app.route("/home")
def home():
	# search_intake_service()
    return render_template('index.html') 

#=====================================================================================================    

@app.route("/netflix")
def netflix():
    if(request.method == 'POST'):
		search_intake_service()
	print('Movies')
	select_shows_all_cri(Genre,Director,Actor,Year)
	print('Shows')
	select_movies_all_cri(Genre,Director,Actor,Year)

	return render_template('netflix.html')

#======================================================================================================	

@app.route("/amazon")
def amazon():
	if(request.method == 'POST'):
		search_intake_service()
	print('Movies')
	select_shows_all_cri(Genre,Director,Actor,Year)
	print('Shows')
	select_movies_all_cri(Genre,Director,Actor,Year)

	return render_template('amazon.html')

#=======================================================================================================

@app.route("/hotstar")
def hotstar():
	if(request.method == 'POST'):
		search_intake_service()
	print('Movies')
	select_shows_all_cri(Genre,Director,Actor,Year)
	print('Shows')
	select_movies_all_cri(Genre,Director,Actor,Year)

	return render_template('hotstar.html')

#=========================================================================================================	

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccesful. Please check email or password', 'danger')
	return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
	app.run(debug=True)
