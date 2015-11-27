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
	return render_template('main.html')


@app.route('/users/')
def showUsers():
	user = session.query(Users).all()
	return render_template('users.html', user=user)


@app.route('/user/<int:users_id>/')
def historyUser(users_id):
	currentuser = session.query(Users).filter_by(id=users_id).one()
	donors = session.query(Donors).filter_by(users_id=users_id)
	return render_template('currentuser.html',currentuser=currentuser, donors=donors)


@app.route('/donors/')
def showDonors():
	donor = session.query(Donors).all()
	return render_template('donors.html',donor=donor)


@app.route('/donors/new/<int:users_id>/', methods=['GET','POST'])
def newDonors(users_id):
	if request.method == 'POST':
		newdonor = Donors(
			first_name=request.form['name'],
			last_name=request.form['last'],
			address=request.form['address'],
			dob=request.form['dob'],
			users_id=users_id)
		session.add(newdonor)
		session.commit()
		return redirect(url_for('historyUser', users_id=users_id))
	else:
		return render_template('newdonor.html', users_id=users_id)




@app.route('/products/')
def showProducts():
	product = session.query(Products).all()
	return render_template('products.html',product=product)


@app.route('/products/<int:products_id>')
def historyProduct(products_id):
	#return 'main page'
	#product = session.query(Products).all()
	return render_template('historyproducts.html')


@app.route('/donor/<int:donors_id>/product/new/')
def addProduct(donors_id):
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()
	return render_template('addproduct.html', currentdonor=currentdonor)


@app.route('/storage/')
def showStorage():
	storage = session.query(Storage).all()
	return render_template('storage.html',storage=storage)


@app.route('/storage/stock/<int:storage_id>/')
def stockStorage(storage_id):
	currentstorage = session.query(Storage).filter_by(id=storage_id).one()
	products = session.query(Products).filter_by(storage_id=storage_id)
	return render_template('showstorage.html', currentstorage=currentstorage, products=products)



if __name__ == '__main__':

	app.run(debug=True)
