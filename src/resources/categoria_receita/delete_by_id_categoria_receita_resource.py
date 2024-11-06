from flask import request
from src.controllers.categoria_receita_controller import CategoriaReceitaController

def delete_by_id_categoria_receita_resource(app):
    @app.delete("/delete_by_id_categoria_receita")
    def delete_by_id_categoria_receita():
        data = request.get_json()
        return CategoriaReceitaController().delete_by_id(categoria=data)