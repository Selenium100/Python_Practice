from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail

with open("config.json", "r") as c:
    params = json.load(c)["params"]
    print(params)

db = SQLAlchemy()
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
if params['local_server']:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']

db.init_app(app)


class Mydata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(20), nullable=False)


class Blog(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), nullable=False)
    heading = db.Column(db.String(80), nullable=False)
    subheading = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(10000), nullable=False)


@app.route('/')
def welcome():
    return "Welcome to Flask app"


@app.route('/blog/<string:blog_slug>', methods=['GET'])
def blog(blog_slug):
    blog = Blog.query.filter_by(slug=blog_slug).first()
    return render_template("blog.html", blog=blog)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to database'''
        fname1 = request.form.get("fname")
        lname1 = request.form.get("lname")
        fsubject1 = request.form.get("fsubject")
        entry = Mydata(firstname=fname1, lastname=lname1, subject=fsubject1)
        db.session.add(entry)
        db.session.commit()
        mail.send_message(f'New message by {fname1}', sender='nityaranjan190592@gmail.com',
                          recipients=[params['gmail-user']], body=fsubject1)

    return render_template("index.html", params=params)


app.run(debug=True)
