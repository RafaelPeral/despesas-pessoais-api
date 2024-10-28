from flask import Flask
from resources.resources import resources

app = Flask(__name__)

resources(app)

if __name__ == "__main__":
    app.run(debug=True)