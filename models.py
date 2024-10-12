from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Product(db.Model) :
    __tablename__ = 'products'
    id = db.Column(db.Integer,primary_key = True)
    pname = db.Column(db.String(225),nullable = False)
    bprice = db.Column(db.Float,nullable = False)
    sprice = db.Column(db.Float,nullable = False)
    stock = db.relationship('stock', back_populates='product')
    
class Stock(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.Integer,primary_key = True)
    productid = db.Column(db.Integer,nullable = False)
    stockquantity = db.Column(db.Integer,nullable = False)
    timepurchased = db.Column(db.DateTime,default = datetime.utcnow)
    product = db.relationship('Product',backref = 'stock')

class Sale(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer,primary_key = True)
    pid = db.Column(db.Integer,db.ForeignKey('products.id'),nullable = False)
    quantity = db.Column(db.Integer,nullable = False)
    timesold = db.Column(db.DateTime,default = datetime.utcnow)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.Integer,nullable = False)
    email = db.Column(db.String(255),unique = True ,nullable = False)
    password = db.Column(db.String(255),nullable = False)



