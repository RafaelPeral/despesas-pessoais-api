from controllers.categorias_receita_controller import CategoriasReceitaController

def categorias_receita_resource(app):
    @app.get("/categorias_receita")
    def categorias_receita():
        return CategoriasReceitaController().get_all()