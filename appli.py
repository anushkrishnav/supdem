from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db=db)

from model import Supplier, User
from forms import UserForm, SupplierForm

@app.route("/", methods=['GET', 'POST'])
def home():
    #SupplierForm
    Sf = SupplierForm()
    Rf = UserForm()
    if request.method == "POST":
            sfor = Supplier(email=Sf.email.data, name=Sf.name.data, service=Sf.service.data)
            db.session.add(sfor)
            db.session.commit()
            flash('Congratulations, you are now a registered Supplier!')
            return redirect(url_for('data'))
    
    return render_template('index.html',form=Sf)

@app.route("/data",methods = ['GET','POST'])
def data():
    if request.method == 'GET':
        Supp = Supplier.query.all()
        return render_template('data.html',Supp=Supp)


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