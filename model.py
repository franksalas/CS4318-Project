
from route import db



class Donors(db.Model):

    __tablename__ = "donors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, first_name, last_name, address, dob, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.dob = dob
        self.user_id = user_id

    def __repr__(self):
        return '<name {0}>'.format(self.name)


class Products(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    bcode = db.Column(db.String, nullable=False)
    product_code = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    exp_date = db.Column(db.String, nullable=False)
    donors_id = db.Column(db.Integer, db.ForeignKey('donors.id'))

    def __init__(self, bcode, product_code, type, exp_date, donors_id):
        self.bcode = bcode
        self.product_code = product_code
        self.type = type
        self.exp_date = exp_date
        self.donors_id = donors_id

    def __repr__(self):
        return '<name {0}>'.format(self.name)


class Medication(db.Model):

    __tablename__ = "medication"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sideffects = db.Column(db.String, nullable=False)
    donors_id = db.Column(db.Integer, db.ForeignKey('donors.id'))

    def __init__(self, name, sideffects, donors_id):
        self.name = name
        self.sideffects = sideffects
        self.donors_id = donors_id

    def __repr__(self):
        return '<name {0}>'.format(self.name)


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    #donors = db.relationship('Donors', backref='donor')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<User {0}>'.format(self.name)