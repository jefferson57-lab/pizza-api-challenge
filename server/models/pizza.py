from server.extensions import db

class Pizza(db.Model):

    __tablename__='pizzas'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    ingredients=db.Column(db.String(255), nullable=False)

    #Relationship
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')


    def __repr__(self):
        return f'<Pizza {self.name}, {self.ingredients}>'
    
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'ingredients':self.ingredients
        }