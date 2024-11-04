from flask import Flask
from resources.resources import resources
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="http://localhost:5173")

resources(app)

if __name__ == "__main__":
    app.run(debug=True)