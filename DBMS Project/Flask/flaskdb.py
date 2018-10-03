from flask import Flask, render_template,url_for,flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0f2f57c293cf38d00e0d55b510360807'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html') 

@app.route("/netflix")
def netflix():
	return render_template('netflix.html')

@app.route("/amazon")
def amazon():
	return render_template('amazon.html')

@app.route("/hotstar")
def hotstar():
	return render_template('hotstar.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
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