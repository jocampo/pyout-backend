from sqlalchemy import create_engine


class Crud:
    def start(self,url = "postgres://admin123:admin123@sqlito.csvdz1qsdaks.us-east-1.rds.amazonaws.com:5432/postgres"):
        db = create_engine(url)

    def addAddSets(self):
        pass

    def deleteAddSets(self,id):
        pass

    def editAddSets(self,id):
        pass

