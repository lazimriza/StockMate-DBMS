from flask import Flask
from routes.auth_routes import auth_blueprint
from routes.product_routes import product_blueprint

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Register Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(product_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
