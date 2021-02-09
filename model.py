from appli import db 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120) )
    name = db.Column(db.String(60) )
    address = db.Column(db.String(500))
    service = db.Column(db.String(60))
    
    def __repr__(self):
        return (f"User('{self.service}')")

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    service  = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Supplier('{self.name}')"
