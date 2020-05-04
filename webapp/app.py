#! /usr/bin/python

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wyniki.db'
db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    age = db.Column(db.Integer)
    home = db.Column(db.String)
    gender = db.Column(db.Integer)
    alcohol = db.Column(db.Integer)
    government = db.Column(db.Integer)
    corona = db.Column(db.Integer)
    eat = db.Column(db.Integer)
    feeling = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __init__(self, age, home, gender, alcohol, government, corona, eat, feeling, status):
        self.age = age
        self.home = home
        self.gender = gender
        self.alcohol = alcohol
        self.government = government
        self.corona = corona
        self.eat = eat
        self.feeling = feeling
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
def reasults():
    return render_template('results.htm')

@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    age = request.form['age']
    home = request.form['home']
    gender = request.form['gender']
    alcohol = request.form['alcohol']
    government = request.form['government']
    corona = request.form['corona']
    eat = request.form['eat']
    feeling = request.form['feeling']
    status = request.form['status']
    # Save the data
    fd = Formdata(age, home, gender, alcohol, government, corona, eat, feeling, status)
    db.session.add(fd)
    db.session.commit()

    return redirect('/results')

if __name__ == "__main__":
    app.run(debug=True)