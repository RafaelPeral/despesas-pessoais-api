from models.configs.connection import DBConnectionHendler
from models.entities.formas_pagamento import FormasPagamento

class FormaPagamentoRepository:
#   def get_all(self):
#       with DBConnectionHendler() as db:
#           data = db.session.query(FormasPagamento).all()
#           return data
    
    def insert(self, forma_pagamento):
        with DBConnectionHendler() as db:
            return 't'