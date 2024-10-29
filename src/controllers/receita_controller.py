from models.repository.receita_repository import ReceitaRepository
from models.entities.receita import Receita

class ReceitaController:
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
            self.receita_repository = ReceitaRepository()
            data = self.receita_repository.get_all()
            response = __format_response(data)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}        

    def insert(self, receita):
        def __format_response(receita):
            return {
                "categoria": receita['categoria'],
                "name": receita['name'],
                "date": receita['date'],
                "forma_pagamento": receita['forma_pagamento'],
                "valor": receita['valor']
            }
        
        def __validate_fields(receita):
            if not 'categoria' in receita or not receita['categoria']:
                raise Exception('O campo categoria é obrigatório')
            if not 'name' in receita or not receita['name']:
                raise Exception('O campo name é obrigatório')
            if not 'date' in receita or not receita['date']:
                raise Exception('O campo date é obrigatório')
            if not 'forma_pagamento' in receita or not receita['forma_pagamento']:
                raise Exception('O campo forma_pagamento é obrigatório')
            if not 'valor' in receita or not receita['valor']:
                raise Exception('O campo valor é obrigatório')
        
        def __create_receita(receita):
            categoria = receita['categoria']
            name = receita['name']
            date = receita['date']
            forma_pagamento = receita['forma_pagamento']
            valor = receita['valor']

            new_receita = Receita(
                categoria = categoria,
                name = name,
                date = date,
                forma_pagamento = forma_pagamento,
                valor = valor
            )
            
            self.receita_repository.insert(new_receita)

        try:
            self.receita_repository = ReceitaRepository()
            __validate_fields(receita)
            __create_receita(receita)
            response = __format_response(receita)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
    
    def delete_by_name(self, receita):
        def __format_response(receita):
            return {
                "name": receita['name']
            }
        
        def __validate_fields(receita):
            if not 'name' in receita or not receita['name']:
                raise Exception('O campo name é obrigatório')
        
        def __delete_receita(receita):
            name = receita['name']

            self.receita_repository.delete_by_name(name)

        try:
            self.receita_repository = ReceitaRepository()
            __validate_fields(receita)
            __delete_receita(receita)
            response = __format_response(receita)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}