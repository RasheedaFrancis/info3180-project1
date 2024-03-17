from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Double)
    property_type = db.Column(db.String(50))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    def __init__(self, title, description, bedrooms, bathrooms, price, property_type, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type =property_type
        self.location = location
        self.photo = photo
        
    
    
    def get_id(self):
        try:
            return unicode(self.id)  
        except NameError:
            return str(self.id)  


    def __repr__(self):
        return '<Property %r>' % self.title



