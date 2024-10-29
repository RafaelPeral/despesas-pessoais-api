from flask import request
from controllers.categoria_receita_controller import categoriaReceitaController

def add_categoria_receita_resource(app):
    @app.post("/add_categoria_receita")
    def add_categoria_receita():
        data = request.get_json()
        return categoriaReceitaController().insert(categoria=data)