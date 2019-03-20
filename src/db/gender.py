
class Gender:
    def __init__(self, name=None, gender_id=None, db=None,engine=None, metadata=None):
        self._name = name
        self._id = id
        self._engine = engine
        self._metadata = metadata

    def list_all_genders(self):
        import sqlalchemy as db
        platform = db.Table('genders', self._metadata, autoload=True,
                            autoload_with=self._engine)
        query = db.select([platform])
        connection = self._engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        return result_set
