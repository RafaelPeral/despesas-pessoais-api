from flask import request
from controllers.categorias_receita_controller import CategoriasReceitaController

def delete_by_name_categoria_receita_resource(app):
    @app.delete("/delete_by_name_categoria_receita")
    def delete_by_name_categoria_receita():
        data = request.get_json()
        return CategoriasReceitaController().delete_by_name(categoria=data)