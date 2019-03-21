import sqlalchemy as db
from src.db.platforms import Platform
from src.db.adset import Adset
from src.db.gender import Gender
from src.db.geolocation import Geolocation


class DBWrapper:
    def __init__(self, url="postgres://admin123:admin123@sqlito.csvdz1qsdaks.us-east-1.rds.amazonaws.com:5432/postgres"):
        engine = db.create_engine(url)
        metadata = db.MetaData()
        self._platform = Platform(engine=engine, metadata=metadata)
        self._adset = Adset(engine=engine,metadata=metadata)
        self._gender = Gender(engine=engine, metadata=metadata)
        self._geolocation = Geolocation(engine=engine, metadata=metadata)

    def get_all_adsets(self):
        if self._adset:
            return self._adset.list_all_adsets()
        return []

    def get_all_geolocations(self):
        if self._geolocation:
            return self._geolocation.list_all_geolocations()
        return []

    def get_all_genders(self):
        if self._gender:
            return self._gender.list_all_genders()
        return []

    def delete_adsets(self, adset_id):
        pass

    def edit_adsets(self, adset_id):
        pass

    def get_all_platforms(self):
        if self._platform:
            self._platform.list_all_platforms()

    def create_platforms(self,name):
        if name:
            self._platform.set_name(name)
            self._platform.create_platform()

    def create_gender(self,name):
        if name:
            self._gender.set_gender_name(name)
            self._gender.create_gender()
