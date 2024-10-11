from sqlalchemy import create_engine

class DatabaseConnector:
    def __init__(self, db_type: str, user: str, password: str, host: str, port: int, db_name: str):
        self.db_type = db_type
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.engine = None

    def connect(self):
        if self.db_type == 'mysql':
            self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}')
        elif self.db_type == 'postgresql':
            self.engine = create_engine(f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}')
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")
        return self.engine
