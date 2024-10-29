from models.entities.receita import receita
from models.configs.connection import DBConnectionHendler

class ReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(receita).all()
            return data