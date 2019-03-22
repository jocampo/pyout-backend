from flask_restful import Resource
from src.db.db_wrapper import DBWrapper
from flask_jsonpify import jsonify


class AdsetsController(Resource):
    def get(self):
        """Returns all adsets from the database"""
        db_wrapper = DBWrapper()
        adsets_response = db_wrapper.get_all_composite_adsets()
        return jsonify({'adsets': [dict(row) for row in adsets_response]})

    def post(self):
        """Creates an adset"""
        return {"status": "Success"}, 201
