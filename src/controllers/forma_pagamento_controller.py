from models.repository.forma_pagamento_repository import FormaPagamentoRepository
from models.entities.formas_pagamento import FormasPagamento
import json

class FormaPagamentoController:
    def get_all(self) -> dict:
        def __format_response(data: list) -> list:
            return {
                "cont": len(data),
                "data": data
            }
        
        try:
            self.forma_pagamento_repository = FormaPagamentoRepository()
            data = self.forma_pagamento_repository.get_all()
            response = __format_response(data=data)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
        
    def insert(self, forma_pagamento: dict) -> dict:
        def __format_response(forma_pagamento: dict) -> dict:
            return {
                "name": forma_pagamento['name']
            }

        try:
            self.forma_pagamento_repository = FormaPagamentoRepository()
            self.__validate_fields(forma_pagamento)
            self.__create_forma_pagamento(forma_pagamento)
            response = __format_response(forma_pagamento=forma_pagamento)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
    
    def __validate_fields(self, forma_pagamento: dict) -> None:
        if not 'name' in forma_pagamento or not forma_pagamento['name']:
            raise Exception('O campo name é obrigatório')
        
    def __create_forma_pagamento(self, forma_pagamento: dict) -> None:
        name = forma_pagamento['name']

        new_forma_pagamento = FormasPagamento(
            nome = name
        )

        self.forma_pagamento_repository.insert(new_forma_pagamento)

        