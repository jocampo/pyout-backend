from flask_restful import Resource
from src.db.db_wrapper import DBWrapper
from flask_jsonpify import jsonify


class PlatformController(Resource):
    def get(self):
        """Returns all platforms from the database"""
        db_wrapper = DBWrapper()
        platforms_response = db_wrapper.get_all_platforms()
        return jsonify({'platforms': [dict(row) for row in platforms_response]})
