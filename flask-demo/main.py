from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

with open("config.json", "r") as c:
    params = json.load(c)["params"]
    print(params)

db = SQLAlchemy()
app = Flask(__name__)
if params['local_server']:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']

db.init_app(app)


class Mydata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(20), nullable=False)


@app.route('/')
def welcome():
    return "Welcome to Flask app"


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to database'''
        fname1 = request.form.get("fname")
        lname1 = request.form.get("lname")
        fsubject1 = request.form.get("fsubject")
        entry = Mydata(firstname=fname1, lastname=lname1 , subject=fsubject1)
        db.session.add(entry)
        db.session.commit()

    return render_template("index.html", params=params)


app.run(debug=True)
