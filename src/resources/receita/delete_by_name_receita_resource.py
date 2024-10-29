from flask import request
from controllers.despesa_controller import DespesaController

def delete_by_name_receita_resource(app):
    @app.delete("/add_receita")
    def delete_by_name_receita():
        data = request.get_json()
        return DespesaController().delete_by_name(despesa=data)