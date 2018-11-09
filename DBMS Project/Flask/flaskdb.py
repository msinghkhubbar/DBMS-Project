from flask import Flask, render_template,url_for,flash,redirect,request
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
	details = (Genre,Director,Actor,Year)
	# details = (request.form['genre'],request.form['director'],request.form['actor'], request.form['year'])
	# return (request.form['genre'],request.form['director'],request.form['actor'], request.form['year'])
	return details
	

# def search_intake(service = 'null'):
# 	Actor = request.form['actor']
# 	Director = request.form['director']
# 	Genre = request.form['genre']
# 	Year = request.form['year']
	

def search_intake_name():
	Name = request_form['name']	
	return Name
#=====================================================================================================================================

@app.route("/")
@app.route("/home")
def home():
	# search_intake_service()
	return render_template('index.html') 

#=====================================================================================================    

@app.route("/netflix")
def netflix():
	details = ()
	if(request.method == 'POST'):
		details = search_intake_service()
	# print('Movies')
	select_shows_all_cri(details[0],details[1],details[2],details[3])
	# (request.form['genre'],request.form['director'],request.form['actor'], request.form['year'])
	# print('Shows')
	select_movies_all_cri(details[0],details[1],details[2],details[3])

	return render_template('netflix.html')


@app.route("/netflixname")
def netflix_name():
	Name = ''
	if(request.method == 'POST'):
		Name = search_intake_name()
	print('Movies\n')
	select_movie_name(Name)
	print('Shows')
	select_show_name(Name)
	
	return render_template('netflix.html')	

#======================================================================================================	

@app.route("/amazon")
def amazon():
	details = ()
	if(request.method == 'POST'):
		details = search_intake_service()
	print('Movies\n')
	select_shows_all_cri(details[0],details[1],details[2],details[3])
	print('Shows')
	select_movies_all_cri(details[0],details[1],details[2],details[3])

	return render_template('amazon.html')



@app.route("/amazonname")
def amazon_name():
	Name = ''
	if(request.method == 'POST'):
		Name = search_intake_name()
	print('Movies\n')
	select_movie_name(Name)
	print('Shows')
	select_show_name(Name)
	
	return render_template('amazon.html')	


#=======================================================================================================

@app.route("/hotstar")
def hotstar():
	details = ()
	if(request.method == 'POST'):
		details = search_intake_service()
	# print('Movies')
	data2 = select_shows_all_cri(details[0],details[1],details[2],details[3])
	# print('Shows')
	data1 = select_movies_all_cri(details[0],details[1],details[2],details[3])
	
	return render_template('hotstar.html',data1 = data1, data2 = data2)


@app.route("/hotstarname")
def hotstar_name():
	Name = ''
	if(request.method == 'POST'):
		Name = search_intake_name()
	print('Movies\n')
	select_movie_name(Name)
	print('Shows')
	select_show_name(Name)
	
	return render_template('hotstarname.html')	


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
