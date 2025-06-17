from flask import Flask
from server.config import Config
from server.extensions import db, migrate
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
from server.models import restaurant, pizza, restaurant_pizza

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# Register the Blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)




if __name__ == '__main__':
    app.run(debug=True)