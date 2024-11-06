from flask import request
from src.controllers.despesa_controller import DespesaController

def delete_by_id_despesa_resource(app):
    @app.delete("/delete_by_id_despesa")
    def delete_by_id_despesa():
        data = request.get_json()
        return DespesaController().delete_by_id(despesa=data)