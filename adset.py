import sqlalchemy as db


class Adset:

    def __init__(self, name=None, active=None, adset_id=None, engine=None,
                 metadata=None):
        self._name = name
        self._adset_id = adset_id
        self._engine = engine
        self._metadata = metadata
        self._active = active

    def list_all_adsets(self):
        platform = db.Table('adsets', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.select([platform])
        connection = self._engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        print(result_set)

