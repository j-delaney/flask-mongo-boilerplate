from app import app, db
from flask import render_template

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/user/<name>')
def user_visit(name):
	user = db.User.find_one({'name': name})
	if not user:
		user = db.User()
		user.name = name
	user.visits += 1
	user.save()

	return render_template('user_visit.html', user=user)