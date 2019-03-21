import sqlalchemy as db


class Geolocation:

    def __init__(self, country=None, region=None, city=None, latitude=None, longitude=None, adset_id=None, engine=None,
                 metadata=None):
        self._country = country
        self._region = region
        self._city = city
        self._latitude = latitude
        self._longitude = longitude
        self._adSetId = adset_id
        self._engine = engine
        self._metadata = metadata

    def list_all_geolocations(self):
        platform = db.Table('geolocations', self._metadata, autoload=True,
                            autoload_with=self._engine)
        query = db.select([platform])
        connection = self._engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        print(result_set)
        return result_set
