from flask import request
from controllers.despesa_controller import DespesaController

def add_categoria_despesa_resource(app):
    @app.post("/add_categoria_despesa")
    def add_categoria_despesa():
        data = request.get_json()
        return DespesaController().insert(despesa=data)