from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template("index3.html")

@app.route('/contact')
def contact() :
    return render_template("index4.html")

@app.route('/login',methods = ["GET","POST"])
def login() :
    if request.method == "POST" :
        user = request.form["yourname"]
        session["user"] = user
        return redirect(url_for("user"))
    else :
        return render_template('login.html')

@app.route('/user')
def user() :
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else :
        return redirect(url_for("login")) 



app.run(debug=True)