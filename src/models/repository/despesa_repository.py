from models.entities.despesa import despesa
from models.configs.connection import DBConnectionHendler

class DespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(despesa).all()
            return data