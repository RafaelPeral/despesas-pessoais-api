from flask import request
from src.controllers.receita_controller import ReceitaController

def add_receita_resource(app):
    @app.post("/add_receita")
    def add_receita():
        data = request.get_json()
        return ReceitaController().insert(receita=data)