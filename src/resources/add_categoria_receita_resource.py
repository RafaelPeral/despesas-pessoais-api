from flask import request
from controllers.categorias_receita_controller import CategoriasReceitaController

def add_categoria_receita_resource(app):
    @app.post("/add_categoria_receita")
    def add_categoria_receita():
        data = request.get_json()
        return CategoriasReceitaController().insert(categoria=data)