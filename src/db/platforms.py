import sqlalchemy as db


class Platform:

    def __init__(self,name=None,platform_id=None,engine=None,metadata=None):
        self._name = name
        self._platform_id = platform_id
        self._engine = engine
        self._metadata = metadata

    def list_all_platforms(self):

        platform = db.Table('platforms', self._metadata, autoload=True,
                            autoload_with=self._engine)
        query = db.select([platform])
        connection = self._engine.connect()
        result_proxy = connection.execute(query)
        return result_proxy.fetchall()

    def create_platform(self):
        platform = db.Table('platforms', self._metadata, autoload=True,
                            autoload_with=self._engine)
        query = db.insert(platform)
        values_list = [{'name': self._name}]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        result_set = result_proxy.fetchall()
        print(result_set)

    def set_name(self, name):
        self._name = name
