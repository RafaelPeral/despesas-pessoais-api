from models.repository.categoria_receita_repository import categoriaReceitaRepository
from models.entities.categoria_receita import categoriareceita

class categoriaReceitaController:
    def get_all(self):
        def __format_response(data: list) -> list:
            return {
                "cont": len(data),
                "data": data
            }
        
        try:
            self.categoria_receita_repository = categoriaReceitaRepository()
            data = self.categoria_receita_repository.get_all()
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
                print(categoria)
                raise Exception('O campo name é obrigatório')
        
        def __create_categoria(categoria):
            name = categoria['name']
            
            new_categoria = categoriareceita(
                name = name
            )
            
            self.categoria_receita_repository.insert(new_categoria)

        try:
            self.categoria_receita_repository = categoriaReceitaRepository()
            __validate_fields(categoria)
            __create_categoria(categoria)
            response = __format_response(categoria)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
    
    def delete_by_name(self, categoria: str):
        def __format_response(categoria: str) -> dict:
            return {
                "name": categoria['name']
            }
        
        def __validate_fields(categoria: str) -> None:
            if not 'name' in categoria or not categoria['name']:
                raise Exception('O campo name é obrigatório')
        
        try:
            self.categoria_receita_repository = categoriaReceitaRepository()
            __validate_fields(categoria)
            self.categoria_receita_repository.delete_by_name(categoria['name'])
            response = __format_response(categoria=categoria)
            return {"success": 200, "data": response}
        except Exception as e:  
            return {"success": 500, "error": str(e)}