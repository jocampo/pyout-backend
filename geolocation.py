
class Geolocation:

    def __init__(self,country,region,city,latitude,longitude,adSetId = None):
        self._country = country
        self._region = region
        self._city = city
        self._latitude = latitude
        self._longitude = longitude
        self._adSetId = adSetId
