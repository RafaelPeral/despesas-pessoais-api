from flask import request
from controllers.despesa_controller import DespesaController

def add_despesa_resource(app):
    @app.post("/add_despesa")
    def add_despesa():
        data = request.get_json()
        return DespesaController().insert(despesa=data)