from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHendler:
    def __init__(self):
        self.__username = "despesas_pessoais_db_user"
        self.__password = "J7CaAZQ0uv8qGMfya1K5oBvvjF78ZzUp"
        self.__host = "dpg-csfp8v2j1k6c73b1uek0-a.oregon-postgres.render.com"
        self.__port = "5432"
        self.__database = "despesas_pessoais_db"
        self.__connection_string = "postgresql://{}:{}@{}/{}".format(self.__username, self.__password, self.__host, self.__database)
        self.__engine = self.__create_databese_engine()
        self.session = None

    def __create_databese_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()