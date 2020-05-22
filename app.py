#! /usr/bin/python
import numpy as np
import psycopg2

from utils import results_utils as ru
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kkgenbnkhfumlr:7e5bf5a2961f3571a049ad287b7d3c96bc0bba6cedcf59e6c89818dffe3f3d76@ec2-54-75-229-28.eu-west-1.compute.amazonaws.com:5432/dajf2u6mmm73or'

db = SQLAlchemy(app)


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
    ages, homes, genders, educations = ru.prepare_personal_data(db, Formdata)
    sentiments = ru.calculate_sentiment(db, Formdata)
    avg_sentiment = np.mean(sentiments)
    government_scores = ru.prepare_government_status(db, Formdata)
    avg_score = np.mean(government_scores)
    ages_view, ages_badfeeling = ru.prepare_age_comparison(db, Formdata)

    return render_template('results.htm', ages=ages, homes=homes, genders=genders, educations=educations,
                           avg_sentiment=avg_sentiment, avg_score=avg_score, ages_view=ages_view,
                           ages_badfeeling=ages_badfeeling)


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
    fd = Formdata(age, home, gender, education, place, corona, easter, view, feeling, badfeeling, alcohol, eat,
                  selfimpr, job, status)
    db.session.add(fd)
    db.session.commit()

    return redirect('/results')

if __name__ == "__main__":
    #manager.run()
    app.run()
    #results()