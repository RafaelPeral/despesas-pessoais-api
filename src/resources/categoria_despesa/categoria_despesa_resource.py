from src.controllers.categoria_despesa_controller import CategoriaDespesaController

def categoria_despesa_resource(app):
    @app.get("/categoria_despesa")
    def get_all_categorias():
        return CategoriaDespesaController().get_all()