import pandas as pd
from data.DatabaseConnector import DatabaseConnector

class DataLoader:
    def __init__(self, config: dict):
        self.db_config = config['database']
        self.schema = self.db_config['schema']
        self.table = config['table']['name']
        self.fields = config['fields']
        self.db_connector = DatabaseConnector(
            db_type=self.db_config['type'],
            host=self.db_config['host'],
            port=self.db_config['port'],
            db_name=self.db_config['name'],
            user=self.db_config['user'],
            password=self.db_config['password']
        )
        self.engine = self.db_connector.connect()

    def load_data(self) -> pd.DataFrame:
        """ Load data from the database """
        selected_fields = ', '.join(self.fields.values())
        query = f"SELECT {selected_fields} FROM {self.schema}.{self.table}"
        print(f"Requête SQL : {query}")  # For debugging
        with self.engine.connect() as connection:
            data = pd.read_sql(query, connection)

        return data
