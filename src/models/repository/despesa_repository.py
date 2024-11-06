from src.models.entities.despesa import Despesa
from src.models.configs.connection import DBConnectionHendler

class DespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(Despesa).all()
            return [{
                'id': despesa.id,
                'categoria': despesa.categoria,
                'name': despesa.name,
                'date': despesa.date,
                'forma_pagamento_name': despesa.forma_pagamento_name,
                'valor': despesa.valor
            }for despesa in data]
    
    def insert(self, despesa: Despesa) -> None:
        with DBConnectionHendler() as db:
            db.session.add(despesa)
            db.session.commit()
    
    def delete_by_name(self, name: str) -> None:
        with DBConnectionHendler() as db:
            db.session.query(Despesa).filter(Despesa.name == name).delete()
            db.session.commit()
    
    def delete_by_id(self, id: int) -> None:
        with DBConnectionHendler() as db:
            db.session.query(Despesa).filter(Despesa.id == id).delete()
            db.session.commit()