from src.models.repository.categoria_despesa_repository import categoriaDespesaRepository
from src.models.entities.categoria_despesa import CategoriaDespesa

class CategoriaDespesaController:
    def get_all(self):
        def __format_response(data: list) -> list:
            return {
                "cont": len(data),
                "data": data
            }
        
        try:
            self.categoria_despesa_repository = categoriaDespesaRepository()
            data = self.categoria_despesa_repository.get_all()
            response = __format_response(data=data)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
    
    def insert(self, categoria):
        def __format_response(categoria):
            return {
                "name": categoria['name']
            }
        
        def __validate_fields(categoria):
            if not 'name' in categoria or not categoria['name']:
                raise Exception('O campo name é obrigatório')
        
        def __create_categoria(categoria):
            name = categoria['name']
            
            new_categoria = CategoriaDespesa(
                name = name
            )
            
            self.categoria_despesa_repository.insert(new_categoria)

        try:
            self.categoria_despesa_repository = categoriaDespesaRepository()
            __validate_fields(categoria)
            __create_categoria(categoria)
            response = __format_response(categoria)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}

    def delete_by_name(self, categoria):
        def __format_response(categoria):
            return {
                "name": categoria['name']
            }
        
        def __validate_fields(categoria):
            if not 'name' in categoria or not categoria['name']:
                raise Exception('O campo name é obrigatório')
        
        def __delete_categoria(categoria):
            name = categoria['name']

            self.categoria_despesa_repository.delete_by_name(name)

        try:
            self.categoria_despesa_repository = categoriaDespesaRepository()
            __validate_fields(categoria)
            __delete_categoria(categoria)
            response = __format_response(categoria)
            return {"success": 200, "data": response}
        except Exception as e:  
            return {"success": 500, "error": str(e)}