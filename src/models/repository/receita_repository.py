from models.entities.receita import Receita
from models.configs.connection import DBConnectionHendler

class ReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(Receita).all()
            return [{
                'id': receita.id,
                'categoria': receita.categoria,
                'name': receita.name,
                'date': receita.date,
                'forma_pagamento': receita.forma_pagamento,
                'valor': receita.valor
            }for receita in data]

    def insert(self, receita: Receita) -> None:
        with DBConnectionHendler() as db:
            db.session.add(receita)
            db.session.commit()

    def delete_by_name(self, name: str) -> None:
        with DBConnectionHendler() as db:
            db.session.query(Receita).filter(Receita.name == name).delete()
            db.session.commit()