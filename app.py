from flask import Flask, render_template, url_for
from sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CRM.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Columb(db.Integer, primary_key=True)
    name = db.Columb(db.String(30), nulable=False)
    surname = db.Columb(db.String(30), nulable=False)
    email = db.Columb(db.String(40), nulable=False)
    password = db.Columb(db.Integer, nulable=False)
    company = db.Columb(db.String(100), nulable=False)

    def __repr__(self):
        return '<Users %r>' % self.id

class Manager(db.Model):
    id = db.Columb(db.Integer, primary_key=True)
    name = db.Columb(db.String(30), nulable=False)
    surname = db.Columb(db.String(30), nulable=False)
    email = db.Columb(db.String(40), nulable=False)
    password = db.Columb(db.Integer, nulable=False)
    company = db.Columb(db.String(100), nulable=False)

    def __repr__(self):
        return '<Manager %r>' % self.id

class Project(db.Model):
    id = db.Columb(db.Integer, primary_key=True)
    nameP = db.Columb(db.String(30), nulable=False)
    status = db.Columb(db.String(30), nulable=False)
    date = db.Columb(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Project %r>' % self.id

class Task(db.Model):
    id = db.Columb(db.Integer, primary_key=True)
    nameT = db.Columb(db.String(30), nulable=False)
    status = db.Columb(db.String(30), nulable=False)
    date = db.Columb(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

class SubTask(db.Model):
    id = db.Columb(db.Integer, primary_key=True)
    nameST = db.Columb(db.String(30), nulable=False)
    status = db.Columb(db.String(30), nulable=False)
    comm = db.Columb(db.String(250), nulable=False)
    date = db.Columb(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<SubTask %r>' % self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/entry')
def signup():
    return render_template("entry.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/task_table')
def task():
    return render_template("task_table.html")

if __name__ == "__main__":
    app.run(debug=True)
