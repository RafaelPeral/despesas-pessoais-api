from flask import request
from src.controllers.categoria_receita_controller import CategoriaReceitaController

def add_categoria_receita_resource(app):
    @app.post("/add_categoria_receita")
    def add_categoria_receita():
        data = request.get_json()
        return CategoriaReceitaController().insert(categoria=data)