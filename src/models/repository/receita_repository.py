from models.entities.receita import Receitas
from models.configs.connection import DBConnectionHendler

class ReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(Receitas).all()
            return data