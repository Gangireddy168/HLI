from flask import Flask, render_template, request, url_for, redirect

from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017")
db=client['USER']
studentdetails=db.USERS
app=Flask(__name__)
@app.route("/crudexample")
def sample():
    return render_template("registraion.html")

@app.route("/success", methods=['GET', 'POST'])
def onsubmit2():
    uname = request.form.get('UserName')
    email=request.form.get('EMAIL')
    password=request.form.get('Password')
    Cpassword = request.form.get('ConfirmPassword')


    c={"user":uname,"Email":email,"Password":password,"CoPassword":Cpassword}

    studentdetails.insert_one(c)

    return render_template("login.html")



@app.route("/login1", methods=['GET', 'POST'])
def onlogin():
    email=request.form.get('EMAIL')
    password=request.form.get('Pwd')


    c={"Email":email,"Password":password}
    d = {"Email": "gangireddyb03", "Password": "Chinna168"}


    b = studentdetails.find_one(c)

    if c==d:
        return render_template("adminbasepage.html")
    elif b:
        return redirect(url_for('home'))
    else:
        return render_template("login.html")




@app.route("/")
def home():
    return render_template("home.html")
@app.route("/register")
def registration():
    return render_template("registration.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")
@app.route("/policys")
def policys():
    return render_template("policys.html")
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/contact us")
def contactus():
    return render_template("contact us.html")
@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")
@app.route("/adminbasepage")
def adminbasepage():
    return render_template("adminbasepage.html")
@app.route("/adminaddpolicy")
def adminaddpolicy():
    return render_template("adminaddpolicy.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")




if __name__ == "__main__":
    app.run()



