from flask import Flask
from .routes.mapas_routes import mapas_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(mapas_bp)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
