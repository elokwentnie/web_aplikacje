#! /usr/bin/python

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wyniki.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    age = db.Column(db.Integer)
    home = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    education = db.Column(db.Integer)
    place = db.Column(db.Integer)
    corona = db.Column(db.Integer)
    easter = db.Column(db.Integer)
    view = db.Column(db.Integer)
    feeling = db.Column(db.Integer)
    badfeeling = db.Column(db.Integer)
    alcohol = db.Column(db.Integer)
    eat = db.Column(db.Integer)
    selfimpr = db.Column(db.Integer)
    job = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __init__(self, age, home, gender, education, place, corona, easter, view, feeling, badfeeling, alcohol, eat, selfimpr, job, status):
        self.age = age
        self.home = home
        self.gender = gender
        self.education = education
        self.place = place
        self.corona = corona
        self.easter = easter
        self.view = view
        self.feeling = feeling
        self.badfeeling = badfeeling
        self.alcohol = alcohol
        self.eat = eat
        self.selfimpr = selfimpr
        self.job = job
        self.status = status


@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/about')
def about():
    return render_template('about.htm')


@app.route('/form', methods=['GET','POST'])
def form():
    return render_template('form.htm')


@app.route('/team')
def team():
    return render_template('team.htm')


@app.route('/results', methods=['GET','POST'])
def results():
    # store the available options representations
    age_options = {1: 'Poniżej 18 lat', 2: '18-25 lat', 3: '25-40 lat', 4: 'Powyżej 40 lat'}
    home_options = {1: "Wieś", 2: "Miasto (do 50 tys. mieszkancow)", 3: "Miasto (50 - 500 tys. mieszkancow", 4: "Miasto (+ 500 tys. mieszkańców)"}
    gender_options = {1: "Mężczyzna", 2: "Kobieta", 3: "Nie chcę podawać"}
    personal_data = db.session.query(Formdata.age, Formdata.home, Formdata.gender).all()
    # create data for rendering
    ages = [[age_options[opt], len([x[0] for x in personal_data if x[0] == opt])] for opt in age_options.keys()]
    homes = [[home_options[opt], len([x[1] for x in personal_data if x[1] == opt])] for opt in home_options.keys()]
    genders = [[gender_options[opt], len([x[2] for x in personal_data if x[2] == opt])] for opt in gender_options.keys()]

    return render_template('results.htm', ages=ages, homes=homes, genders=genders)

@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    age = request.form['age']
    home = request.form['home']
    gender = request.form['gender']
    education = request.form['education']
    place = request.form['place']
    corona = request.form['corona']
    easter = request.form['easter']
    view = request.form['view']
    feeling = request.form['feeling']
    badfeeling = request.form['badfeeling']
    alcohol = request.form['alcohol']
    eat = request.form['eat']
    selfimpr = request.form['selfimpr']
    job = request.form['job']
    status = request.form['status']
    # Save the data
    fd = Formdata(age, home, gender, education, place, corona, easter, view, feeling, badfeeling, alcohol, eat, selfimpr, job, status)
    db.session.add(fd)
    db.session.commit()

    return redirect('/results')

if __name__ == "__main__":
    #manager.run()
    app.run(debug=True)