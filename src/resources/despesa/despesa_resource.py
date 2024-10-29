from controllers.despesa_controller import DespesaController

def despesa_resource(app):
    @app.get("/despesa")
    def despesa():
        return DespesaController().get_all()