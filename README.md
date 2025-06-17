🍕 Pizza Restaurant API Challenge
Project Overview
A robust REST API for managing pizza restaurants, their menu items, and associations. Built with:

Flask (Python web framework)

SQLAlchemy (ORM)

Flask-Migrate (database migrations)

PostgreSQL (production-grade database)

Key Features:
✔️ Full CRUD operations for restaurants
✔️ Comprehensive pizza menu management
✔️ Association management with validation
✔️ Production-ready architecture

🚀 Quick Start Guide
Prerequisites
Python 3.8+

PostgreSQL

Pipenv (recommended)

Installation
bash
git clone https://github.com/jefferson57-lab/pizza-api-challenge.git
cd pizza-api-challenge
pipenv install && pipenv shell
Database Setup
bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python -m server.seed  # Populate with sample data
Running the Server
bash
flask run
🔍 API Endpoints
Endpoint	Method	Description
/restaurants	GET	List all restaurants
/restaurants/<id>	GET	Get restaurant details
/restaurants/<id>	DELETE	Remove a restaurant
/pizzas	GET	List all pizza options
/restaurant_pizzas	POST	Create new pizza association
📝 Request/Response Examples
Get All Restaurants

bash
curl http://localhost:5000/restaurants
Create Pizza Association

bash
curl -X POST http://localhost:5000/restaurant_pizzas \
  -H "Content-Type: application/json" \
  -d '{"price": 12.99, "pizza_id": 1, "restaurant_id": 3}'
⚖️ Validation Rules
Price Validation:

Database level: CHECK constraint (1 ≤ price ≤ 30)

Application level: Flask validation

Required Fields:

price, restaurant_id, pizza_id

Error Responses:

400 Bad Request for invalid data

404 Not Found for missing resources

🧪 Testing Guide
Import challenge-1-pizzas.postman_collection.json into Postman

Start server: flask run

Verify:

Successful CRUD operations

Proper error handling

Validation enforcement
