from sqlalchemy import create_engine, MetaData


class Crud:
    def start(self, url="postgres://admin123:admin123@sqlito.csvdz1qsdaks.us-east-1.rds.amazonaws.com:5432/postgres"):
        db = create_engine(url)
        metadata = MetaData()
        print(metadata)

    def add_adsets(self):
        pass

    def delete_adsets(self, adset_id):
        pass

    def edit_adsets(self, adset_id):
        pass

