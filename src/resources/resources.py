from resources.despesa_resource import despesa_resource
from resources.receita_resource import receita_resource
from resources.add_forma_pagamento_resource import add_forma_pagamento_resource
from resources.forma_pagamento_resource import forma_pagamento_resource
from resources.delete_by_name_forma_pagamento_resource import delete_by_name_forma_pagamento_resource
from resources.delete_by_name_categoria_receita_resource import delete_by_name_categoria_receita_resource
from resources.add_categoria_receita_resource import add_categoria_receita_resource
from resources.categoria_receita_resource import categorias_receita_resource

def resources(app):
    despesa_resource(app)
    receita_resource(app)
    add_forma_pagamento_resource(app)
    forma_pagamento_resource(app)
    delete_by_name_forma_pagamento_resource(app)
    delete_by_name_categoria_receita_resource(app)
    add_categoria_receita_resource(app)
    categorias_receita_resource(app)