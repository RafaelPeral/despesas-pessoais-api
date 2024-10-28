from flask import request

def add_forma_pagamento_resource(app):
    @app.post("/add_forma_pagamento")
    def add_forma_pagamento():
        return request.data