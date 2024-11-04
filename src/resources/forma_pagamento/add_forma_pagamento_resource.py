from flask import request
from src.controllers.forma_pagamento_controller import FormaPagamentoController

def add_forma_pagamento_resource(app):
    @app.post("/add_forma_pagamento")
    def add_forma_pagamento():
        data = request.get_json()
        return FormaPagamentoController().insert(forma_pagamento=data)