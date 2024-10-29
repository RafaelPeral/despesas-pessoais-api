from controllers.categoria_despesa_controller import CategoriaDespesaController

def categoria_despesa_resource(app):
    @app.get("/get_all_categorias")
    def get_all_categorias():
        return CategoriaDespesaController().get_all()