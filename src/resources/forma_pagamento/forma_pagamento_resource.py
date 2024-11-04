from src.controllers.forma_pagamento_controller import FormaPagamentoController

def forma_pagamento_resource(app):
    @app.get("/forma_pagamento")
    def forma_pagamento():
        return FormaPagamentoController().get_all()