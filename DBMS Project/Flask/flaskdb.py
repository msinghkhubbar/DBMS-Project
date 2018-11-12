from flask import Flask, render_template,url_for,flash,redirect,request
from forms import RegistrationForm, LoginForm
from database import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '0f2f57c293cf38d00e0d55b510360807'

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

	return render_template('netflix.html',data1 = data1, data2 = data2)	


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
		
	return render_template('hotstarname.html', Name1 = Name1, Name2 = Name2 )	

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
