from src.models.repository.categoria_receita_repository import categoriaReceitaRepository
from src.models.entities.categoria_receita import CategoriaReceita

class CategoriaReceitaController:
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
            
            new_categoria = CategoriaReceita(
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
        
        def __delete_categoria(categoria: str) -> None:
            name = categoria['name']

            self.categoria_receita_repository.delete_by_name(name)

        try:
            self.categoria_receita_repository = categoriaReceitaRepository()
            __validate_fields(categoria)
            __delete_categoria(categoria)
            response = __format_response(categoria=categoria)
            return {"success": 200, "data": response}
        except Exception as e:  
            return {"success": 500, "error": str(e)}
        
    def delete_by_id(self, categoria: str):
        def __format_response(categoria: str) -> dict:
            return {
                "id": categoria['id']
            }
        
        def __validate_fields(categoria: str) -> None:
            if not 'id' in categoria or not categoria['id']:
                raise Exception('O campo id é obrigatório')
        
        def __delete_categoria(categoria: str) -> None:
            self.categoria_receita_repository.delete_by_id(categoria['id'])

        try:
            self.categoria_receita_repository = categoriaReceitaRepository()
            __validate_fields(categoria)
            __delete_categoria(categoria)
            response = __format_response(categoria=categoria)
            return {"success": 200, "data": response}
        except Exception as e:  
            return {"success": 500, "error": str(e)}