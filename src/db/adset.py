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
        return result_set

    def create_adset(self,platform_id,gender_id, geolocation_id):
        if self._name and self._active and platform_id and gender_id and geolocation_id:
            adsets = db.Table('adsets', self._metadata, autoload=True,
                                autoload_with=self._engine)
            query = db.insert(adsets)
            values_list = [
                {'name': self._name , 'active' : self._active}, ]
            connection = self._engine.connect()
            result_proxy = connection.execute(query, values_list)
            result_set = result_proxy.fetchall()
            print(result_set)
            # Pending ids.


    def set_active(self,active):
        if active:
            self._active=active

    def set_name(self, name):
        if name:
            self._name = name

    def create_adset_geolocation (adset_id,geolocation_id):
        pass

    def create_adset_genders (adset_id,geolocation_id):
        pass