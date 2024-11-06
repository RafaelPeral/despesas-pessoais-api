from flask import request
from src.controllers.categoria_despesa_controller import CategoriaDespesaController


def delete_by_id_categoria_despesa_resource(app):
    @app.delete("/delete_by_id_categoria_despesa")
    def delete_by_id_categoria_despesa():
        data = request.get_json()
        return CategoriaDespesaController().delete_by_id(categoria=data)