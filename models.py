from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    
    pizzas_association = db.relationship('RestaurantPizza', back_populates='restaurant', overlaps="pizzas")
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    restaurants_association = db.relationship('RestaurantPizza', back_populates='pizza', overlaps="pizzas")
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    restaurant = db.relationship('Restaurant', back_populates='pizzas_association')
    pizza = db.relationship('Pizza', back_populates='restaurants_association')

    @validates('price')
    def validate_price(self, key, value):
        value = int(value)
        if not 1 <= value <= 30:
            raise ValueError("Price must be between 1 and 30.")
        return value