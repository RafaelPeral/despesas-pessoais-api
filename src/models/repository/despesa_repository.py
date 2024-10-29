from models.entities.despesa import despesa
from models.configs.connection import DBConnectionHendler

class DespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(despesa).all()
            return [{
                'id': despesa.id,
                'categoria': despesa.categoria,
                'name': despesa.name,
                'date': despesa.date,
                'forma_pagamento': despesa.forma_pagamento,
                'valor': despesa.valor
            }for despesa in data]
    
    def insert(self, despesa: despesa) -> None:
        with DBConnectionHendler() as db:
            db.session.add(despesa)
            db.session.commit()
    
    def delete_by_name(self, name: str) -> None:
        with DBConnectionHendler() as db:
            db.session.query(despesa).filter(despesa.name == name).delete()
            db.session.commit()