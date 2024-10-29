#categoria_receita
from resources.categoria_receita.categoria_receita_resource import categorias_receita_resource
from resources.categoria_receita.add_categoria_receita_resource import add_categoria_receita_resource
from resources.categoria_receita.delete_by_name_categoria_receita_resource import delete_by_name_categoria_receita_resource

#despesa
from resources.despesas.despesa_resource import despesa_resource

#forma_pagamento
from resources.forma_pagamento.forma_pagamento_resource import forma_pagamento_resource
from resources.forma_pagamento.add_forma_pagamento_resource import add_forma_pagamento_resource
from resources.forma_pagamento.delete_by_name_forma_pagamento_resource import delete_by_name_forma_pagamento_resource

#receita
from resources.receita.receita_resource import receita_resource

def resources(app):
    despesa_resource(app)
    receita_resource(app)
    add_forma_pagamento_resource(app)
    forma_pagamento_resource(app)
    delete_by_name_forma_pagamento_resource(app)
    delete_by_name_categoria_receita_resource(app)
    add_categoria_receita_resource(app)
    categorias_receita_resource(app)