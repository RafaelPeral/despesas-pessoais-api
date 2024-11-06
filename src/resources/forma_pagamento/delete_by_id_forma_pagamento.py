from flask import request
from src.controllers.forma_pagamento_controller import FormaPagamentoController

def delete_by_id_forma_pagamento_resource(app):
    @app.delete("/delete_by_id_forma_pagamento")
    def delete_by_id_forma_pagamento():
        data = request.get_json()
        return FormaPagamentoController().delete_by_id(forma_pagamento=data)