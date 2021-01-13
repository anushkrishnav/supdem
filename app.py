from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db=db)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    service = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.password}')"

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    service  = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.password}')"

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)




"""

Hello Ma'am,
Vedant here. Hope you are enjoying the Winter!
Ma'am I had some questions
1) I am Beta MLSA and the Founder of Devscript. Almost 50% of our team comprises of MLSAs and remaining have applied and are on the way to become. We also have a series where we provide a platform and exposure to the Alpha MLSAs for their Beta Conversion sessions/event and for further events as well. I wanted to know that how Microsoft can support us in our initiative? Something apart from the benefits we get being an MLSA.

2) I am a Beta MLSA from Sept 2019 cohort and have completed 1 yr. During this period, I learnt a lot, have given tons of sessions, organised multiple events and hackathons, worked in many communities, also started one, mentored around 3000 students till date and enjoyed sharing knowledge and helping people. I am looking forward for becoming a Gold MLSA. I don't know what parameters and considered and what further should I need to do to become one. Becoming a Gold MLSA will really motivate me a lot! Will you please guide me on the same?

Thanks and Regards,
Vedant

"""