from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():

    people = [
        Person("LeBron", "James"),
        Person("Barack", "Obama"),
        Person("Bill", "Gates")
    ]

    return render_template("index.html", people = people)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


if __name__ == '__main__':
    app.run()