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
@app.route("/", methods=['GET', 'POST'])    # User Form
def home():
    print("home")
    Rf = UserForm()
    if request.method == "POST":
        select = request.form.get('comp_select')
        sFor = User( service=select,email=Rf.email.data,name=Rf.name.data)
        
        db.session.add(sFor)
        db.session.commit()

        flash('Congratulations, you are now a registered User!')
        # print("sFor",sFor)
        return redirect(url_for('recommendation'))
    return render_template('home.html',form=Rf)

@app.route("/supplier", methods=['GET', 'POST'])    #Supplier Form
def supplier():
    print("supplier")
    Sf = SupplierForm()
    if request.method == "POST":
        select = request.form.get('comp_select')

        sfor = Supplier(email=Sf.email.data, name=Sf.name.data, service=select)
        
        db.session.add(sfor)
        db.session.commit()
        
        flash('Congratulations, you are now a registered Supplier!')
        return redirect(url_for('home'))
    return render_template('supplier.html',form=Sf)

@app.route("/recommendation",methods = ['GET','POST'])
def recommendation():
    if request.method == 'GET':
        allSuppliers = Supplier.query.all()
        # sFor=request.args.get('sFor') 

        allUsers = User.query.all()
        # print("Supp",allSuppliers[-1].data())
        Suppliers = [allUsers[-1].data()[1]]
     
        for i in allSuppliers:
            if i.data()[1]==allUsers[-1].data()[1]:
                Suppliers.append(i)
        # print("last user",allUsers[-1].data())
        if not len(Suppliers)>1:
            return redirect(url_for('noservice'))
           
        return render_template('recommend.html',Supp=Suppliers)

@app.route("/about",methods=['GET','POST'])
def about():
    if request.method=='GET':
        return render_template('about.html')

@app.route("/noservice",methods=['GET','POST'])
def noservice():
    if request.method=='GET':
        return render_template('noservice.html')

@app.route("/data",methods = ['GET','POST'])
def data():
    if request.method == 'GET':
        Supp = Supplier.query.all()
        print("data",Supp)
        Users = User.query.all()
        return render_template('data.html',Supp=[Supp,Users])

if __name__ == '__main__':
    app.run(debug=True)    