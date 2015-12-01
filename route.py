from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Donors, Products, Medication


app = Flask(__name__)


engine = create_engine('sqlite:///newBlood.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




@app.route('/')
def main():
	countusers = session.query(func.count(Users.id)).scalar()
	countdonors = session.query(func.count(Donors.id)).scalar()
	countproducts = session.query(func.count(Products.id)).scalar()
	countmedication = session.query(func.count(Medication.id)).scalar()
	return render_template('main.html',countdonors=countdonors,countusers=countusers,countproducts=countproducts,countmedication=countmedication)
	


@app.route('/users/')
def showUsers():
	user = session.query(Users).all()
	return render_template('users.html', user=user)


@app.route('/user/<int:users_id>/')
def historyUser(users_id):
	currentuser = session.query(Users).filter_by(id=users_id).one()
	donors = session.query(Donors).filter_by(users_id=users_id)
	# count = session.query(Donors).filter_by(users_id=users_id).scalar()
	# count = session.query(func.count(Donors.id)).scalar() GIVES ALL DONORS
	#count = session.query(Products).filter_by(donors_id=donors_id)
	count = session.query(func.count('*')).select_from(Products).scalar()

	return render_template('currentuser.html',currentuser=currentuser, donors=donors,count=count)


# @app.route('/user/new/', methods=['GET','POST'])
# def newUser():
# 	if request.method == 'POST':
# 		newuser = Users(name=request.form['name'])	
# 		session.add(newuser)
# 		session.commit()
# 		return redirect(url_for('showUsers'))
# 	else:
# 		return render_template('newuser.html')

@app.route('/user/new/', methods=['GET','POST'])
def newUser():
	if request.method == 'POST':
		newuser = Users(name=request.form['name'])	
		session.add(newuser)
		session.commit()
		return redirect(url_for('showUsers'))
	else:
		return render_template('newuser.html')





@app.route('/donors/')
def showDonors():
	donor = session.query(Donors).all()
	return render_template('donors.html',donor=donor)


@app.route('/donors/profile/<int:donors_id>/')
def profileDonors(donors_id):
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()	
	return render_template('profiledonor.html',currentdonor=currentdonor)


@app.route('/donors/info/<int:donors_id>/')
def infoDonors(donors_id):
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()	
	return render_template('infodonor.html',currentdonor=currentdonor)



@app.route('/donors/<int:donors_id>')
def historyDonors(donors_id):
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()
	products = session.query(Products).filter_by(donors_id=donors_id)
	return render_template('currentdonor.html',currentdonor=currentdonor, products=products)


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


# @app.route('/products/donors/<int:donors_id>/')
# def historyProduct(donors_id):
# 	currentdonor = session.query(Donors).filter_by(id=donors_id).one()

# 	#return 'main page'
# 	#product = session.query(Products).all()
# 	return render_template('historyproducts.html',currentdonor=currentdonor)



@app.route('/products/<int:products_id>')
def historyProduct(products_id):
	#return 'main page'
	#product = session.query(Products).all()
	return render_template('historyproducts.html')


@app.route('/donor/<int:donors_id>/product/new/', methods=['GET', 'POST'])
def addProduct(donors_id):
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()
	if request.method == 'POST':
		newProduct = Products(
			bcode=request.form['bcode'],
			product_code=request.form['product_code'],
			type=request.form['type'],
			exp_date=request.form['exp_date'],
			donors_id=donors_id
			)
		session.add(newProduct)
		session.commit()
		return redirect(url_for('historyDonors', donors_id=donors_id))
	else:
		return render_template('addproduct.html',currentdonor=currentdonor, donors_id=donors_id)





@app.route('/medication/')
def showMedication():
	medication = session.query(Medication).all()
	return render_template('medication.html',medication=medication)


@app.route('/medication/<int:donors_id>/')
def donorMedication(donors_id):
	#medication = session.query(Medication).all()
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()
	currentmedication = session.query(Medication).filter_by(donors_id=donors_id)
	return render_template('donormedication.html',currentdonor=currentdonor,currentmedication=currentmedication)


@app.route('/medication/<int:donors_id>/new', methods=['GET', 'POST'])
def addMedication(donors_id):
	currentdonor = session.query(Donors).filter_by(id=donors_id).one()
	if request.method == 'POST':
		newmedication = Medication(
			name=request.form['name'],
			sideffects=request.form['sideffects'],
			donors_id=donors_id
			)
		session.add(newmedication)
		session.commit()
		return redirect(url_for('donorMedication', donors_id=donors_id))
	else:
		return render_template('addmedication.html',currentdonor=currentdonor, donors_id=donors_id)


######## delete from database area ######

# DELETE MENU ITEM SOLUTION

@app.route('/medication/<int:donors_id>/<int:medication_id>/',methods=['GET', 'POST'])
def deleteMedication(donors_id,medication_id):
    medtodelete = session.query(Medication).filter_by(id=medication_id).one()
    currentdonor = session.query(Donors).filter_by(id=donors_id).one()
    if request.method == 'POST':
        session.delete(medtodelete)
        session.commit()
        return redirect(url_for('donorMedication',donors_id=donors_id))
    else:
      return render_template('deletemedication.html', medtodelete=medtodelete,currentdonor=currentdonor)


# @app.route('/product/<int:donors_id>/<int:products_id>/',methods=['GET', 'POST'])
# def deleteProduct(donors_id,product_id):
#     productodelete = session.query(Products).filter_by(id=product_id).one()
#     currentdonor = session.query(Donors).filter_by(id=donors_id).one()
#     if request.method == 'POST':
#         session.delete(productodelete)
#         session.commit()
#         return redirect(url_for('donorMedication',donors_id=donors_id))
#     else:
#       return render_template('deletemedication.html', medtodelete=medtodelete, currentdonor=currentdonor)


if __name__ == '__main__':

	app.run(debug=True)
