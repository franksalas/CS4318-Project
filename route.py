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
	return render_template('users.html')


@app.route('/donors/')
def showDonors():
	#return 'main page'
	return render_template('donors.html')



@app.route('/products/')
def showProducts():
	#return 'main page'
	return render_template('products.html')



@app.route('/storage/')
def showStorage():
	#return 'main page'
	return render_template('storage.html')



if __name__ == '__main__':

	app.run(debug=True)