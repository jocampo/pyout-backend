from flask import Flask
from flask_restful import Api
from src.api.controllers.gender_controller import GenderController


# Create the application instance
app = Flask(__name__)
api = Api(app, "/api")

api.add_resource(GenderController, "/genders")

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
