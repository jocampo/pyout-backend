import os

from flask import Flask
from flask_restful import Api

from src.api.controllers.gender_controller import GenderController
from src.api.controllers.geolocations_controller import GeolocationsController
from src.api.controllers.platform_controller import PlatformController


# Create the application instance
app = Flask(__name__)
api = Api(app, "/api")

api.add_resource(GenderController, "/genders")
api.add_resource(GeolocationsController, "/geolocations")
api.add_resource(PlatformController, "/platforms")

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
