from flask import request
from controllers.despesa_controller import DespesaController

def add_receita_resource(app):
    @app.post("/add_receita")
    def add_receita():
        data = request.get_json()
        return DespesaController().insert(despesa=data)