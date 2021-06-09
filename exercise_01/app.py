from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World from view function!.</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello %s welcome to Flask</h1>' % name

@app.route('/profile')
def profile():
	return '<h2>Welcome to profile</h2>'

if __name__ == '__main__':
	app.run(debug=True)
	
