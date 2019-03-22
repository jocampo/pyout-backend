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
            adset_id = result_proxy.inserted_primary_key[0]

            if adset_id:
                self.create_adset_genders(adset_id=adset_id,gender_id=gender_id)
                self.create_adset_geolocation(adset_id=adset_id,geolocation_id=geolocation_id)
                self.create_adset_platforms(adset_id=adset_id,platform_id=platform_id)
            else:
                print("Inserted AdSet Id is invalid")

    def set_active(self,active):
        if active:
            self._active=active

    def set_name(self, name):
        if name:
            self._name = name

    def create_adset_geolocation (self,adset_id,geolocation_id):
        adsets = db.Table('adsets_geolocations', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.insert(adsets)
        values_list = [
            {'adset_id': adset_id, 'geolocation_id':geolocation_id}, ]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        return result_proxy.inserted_primary_key

    def create_adset_genders (self,adset_id,gender_id):
        adsets = db.Table('adsets_genders', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.insert(adsets)
        values_list = [
            {'adset_id': adset_id, 'gender_id': gender_id}, ]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        return result_proxy.inserted_primary_key

    def create_adset_platforms (self,adset_id,platform_id):
        adsets = db.Table('adsets_platforms', self._metadata, autoload=True,
                          autoload_with=self._engine)
        query = db.insert(adsets)
        values_list = [
            {'adset_id': adset_id, 'platform_id': platform_id}, ]
        connection = self._engine.connect()
        result_proxy = connection.execute(query, values_list)
        return result_proxy.inserted_primary_key
