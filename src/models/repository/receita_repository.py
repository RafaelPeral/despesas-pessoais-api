from src.models.entities.receita import Receita
from src.models.configs.connection import DBConnectionHendler

class ReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(Receita).all()
            return [{
                'id': receita.id,
                'categoria': receita.categoria,
                'name': receita.name,
                'date': receita.date,
                'forma_pagamento_name': receita.forma_pagamento_name,
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
    
    def delete_by_id(self, id: int) -> None:
        with DBConnectionHendler() as db:
            db.session.query(Receita).filter(Receita.id == id).delete()
            db.session.commit()