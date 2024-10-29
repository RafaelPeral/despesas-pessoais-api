from models.configs.connection import DBConnectionHendler
from models.entities.formas_pagamento import FormasPagamento

class FormaPagamentoRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(FormasPagamento).all()
            return [
            {
                'id': forma_pagamento.id,
                'nome': forma_pagamento.nome,
            }
            for forma_pagamento in data
            ]
    
    def insert(self, forma_pagamento: FormasPagamento) -> None:
        with DBConnectionHendler() as db:
            db.session.add(forma_pagamento)
            db.session.commit()