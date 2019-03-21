import sqlalchemy as db


class Gender:
    def __init__(self, name=None, engine=None, metadata=None):
        self._name = name
        self._id = id
        self._engine = engine
        self._metadata = metadata

    def list_all_genders(self):
        platform = db.Table('genders', self._metadata, autoload=True,
                            autoload_with=self._engine)
        query = db.select([platform])
        connection = self._engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        return result_set

    def create_gender(self):
        platform = db.Table('genders', self._metadata, autoload=True,
                            autoload_with=self._engine)
        query = db.insert(platform)
        values_list = [{'name': self._name}]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        result_set = result_proxy.fetchall()
        print(result_set)

    def set_gender_name(self, gender_name):
        self._name = gender_name
