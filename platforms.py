

class Platform:

    def __init__(self,name=None,platform_id=None,engine=None,metadata=None):
        self._name = name
        self._platform_id = platform_id
        self._engine = engine
        self._metadata = metadata

    def list_all_platforms(self):
        import sqlalchemy as db
        platform = db.Table('adsets_platforms', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.select([platform])
        connection = self._engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        print(result_set)

