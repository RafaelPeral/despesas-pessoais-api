from src.models.configs.connection import DBConnectionHendler
from src.models.entities.forma_pagamento import FormaPagamento

class FormaPagamentoRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            def __sum(receita):
                return sum([receita.valor for receita in receita])
            
            data = db.session.query(FormaPagamento).all()

            return [
            {
                'id': forma_pagamento.id,
                'name': forma_pagamento.name,
                'receita': __sum(forma_pagamento.receitas),
                'despesa': __sum(forma_pagamento.despesas),
                'total': __sum(forma_pagamento.receitas) - __sum(forma_pagamento.despesas)
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

    def delete_by_id(self, id: int) -> None:
        with DBConnectionHendler() as db:
            db.session.query(FormaPagamento).filter(FormaPagamento.id == id).delete()
            db.session.commit()