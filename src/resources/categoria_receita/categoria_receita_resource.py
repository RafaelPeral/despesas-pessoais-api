from src.controllers.categoria_receita_controller import CategoriaReceitaController

def categoria_receita_resource(app):
    @app.get("/categoria_receita")
    def categoria_receita():
        return CategoriaReceitaController().get_all()