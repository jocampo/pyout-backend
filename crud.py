import sqlalchemy as db
from platforms import Platform
from adset import Adset
from gender import Gender
from geolocation import Geolocation

class Crud:
    def start(self, url="postgres://admin123:admin123@sqlito.csvdz1qsdaks.us-east-1.rds.amazonaws.com:5432/postgres"):
        engine = db.create_engine(url)
        metadata = db.MetaData()
        self._platform = Platform(engine=engine, metadata=metadata)
        self._adset = Adset(engine=engine,metadata=metadata)
        self._gender = Gender(engine=engine, metadata=metadata)
        self._geolocation = Geolocation(engine=engine, metadata=metadata)

    def get_all_adsets(self):
        if self._adset:
            self._adset.list_all_adsets()

    def get_all_geolocations(self):
        if self._geolocation:
            self._geolocation.list_all_geolocations()

    def get_all_genders(self):
        if self._gender:
            self._gender.list_all_genders()

    def delete_adsets(self, adset_id):
        pass

    def edit_adsets(self, adset_id):
        pass

    def get_all_platforms(self):
        if self._platform:
            self._platform.list_all_platforms()
