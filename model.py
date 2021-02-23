from app import db 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    firstName = db.Column(db.String(60))
    lastName = db.Column(db.String(60))
    phoneNumber = db.Column(db.String(13))
    address = db.Column(db.String(500))
    city = db.Column(db.String(20))
    service = db.Column(db.String(60))
    note = db.Column(db.String(500))
    
    def __repr__(self):
        return (f"User('{self.service}')")

    def data(self):
        l = [self.firstName,self.lastName,self.phoneNumber,self.address,  self.email,self.city,self.note,self.service]
        return l

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstName = db.Column(db.String(60))
    name = db.Column(db.String(60))
    lastName = db.Column(db.String(60))
    address = db.Column(db.String(500))
    phoneNumber = db.Column(db.String(13))
    city = db.Column(db.String(20))
    service  = db.Column(db.String(60), nullable=False)
    note = db.Column(db.String(500))


    def __repr__(self):
        return f"Supplier('{self.service}')"

    def data(self):
        l = [self.firstName,self.lastName,self.phoneNumber,self.address,  self.email,self.city,self.note,self.service]
        return l