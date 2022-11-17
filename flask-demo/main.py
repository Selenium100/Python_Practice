from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
import datetime
import os
from werkzeug.utils import secure_filename

with open("config.json", "r") as c:
    params = json.load(c)["params"]
    print(params)

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
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
    date = db.Column(db.String(20), nullable=False)


class Blog(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), nullable=False)
    heading = db.Column(db.String(80), nullable=False)
    subheading = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    email = db.Column(db.String(20), nullable=False)


@app.route('/')
def welcome():
    blog = Blog.query.filter_by().all()
    return render_template('welcome.html', blog=blog)


@app.route('/blog/<string:blog_slug>', methods=['GET'])
def blog(blog_slug):
    blog = Blog.query.filter_by(slug=blog_slug).first()
    return render_template("blog.html", blog=blog)


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        subject = request.form.get('subject')
        date = datetime.datetime.now()

        if sno == '0':
            mydata = Mydata(firstname=firstname, lastname=lastname, subject=subject, date=date)
            db.session.add(mydata)
            db.session.commit()
            mail.send_message(f'New message by {firstname}', sender='nityaranjan190592@gmail.com',
                              recipients=[params['gmail-user']], body=subject)
        else:
            mydata = Mydata.query.filter_by(sno=sno).first()
            mydata.firstname = firstname
            mydata.lastname = lastname
            mydata.subject = subject
            mydata.date = datetime.datetime.now()
            db.session.commit()
            return redirect("/edit/"+sno)
        mydata = Mydata.query.filter_by(sno=sno).first()
        return render_template('edit.html',sno=sno,params=params,mydata=mydata)

    return render_template('edit.html', sno=sno, params=params)


@app.route('/AdminTaskdbEdit/<string:sno>', methods=['GET', 'POST'])
def AdminTaskdbEdit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            heading = request.form.get('heading')
            subheading = request.form.get('subheading')
            slug = request.form.get('slug')
            content = request.form.get('content')
            email = request.form.get('email')
            date = datetime.datetime.now()

            if sno == '0':
                blog = Blog(heading=heading, subheading=subheading, slug=slug, content=content, email=email, date=date)
                db.session.add(blog)
                db.session.commit()
                mail.send_message(f'New message by {slug}', sender='nityaranjan190592@gmail.com',
                                  recipients=[params['gmail-user']], body=content)
            else:
                blog = Blog.query.filter_by(sno=sno).first()
                blog.slug = slug
                blog.heading = heading
                blog.subheading = subheading
                blog.content = content
                blog.date = date
                db.session.commit()
                return redirect("/AdminTaskdbEdit/" + sno)
    blog = Blog.query.filter_by(sno=sno).first()
    return render_template('AdminTaskdbEdit.html', params=params, blog=blog, sno=sno)


@app.route('/effortdashboard', methods=['GET'])
def effortdashboard():
    mydata = Mydata.query.all()
    return render_template("taksdashboard.html", mydata=mydata)


@app.route('/dashboard', methods=['GET', 'POST'])
def login():
    if ('user' in session and session['user'] == params['admin_user']):
        blog = Blog.query.all()
        return render_template('dashboard.html', params=params, blog=blog)

    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        if username == params['admin_user'] and password == params['admin_password']:
            session['user'] = username
            blog = Blog.query.all()
            return render_template('dashboard.html', params=params, blog=blog)
        else:
            return "Usename or Password is Incorrect"
            # set session variable

    return render_template("login.html")


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


@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if ('user' in session and session['user'] == params['admin_user'] ):
        if (request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded Successfully"


@app.route('/delete/<string:sno>')
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        blog = Blog.query.filter_by(sno=sno).first()
        db.session.delete(blog)
        db.session.commit()
    return redirect('/dashboard')




@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')






app.run(debug=True)
