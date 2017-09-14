from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
from models import Base, Person

@app.route('/')
def hello_world():
    person = Person("LeBron", "James")
    return render_template("index.html", person = person)

if __name__ == '__main__':
    app.run()
