from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__,template_folder = "templates")

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login', methods = ['POST','GET'])
def login():
	if request.method == 'POST' and request.form['nm'] == 'admin':
		return redirect(url_for('success'))
	else:
		#return redirect(url_for('index'))
		abort(401)

@app.route('/success')
def success():
	return "Logged in successfully"

if __name__ == '__main__':
	app.run(debug = True)