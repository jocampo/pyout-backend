from flask_restful import Resource
from src.db.crud import Crud
from flask_jsonpify import jsonify


class GenderController(Resource):
    def get(self):
        """Returns all genders from the database"""
        db_wrapper = Crud()
        db_wrapper.start()
        genders_response = db_wrapper.get_all_genders()
        return jsonify({'genders': [dict(row) for row in genders_response]})
