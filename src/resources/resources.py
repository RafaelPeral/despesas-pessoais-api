from resources.despesa_resource import despesa_resource
from resources.receita_resource import receita_resource
from resources.add_forma_pagamento_resource import add_forma_pagamento_resource
from resources.forma_pagamento_resource import forma_pagamento_resource

def resources(app):
    despesa_resource(app)
    receita_resource(app)
    add_forma_pagamento_resource(app)
    forma_pagamento_resource(app)