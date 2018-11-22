from flask import Flask, render_template,url_for,flash,redirect,request
from forms import RegistrationForm, LoginForm
from database import *
# from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = '0f2f57c293cf38d00e0d55b510360807'


logged_user = ''
movie_result = None
show_result = None
movie_name = ''
idd = ''
# bcrypt=Bcrypt(app)

def take():
	Name = ''
	if(request.method == 'POST'):
		Name = request.form['name']
	return Name	
	


@app.route("/")
@app.route("/home")
def home():
	# search_intake_service()
	return render_template('index.html') 

#=====================================================================================================    


@app.route("/netflix")
def netflix():
	details = []
	data1 = ()
	data2 = ()
	if(request.method == 'POST'):
		Genre1 = request.form['genre']
		Director1 = request.form['director']
		Actor1 = request.form['actor']
		Year1 = request.form['year']

		Genre = str(Genre1)
		Director =str(Director1) 
		Actor = str(Actor1)
		Year = int(Year1)

			# details = search_intake_service()
		print('Movies\n')
		# data2 = select_shows_all_cri(details[0],details[1],details[2],details[3])
		data2 = select_movies_all_cri(Genre,Director,Actor,Year)
		print('Shows')
		# data1 = select_movies_all_cri(details[0],details[1],details[2],details[3])
		data1 = select_shows_all_cri(Genre,Director,Actor,Year)


# def take():
# 	Name = ''
# 	if(request.method == 'POST'):
# 		Name = request.form['name']
# 	return Name	
	


# 	return render_template('netflix.html',data1 = data1, data2 = data2)	


@app.route("/netflixname")
def netflix_name():
	Name1 = ''
	Name2 = ''
	if(request.method == 'POST'):
		Name = request.form['name']
		print('Movies\n')
		Name1 = select_movie_name(Name)
		print('Shows')
		Name2 = select_show_name(Name)
	
	return render_template('netflixname.html', Name1 = Name1, Name2 = Name2)	

#======================================================================================================	

@app.route("/amazon", methods = ['GET','POST'])
def amazon():
	details = []
	data1 = ()
	data2 = ()
	if(request.method == 'POST'):
		Genre1 = request.form['genre']
		Director1 = request.form['director']
		Actor1 = request.form['actor']
		Year1 = request.form['year']
		# Genre = str(Genre1)
		# Director =str(Director1) 
		# Actor = str(Actor1)
		# Year = int(Year1)
		# print(Genre1)
		# print(Director1)
		# print(Actor1)
		# print(Year1)

		data1 = select_movies_all_cri(Genre1,Director1,Actor1,Year1)
		data2 = select_shows_all_cri(Genre1,Director1,Actor1,Year1)
	return render_template('amazon.html',data1 = data1, data2 = data2)



@app.route("/amazonname", methods = ['GET','POST'])
def amazon_name():
	Name1 = ''
	Name2 = ''
	if(request.method == 'POST'):
		Name = request.form['name']
		Name1 = select_movie_name(Name)
		Name2 = select_show_name(Name)		
	return render_template('amazonname.html', Name1 = Name1, Name2 = Name2)	


#=======================================================================================================

@app.route("/hotstar")
def hotstar():
	global movie_result
	global show_result
	details = []
	data1 = ()
	data2 = ()
	if(request.method == 'POST'):
		Genre1 = request.form['genre']
		Director1 = request.form['director']
		Actor1 = request.form['actor']
		Year1 = request.form['year']

		# Genre = str(Genre1)
		# Director =str(Director1) 
		# Actor = str(Actor1)
		# Year = int(Year1)

		print(Genre1)
		print(Director1)
		print(Actor1)
		print(Year1)

		data1 = select_movies_all_cri(Genre1,Director1,Actor1,Year1)
		data2 = select_shows_all_cri(Genre1,Director1,Actor1,Year1)
		for i in data1:
			movie_result.append(i)
		for i in data2:
			show_result.append(i)
	return render_template('hotstar.html',data1 = data1, data2 = data2)


@app.route("/hotstarname", methods = ['GET','POST'])
def hotstar_name():
	Name1 = ''
	Name2 = ''
	if(request.method == 'POST'):
		Name = request.form['name']
		Name1 = select_movie_name(Name)
		Name2 = select_show_name(Name)		
	return render_template('hotstarname.html', Name1 = Name1, Name2 = Name2)	

# @app.route("/results", methods=['GET','POST'])
# def results():
# 	details = []
# 	data1 = ()
# 	data2 = ()
# 	if(request.method == 'POST'):
# 		Genre1 = request.form['genre']
# 		Director1 = request.form['director']
# 		Actor1 = request.form['actor']
# 		Year1 = request.form['year']

# 		Genre = str(Genre1)
# 		Director =str(Director1) 
# 		Actor = str(Actor1)
# 		Year = str(Year1)

# 		data1 = select_movies_all_cri(Genre,Director,Actor,Year)
# 		data2 = select_shows_all_cri(Genre,Director,Actor,Year)
# 	return render_template('results.html', data1=data1, data2=data2)
#=========================================================================================================	
@app.route("/feedback", methods = ['GET','POST'])
def feedback():
	 # global movie_name
	global idd
	global movie_name
	if(request.method == 'POST'):
		# movie_name = request.form['1']
		idd = request.form['1']
		movie_name = feedback_name(idd)
		# print(movie_name)
		# print(idd)
	return render_template('feedback.html', idd= idd, movie_name = movie_name[0])

@app.route("/feedbacksubmit", methods = ['GET','POST'])
def feedbacksubmit():
	# global movie_name
	global idd
	rating=0
	if(request.method == 'POST'):
		rating = request.form['rating']
		comment = request.form['comment']
		feedback_submit(uid,idd,rating,comment)
		# print(movie_name)
		print(rating)
		print(idd)
	return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		database.registration(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
		flash(f'Account created for {form.email.data}','success')
		return redirect(url_for('register'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	global logged_user
	passw = ''
	if form.validate_on_submit():
		entered_pass = form.password.data
		passw1 = check_login(form.email.data)
		passw = str(passw1[0])
		print(passw)
		if entered_pass == passw:
			flash('You have been logged in', 'success')
			logged_user = form.email.data
			print(logged_user)
			return redirect(url_for('home', data = logged_user))
		else:
			flash('Login unsuccesful. Please check email or password', 'danger')
			return render_template('login.html', title='Login', form=form)
	else:		
		return render_template('login.html', title='Login', form=form)



if __name__=='__main__':
	app.run(debug=True)
