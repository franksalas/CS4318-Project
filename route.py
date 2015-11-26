from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Donors, Products, Storage
app = Flask(__name__)


engine = create_engine('sqlite:///newBlood.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def main():
	#return 'main page'
	return render_template('main.html')
	

@app.route('/users/')
def showUsers():
	#return 'main page'
	user = session.query(Users).all()
	return render_template('users.html',user=user)



@app.route('/user/<int:users_id>')
def historyUser(users_id):
	#return 'main page'
	return render_template('historyuser.html')



@app.route('/donors/')
def showDonors():
	#return 'main page'
	donor = session.query(Donors).all()
	return render_template('donors.html',donor=donor)



@app.route('/products/')
def showProducts():
	#return 'main page'
	product = session.query(Products).all()
	return render_template('products.html',product=product)



@app.route('/storage/')
def showStorage():
	#return 'main page'
	storage = session.query(Storage).all()
	return render_template('storage.html',storage=storage)



if __name__ == '__main__':

	app.run(debug=True)

# {% extends "base.html" %}
# {% block content %}
#  {% endblock %}
