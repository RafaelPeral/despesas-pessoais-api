from src.models.repository.despesa_repository import DespesaRepository
from src.models.entities.despesa import Despesa
from src.models.entities.forma_pagamento import FormaPagamento
from src.models.entities.categoria_despesa import CategoriaDespesa
from src.models.configs.connection import DBConnectionHendler

class DespesaController:
    def get_all(self):
        def __format_response(data):
            def cont (data):
                total = 0
                for c in data:
                    total += c['valor']
                return total
            
            return {
                "cont" : len(data),
                "total" : cont(data),
                "data": data
            }
        
        try:
            despesarepository = DespesaRepository()
            data = despesarepository.get_all()
            response = __format_response(data)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
    
    def insert(self, despesa):
        def __format_response(despesa):
            return {
                "categoria": despesa['categoria'],
                "name": despesa['name'],
                "date": despesa['date'],
                "forma_pagamento_name": despesa['forma_pagamento_name'],
                "valor": despesa['valor']
            }
        
        def __validate_fields(despesa):
            def __categoria_despesa_exists(categoria):
                with DBConnectionHendler() as db:
                    return db.session.query(CategoriaDespesa).filter_by(name=categoria).first() is not None
            
            def __forma_pagamento_exists(forma_pagamento):
                with DBConnectionHendler() as db:
                    return db.session.query(FormaPagamento).filter_by(name=forma_pagamento).first() is not None

            if not 'categoria' in despesa or not despesa['categoria']:
                raise Exception('O campo categoria é obrigatório')
            if not 'name' in despesa or not despesa['name']:
                raise Exception('O campo name é obrigatório')
            if not 'date' in despesa or not despesa['date']:
                raise Exception('O campo date é obrigatório')
            if not 'forma_pagamento_name' in despesa or not despesa['forma_pagamento_name']:
                raise Exception('O campo forma_pagamento_name é obrigatório')
            if not 'valor' in despesa or not despesa['valor']:
                raise Exception('O campo valor é obrigatório')
            
            if not __categoria_despesa_exists(despesa['categoria']):
                raise Exception('A categoria informada não existe')
            if not __forma_pagamento_exists(despesa['forma_pagamento_name']):
                raise Exception('A forma de pagamento informada não existe')
        
        def __create_despesa(despesa):
            categoria = despesa['categoria']
            name = despesa['name']
            date = despesa['date']
            forma_pagamento_name = despesa['forma_pagamento_name']
            valor = despesa['valor']

            new_despesa = Despesa(
                categoria = categoria,
                name = name,
                date = date,
                forma_pagamento_name = forma_pagamento_name,
                valor = valor
            )
            
            self.despesa_repository.insert(new_despesa)
        
        try:
            self.despesa_repository = DespesaRepository()
            __validate_fields(despesa)
            __create_despesa(despesa)
            response = __format_response(despesa)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
        
    def delete_by_name(self, despesa):
        def __format_response(despesa):
            return {
                "name": despesa['name']
            }
        
        def __validate_fields(despesa):
            if not 'name' in despesa or not despesa['name']:
                raise Exception('O campo name é obrigatório')
        
        def __delete_despesa(despesa):
            name = despesa['name']
            
            self.despesa_repository.delete_by_name(name)
        
        try:
            self.despesa_repository = DespesaRepository()
            __validate_fields(despesa)
            __delete_despesa(despesa)
            response = __format_response(despesa)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
        
    def delete_by_id(self, despesa):
        def __format_response(despesa):
            return {
                "id": despesa['id']
            }
        
        def __validate_fields(despesa):
            if not 'id' in despesa or not despesa['id']:
                raise Exception('O campo id é obrigatório')
        
        def __delete_despesa(despesa):
            self.despesa_repository.delete_by_id(despesa['id'])
        
        try:
            self.despesa_repository = DespesaRepository()
            __validate_fields(despesa)
            __delete_despesa(despesa)
            response = __format_response(despesa)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}