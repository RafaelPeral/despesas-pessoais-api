from flask import request
from src.controllers.categoria_despesa_controller import CategoriaDespesaController

def add_categoria_despesa_resource(app):
    @app.post("/add_categoria_despesa")
    def add_categoria_despesa():
        data = request.get_json()
        return CategoriaDespesaController().insert(categoria=data)