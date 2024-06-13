from flask import Flask
from routes.amenities_routes import amenities_bp
from routes.places_routes import places_bp
from routes.reviews_routes import reviews_bp
from routes.user_routes import users_bp
from routes.countries_routes import countries_bp

app = Flask(__name__)
app.register_blueprint(amenities_bp)
app.register_blueprint(places_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(users_bp)
app.register_blueprint(countries_bp)

if __name__ == '__main__':
    app.run(debug=True)