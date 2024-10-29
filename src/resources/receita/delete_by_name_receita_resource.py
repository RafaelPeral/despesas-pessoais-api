from flask import request
from controllers.receita_controller import ReceitaController

def delete_by_name_receita_resource(app):
    @app.delete("/delete_by_name_receita")
    def delete_by_name_receita():
        data = request.get_json()
        return ReceitaController().delete_by_name(despesa=data)