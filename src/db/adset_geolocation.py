import sqlalchemy as db


class AdsetGeolocation:
    def __init__(self, adset_id=None, geolocation_id=None, engine=None,
                 metadata=None):
        self._adset_id = adset_id
        self._geolocation_id = geolocation_id
        self._engine = engine
        self._metadata = metadata

    def create_adset_geolocation (self):
        adsets = db.Table('adsets_geolocations', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.insert(adsets)
        values_list = [
            {'adset_id': self._adset_id, 'geolocation_id':self._geolocation_id}, ]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        return result_proxy.inserted_primary_key