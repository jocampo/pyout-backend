import sqlalchemy as db


class AdsetGender:
    def __init__(self, adset_id=None,gender_id = None, engine=None,
                 metadata=None):
        self._adset_id = adset_id
        self._gender_id = gender_id
        self._engine = engine
        self._metadata = metadata

    def create_adset_gender(self):
        adsets_genders = db.Table('adsets_genders', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.insert(adsets_genders)
        values_list = [
            {'adset_id': self._adset_id, 'gender_id':self._gender_id}, ]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        return result_proxy.inserted_primary_key