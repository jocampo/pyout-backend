from flask_restful import Resource
from src.db.db_wrapper import DBWrapper
from flask_jsonpify import jsonify


class GeolocationsController(Resource):
    def get(self):
        """Returns all geolocations from the database"""
        db_wrapper = DBWrapper()
        geolocations_response = db_wrapper.get_all_geolocations()
        return jsonify({'geolocations': [dict(row) for row in geolocations_response]})
