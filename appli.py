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
@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def home():
    #User Form
    # Rf = UserForm()
    # sFor = request.form['contact']
    # print(sFor)
    if request.method == "POST":
            # sFor = request.form['contact']#User(email=Rf.email.data, name=Rf.name.data, service=Rf.service.data)

            return redirect(url_for('recommendation',sFor=sFor))
    
    return render_template('home.html')#,form=Rf)

@app.route("/supplier", methods=['GET', 'POST'])
def supplier():
    #Supplier Form
    Sf = SupplierForm()
    Rf = UserForm()
    if request.method == "POST":
            sfor = Supplier(email=Sf.email.data, name=Sf.name.data, service=Sf.service.data)
            db.session.add(sfor)
            db.session.commit()
            flash('Congratulations, you are now a registered Supplier!')
            return redirect(url_for('home'))

    return render_template('supplier.html',form=Sf)

@app.route("/data",methods = ['GET','POST'])
def data():
    if request.method == 'GET':
        Supp = Supplier.query.all()
        print("data",Supp)
        
        return render_template('data.html',Supp=Supp)

@app.route("/recommendation",methods = ['GET','POST'])
def recommendation():
    if request.method == 'GET':
        Supp = Supplier.query.all()
        sFor=request.args.get('sFor')
        print("recomme",sFor)
        return render_template('recommend.html',Supp=Supp)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
