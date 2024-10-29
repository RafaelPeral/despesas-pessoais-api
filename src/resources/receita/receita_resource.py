from controllers.receita_controller import ReceitaController

def receita_resource(app):
    @app.get("/receita")
    def receita():
        return ReceitaController().get_all()