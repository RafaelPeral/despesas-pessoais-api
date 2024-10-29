from models.configs.connection import DBConnectionHendler
from models.entities.forma_pagamento import formaPagamento

class FormaPagamentoRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(formaPagamento).all()
            return [
            {
                'id': forma_pagamento.id,
                'name': forma_pagamento.name,
            }
            for forma_pagamento in data
            ]
    
    def insert(self, forma_pagamento: formaPagamento) -> None:
        with DBConnectionHendler() as db:
            db.session.add(forma_pagamento)
            db.session.commit()
    
    def delete_by_name(self, name: str) -> None:
        with DBConnectionHendler() as db:
            db.session.query(formaPagamento).filter(formaPagamento.name == name).delete()
            db.session.commit()