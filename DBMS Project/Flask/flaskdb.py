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


@app.route("/home")
def home():
	# search_intake_service()
	return render_template('index.html', logged_user=logged_user) 

#=====================================================================================================    


@app.route("/netflix", methods = ['GET','POST'])
def netflix():
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

		data1 = select_movies_all_cri_netflix(Genre1,Director1,Actor1,Year1)
		data2 = select_shows_all_cri_netflix(Genre1,Director1,Actor1,Year1)
	return render_template('netflix.html',data1 = data1, data2 = data2, logged_user=logged_user)


# def take():
# 	Name = ''
# 	if(request.method == 'POST'):
# 		Name = request.form['name']
# 	return Name	
	


# 	return render_template('netflix.html',data1 = data1, data2 = data2)	


@app.route("/netflixname", methods=['GET','POST'])
def netflix_name():
	Name1 = ''
	Name2 = ''
	if(request.method == 'POST'):
		Name = request.form['name']
		print('Movies\n')
		Name1 = select_movie_name_netflix(Name)
		print('Shows')
		Name2 = select_show_name_netflix(Name)
	
	return render_template('netflixname.html', Name1 = Name1, Name2 = Name2, logged_user=logged_user)	

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

		data1 = select_movies_all_cri_amazon(Genre1,Director1,Actor1,Year1)
		data2 = select_shows_all_cri_amazon(Genre1,Director1,Actor1,Year1)
	return render_template('amazon.html',data1 = data1, data2 = data2, logged_user=logged_user)



@app.route("/amazonname", methods = ['GET','POST'])
def amazon_name():
	Name1 = ''
	Name2 = ''
	if(request.method == 'POST'):
		Name = request.form['name']
		Name1 = select_movie_name_amazon(Name)
		Name2 = select_show_name_amazon(Name)		
	return render_template('amazonname.html', Name1 = Name1, Name2 = Name2, logged_user=logged_user)	


#=======================================================================================================

@app.route("/hotstar" , methods = ['GET','POST'])
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

		data1 = select_movies_all_cri_hotstar(Genre1,Director1,Actor1,Year1)
		data2 = select_shows_all_cri_hotstar(Genre1,Director1,Actor1,Year1)
	return render_template('hotstar.html',data1 = data1, data2 = data2, logged_user=logged_user)


@app.route("/hotstarname", methods = ['GET','POST'])
def hotstar_name():
	Name1 = ''
	Name2 = ''
	if(request.method == 'POST'):
		Name = request.form['name']
		Name1 = select_movie_name_hotstar(Name)
		Name2 = select_show_name_hotstar(Name)		
	return render_template('hotstarname.html', Name1 = Name1, Name2 = Name2, _logged_user=logged_user)	

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
	return render_template('feedback.html', idd= idd, movie_name = movie_name[0], logged_user=logged_user)

@app.route("/feedbacksubmit", methods = ['GET','POST'])
def feedbacksubmit():
	# global movie_name
	global idd
	global logged_user
	rating=0
	if(request.method == 'POST'):
		rating = request.form['rating']
		comment = request.form['comment']
		feedback_submit(logged_user,idd,rating,comment)                 #flash error in case of an integrity error,error getting detected
		# print(movie_name)
		print(rating)
		print(idd)
	return render_template("index.html", logged_user = logged_user)

@app.route("/watchlist", methods = ['GET','POST'])
def watchlist():	
	global idd
	global logged_user
	data1=()
	data2=()
	data3=()
	if (request.method == 'POST'):
		idd = request.form['2']
		print(idd)
		watchlist_submit(logged_user,idd)           
		rec_submit(idd)                                         #error not detected,shouldnt display in case of an integrity error,just flash a message
		data1,data2 = watchlist_display(logged_user)
		print(data1)
		print(data2)
		data3 = select_rec()
	return render_template("watchlist.html", data1=data1, data2=data2, data3=data3, logged_user = logged_user)



@app.route("/recommend")
def recommend():	
	global idd
	global logged_user
	data3 = ()
	rec_submit(idd) 
	# data2=()
	 # if (request.method == 'POST'):
	# 	idd = request.form['2']
	# 	watchlist_submit(logged_user,idd)                 #error not detected,shouldnt display in case of an integrity error,just flash a message
	data3 = select_rec()

	# 	print(data1)
	# 	print(data2)
	return render_template("recommend.html", data3=data3, logged_user = logged_user)



@app.route("/watchlistDisplay")
def watchlistDisplay():	
	global idd
	global logged_user               #error not detected,shouldnt display in case of an integrity error,just flash a message
	data1,data2 = watchlist_display(logged_user)
	print(data1)
	print(data2)
	return render_template("watchlist.html", data1=data1, data2=data2,logged_user = logged_user)


@app.route("/")
@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		database.registration(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
		flash(f'Account created for {form.email.data}','success')
		return redirect(url_for('login'))
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
