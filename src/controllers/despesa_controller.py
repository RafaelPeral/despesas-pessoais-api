from models.repository.despesa_repository import DespesaRepository
from models.entities.despesa import Despesa

class DespesaController:
    def get_all(self):
        def __format_response(data):
            return {
                "cont" : len(data),
                "total" : sum(data),
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
                "forma_pagamento": despesa['forma_pagamento'],
                "valor": despesa['valor']
            }
        
        def __validate_fields(despesa):
            if not 'categoria' in despesa or not despesa['categoria']:
                raise Exception('O campo categoria é obrigatório')
            if not 'name' in despesa or not despesa['name']:
                raise Exception('O campo name é obrigatório')
            if not 'date' in despesa or not despesa['date']:
                raise Exception('O campo date é obrigatório')
            if not 'forma_pagamento' in despesa or not despesa['forma_pagamento']:
                raise Exception('O campo forma_pagamento é obrigatório')
            if not 'valor' in despesa or not despesa['valor']:
                raise Exception('O campo valor é obrigatório')
        
        def __create_despesa(despesa):
            categoria = despesa['categoria']
            name = despesa['name']
            date = despesa['date']
            forma_pagamento = despesa['forma_pagamento']
            valor = despesa['valor']

            new_despesa = Despesa(
                categoria = categoria,
                name = name,
                date = date,
                forma_pagamento = forma_pagamento,
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