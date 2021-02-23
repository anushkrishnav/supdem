from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db=db)


from forms import UserForm, SupplierForm
from model import Supplier, User
@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])    # User Form
def home():
    print("home")
    Rf = UserForm()
    if request.method == "POST":
        service = request.form.get('service')
        city = request.form.get('city')
        print("city",city)
        sFor = User( service=service,email=Rf.email.data,firstName=Rf.firstName.data,lastName=Rf.lastName.data,address=Rf.address.data,phoneNumber=Rf.phoneNumber.data,city=city,note=Rf.note.data)
        
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
        service = request.form.get('service')
        city = request.form.get('city')

        sfor = Supplier(service=service,email=Sf.email.data,firstName=Sf.firstName.data,lastName=Sf.lastName.data,address=Sf.address.data,phoneNumber=Sf.phoneNumber.data,city=city,note=Sf.note.data)
        
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
        # print("all suppliers",allSuppliers)
        # print("allUsers",allUsers)
        for i in allSuppliers:
            # print("test",i.data()[-1],allUsers[-1].data()[-1])
            if i.data()[-1]==allUsers[-1].data()[-1] and i.data()[-3]==allUsers[-1].data()[-3] :
                Suppliers.append(i)
        # print("last user",allUsers[-1].data())
        # print(Suppliers[0],type(Suppliers[0]))
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
    