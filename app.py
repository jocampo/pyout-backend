from flask import Flask
from flask_restful import Api
from src.api.controllers.gender_controller import GenderController
import os


# Create the application instance
app = Flask(__name__)
api = Api(app, "/api")

api.add_resource(GenderController, "/genders")

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
