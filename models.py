from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Product(db.Model) :
    __tablename__ = 'products'
    id = db.Column(db.integer,primary_key = True)
    pname = db.Column(db.string(225),nullable = False)
    bprice = db.Column(db.float,nullable = False)
    sprice = db.Column(db.float,nullable = False)
    
class stock(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.integer,primary_key = True)
    productid = db.Column(db.integer,nullable = False)
    stockquantity = db.Column(db.integer,nullable = False)
    timepurchased = db.Column(db.DateTime,default = datetime.utcnow)
    product = db.relationship('Product',backref = 'stock')

class Sale(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.integer,primary_key = True)
    pid = db.Column(db.integer,db.ForeignKey('products.id'),nullable = False)
    quantity = db.Column(db.integer,nullable = False)
    timesold = db.Column(db.DateTime,default = datetime.utcnow)

class User(db.Model):
    id = db.Column(db.integer,primary_key = True)
    fullname = db.Column(db.integer,nullable = False)
    email = db.Column(db.string(255),unique = True ,nullable = False)
    password = db.Column(db.strung(255),nullable = False)

