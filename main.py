from flask import Flask, render_template, request, redirect, url_for,flash,session
from dbservice import (
    fetcheddata,
    profitsperday,
    insertproducts,
    insertsales,
    salesperproduct,
    profitsperproduct,
    salesperday,
    profitsperday,
    insertusers,
    checkemail,
)
from flask_bcrypt import Bcrypt 


# Create an instance
# configure your application
# define routes
# run the application
app = Flask(__name__)
bcrypt = Bcrypt(app) 
app.secret_key = 'cd7a45a8c7975c87f573c2a1d86e10e6d278be20bba17b3b05c10895ea476203'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/products")
def products():
    if "email" not in session :
        return redirect(url_for('login'))
    prods = fetcheddata("products")
    return render_template("products.html", prods=prods)


@app.route("/addproducts", methods=["GET", "POST"])
def addproducts():
    # check the method
    if request.method == "POST":
        # Requst data
        pname = request.form["pname"]
        bprice = request.form["buyingprice"]
        sprice = request.form["sellingprice"]
        squantity = request.form["quantity"]
        # insert products
        newprod = (pname, bprice, sprice, squantity)
        insertproducts(newprod)
        session['email'] = email
        return redirect(url_for("products"))


@app.route("/sales")
def sales():
    if "email" not in session :
        return redirect(url_for('login'))
    sales = fetcheddata("sales")
    products = fetcheddata("products")
    return render_template("sales.html", sales=sales, products=products)


@app.route("/makesales", methods=["GET", "POST"])
def makesales():
    if request.method == "POST":
        pname = request.form["pid"]
        quantity = request.form["quantity"]
        salesmade = (pname, quantity)
        insertsales(salesmade)
        session['email'] = email
        return redirect(url_for("sales"))


@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "POST" :
        fname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash (password).decode('utf-8')

        x = checkemail(email)
        if x == None:
            newuser = (fname,email,hashed_password)
            insertusers(newuser)
            flash("registered successful")
            return redirect(url_for("login"))
        else :
            flash("email already exists")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/login',methods = ["GET","POST"])
def login() :
    if request.method == "POST" :
        # get form data
        email = request.form["email"]
        password = request.form["password"]
        cemail = checkemail(email)
        print(cemail)
        if cemail == None:
            flash("email does not exist")
            return redirect(url_for("register"))
        else :
            # check password
            if bcrypt.check_password_hash(cemail[-1],password):
                flash("Login successful")
                session['email'] = email
                return redirect(url_for("dashboard"))
            else :
                flash("Incorrect passowrd")    
    return render_template("login.html")    

@app.route("/dashboard")
def dashboard():
    if "email" not in session :
        flash("Login for access")
        return redirect(url_for('login'))
    # salesperproduct
    sproducts = salesperproduct()
    # print(sproducts)
    names = []
    sales = []
    # print(profitspproduct)
    for i in sproducts:
        names.append(i[1])
        sales.append(float(i[0]))
    # profitsperproduct
    pname = []
    profits = []
    profitspproduct = profitsperproduct()
    for m in profitspproduct:
        pname.append(m[1])
        profits.append(float(m[0]))

    salespday = salesperday()
    sales1 = []
    day = []
    for i in salespday:
        sales1.append(i[0])
        day.append(str(i[1]))

    profitspday = profitsperday()
    profits1 = []
    day1 = []
    for i in profitspday:
        profits1.append(i[0])
        day1.append(str(i[1]))

    return render_template(
        "dashboard.html",
        names=names,
        sales=sales,
        profits=profits,
        pname=pname,
        sales1=sales1,
        day=day,
        profits1=profits1,
        day1=day1,
    )

@app.route('/logout')
def logout() :
    session.pop('email',None)
    return redirect(url_for('login'))


@app.route("/profitsmade")
def profitsmade():
    profitsmade = profitsperday()
    return render_template("profits.html", profitsmade=profitsmade)


@app.route("/year")
def year():
    return "2001"

app.run(debug=True)


# URL => Uniform Resource Locator e.g: https://jumia.com
# Routes => connects a url into a function..any route should start with a forward slash e.g: https://techcamp.co.ke/home
# flask uses templating where html files are placed inside the templates folder
# All css and javascript are placed inside the static


# create html files for each route
# products.html
# home.html
# sales.html
# dashboard.html
