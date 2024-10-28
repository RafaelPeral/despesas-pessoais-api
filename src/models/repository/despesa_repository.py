from models.entities.despesas import Despesas
from models.configs.connection import DBConnectionHendler

class DespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(Despesas).all()
            return data