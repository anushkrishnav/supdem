from appli import db 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    service = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.name}')"

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    service  = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Supplier('{self.name}')"
