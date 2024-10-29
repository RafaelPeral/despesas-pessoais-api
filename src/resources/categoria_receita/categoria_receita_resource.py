from controllers.categoria_receita_controller import categoriaReceitaController

def categoria_receita_resource(app):
    @app.get("/categoria_receita")
    def categoria_receita():
        return categoriaReceitaController().get_all()