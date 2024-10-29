from models.configs.connection import DBConnectionHendler
from models.entities.forma_pagamento import FormaPagamento

class FormaPagamentoRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(FormaPagamento).all()
            return [
            {
                'id': forma_pagamento.id,
                'name': forma_pagamento.name,
            }
            for forma_pagamento in data
            ]
    
    def insert(self, forma_pagamento: FormaPagamento) -> None:
        with DBConnectionHendler() as db:
            db.session.add(forma_pagamento)
            db.session.commit()
    
    def delete_by_name(self, name: str) -> None:
        with DBConnectionHendler() as db:
            db.session.query(FormaPagamento).filter(FormaPagamento.name == name).delete()
            db.session.commit()