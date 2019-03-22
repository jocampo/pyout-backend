import os

import sqlalchemy as db

from src.db.platforms import Platform
from src.db.adset import Adset
from src.db.gender import Gender
from src.db.geolocation import Geolocation


class DBWrapper:
    def __init__(self):
        conn_string = os.environ.get("DBCONNSTRING", "")

        if conn_string == "":
            raise Exception("Could not connect to the database. Unable to fetch the connection string")

        engine = db.create_engine(conn_string)
        metadata = db.MetaData()
        self._platform = Platform(engine=engine, metadata=metadata)
        self._adset = Adset(engine=engine, metadata=metadata)
        self._gender = Gender(engine=engine, metadata=metadata)
        self._geolocation = Geolocation(engine=engine, metadata=metadata)

    def get_all_adsets(self):
        if self._adset:
            return self._adset.list_all_adsets()
        return []

    def get_all_composite_adsets(self):
        if self._adset:
            return self._adset.list_composite_adsets()
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
            return self._platform.list_all_platforms()
        return []

    def create_platforms(self, name):
        if name:
            self._platform.set_name(name)
            self._platform.create_platform()

    def create_gender(self, name):
        if name:
            self._gender.set_gender_name(name)
            return self._gender.create_gender()

    def create_adset(self,platform_id,gender_id, geolocation_id,name,active):
        if gender_id and geolocation_id and platform_id:
            self._adset.set_name(name)
            self._adset.set_active(active)
            self._adset.create_adset(platform_id,gender_id,geolocation_id)
