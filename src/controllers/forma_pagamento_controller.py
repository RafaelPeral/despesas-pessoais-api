from src.models.repository.forma_pagamento_repository import FormaPagamentoRepository
from src.models.entities.forma_pagamento import FormaPagamento

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
        
        def __validate_fields(forma_pagamento: dict) -> None:
            if not 'name' in forma_pagamento or not forma_pagamento['name']:
                raise Exception('O campo name é obrigatório')

        def __create_forma_pagamento(forma_pagamento: dict) -> None:
            name = forma_pagamento['name']

            new_forma_pagamento = FormaPagamento(
                name = name
            )

            self.forma_pagamento_repository.insert(new_forma_pagamento)

        try:
            self.forma_pagamento_repository = FormaPagamentoRepository()
            __validate_fields(forma_pagamento)
            __create_forma_pagamento(forma_pagamento)
            response = __format_response(forma_pagamento=forma_pagamento)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
        
    def delete_by_name(self, forma_pagamento: str) -> None:
        def __format_response(forma_pagamento: str) -> dict:
            return {
                "name": forma_pagamento['name']
            }

        def __validate_fields(forma_pagamento: str) -> None:
            if not 'name' in forma_pagamento or not forma_pagamento['name']:
                raise Exception('O campo name é obrigatório')
        
        def __delete_forma_pagamento(forma_pagamento: str) -> None:
            name = forma_pagamento['name']

            self.forma_pagamento_repository.delete_by_name(name)

        try:
            self.forma_pagamento_repository = FormaPagamentoRepository()
            __validate_fields(forma_pagamento)
            __delete_forma_pagamento(forma_pagamento)
            response = __format_response(forma_pagamento=forma_pagamento)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
        
    def delete_by_id(self, forma_pagamento: str) -> None:
        def __format_response(forma_pagamento: str) -> dict:
            return {
                "id": forma_pagamento['id']
            }

        def __validate_fields(forma_pagamento: str) -> None:
            if not 'id' in forma_pagamento or not forma_pagamento['id']:
                raise Exception('O campo id é obrigatório')
        
        def __delete_forma_pagamento(forma_pagamento: str) -> None:
            self.forma_pagamento_repository.delete_by_id(forma_pagamento['id'])

        try:
            self.forma_pagamento_repository = FormaPagamentoRepository()
            __validate_fields(forma_pagamento)
            __delete_forma_pagamento(forma_pagamento)
            response = __format_response(forma_pagamento=forma_pagamento)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}