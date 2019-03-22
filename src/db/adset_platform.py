import sqlalchemy as db


class AdsetPlatform:
    def __init__(self, adset_id=None,platform_id = None, engine=None,
                 metadata=None):
        self._adset_id = adset_id
        self._platform_id = platform_id
        self._engine = engine
        self._metadata = metadata

    def create_adset_platform (self):
        adsets_genders = db.Table('adsets_platforms', self._metadata, autoload=True,
                                  autoload_with=self._engine)
        query = db.insert(adsets_genders)
        values_list = [
            {'adset_id': self._adset_id, 'platform_id':self._platform_id}, ]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        return result_proxy.inserted_primary_key