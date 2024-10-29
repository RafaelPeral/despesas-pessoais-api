from flask import request
from controllers.categoria_receita_controller import categoriaReceitaController

def delete_by_name_categoria_receita_resource(app):
    @app.delete("/delete_by_name_categoria_receita")
    def delete_by_name_categoria_receita():
        data = request.get_json()
        return categoriaReceitaController().delete_by_name(categoria=data)