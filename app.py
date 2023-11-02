from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


class Home(Resource):
    def get(self):
        response_message = {
            "message": "pizza app."
        }
        return make_response(response_message, 200)


class Restaurants(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
            }
            restaurant_list.append(restaurant_dict)
        return make_response(jsonify(restaurant_list), 200)


class RestaurantByID(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            restaurant_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [
                    {
                        "id": pizza.id,
                        "name": pizza.name,
                        "ingredients": pizza.ingredients,
                    }
                    for pizza in restaurant.pizzas
                ]
            }
            return make_response(jsonify(restaurant_dict), 200)
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)


class DeleteRestaurant(Resource):
    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)
        
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        
        db.session.delete(restaurant)
        db.session.commit()
        
        return make_response("", 204)


class Pizzas(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizza_list = []
        for pizza in pizzas:
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients,
            }
            pizza_list.append(pizza_dict)
        return make_response(jsonify(pizza_list), 200)


class RestaurantPizzas(Resource):
    def post(self):
        data = request.get_json()
        price = data.get("price")
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")
        
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        if not pizza or not restaurant:
            return make_response(jsonify({"error": "Pizza or Restaurant doesn't exist"}), 400)
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        response_data = {
            "id": restaurant_pizza.id,
            "restaurant_id": restaurant_pizza.restaurant.id,
            "pizza_id": restaurant_pizza.pizza.id,
            "price": restaurant_pizza.price,
        }
        return make_response(jsonify(response_data), 201)


@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: The requested resource does not exist.",
        404
    )
    return response


api.add_resource(Home, '/')
api.add_resource(Restaurants, '/restaurants')
api.add_resource(RestaurantByID, '/restaurants/<int:id>')
api.add_resource(DeleteRestaurant, '/restaurants/<int:id>')
api.add_resource(Pizzas, '/pizzas')
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)