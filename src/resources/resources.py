#categoria_despesa
from resources.categoria_despesa.categoria_despesa_resource import categoria_despesa_resource
from resources.categoria_despesa.add_categoria_despesa_resourse import add_receita_resource
from resources.categoria_despesa.delete_by_name_categoria_despesa_resource import delete_by_name_categoria_despesa_resource

#categoria_receita
from resources.categoria_receita.categoria_receita_resource import categoria_receita_resource
from resources.categoria_receita.add_categoria_receita_resource import add_categoria_receita_resource
from resources.categoria_receita.delete_by_name_categoria_receita_resource import delete_by_name_categoria_receita_resource

#despesa
from resources.despesa.despesa_resource import despesa_resource
from resources.despesa.add_despesa_resource import add_despesa_resource
from resources.despesa.delete_by_name_despesa_resource import delete_by_name_despesa_resource

#forma_pagamento
from resources.forma_pagamento.forma_pagamento_resource import forma_pagamento_resource
from resources.forma_pagamento.add_forma_pagamento_resource import add_forma_pagamento_resource
from resources.forma_pagamento.delete_by_name_forma_pagamento_resource import delete_by_name_forma_pagamento_resource

#receita
from resources.receita.receita_resource import receita_resource
from resources.receita.add_receita_resource import add_receita_resource
from resources.receita.delete_by_name_receita_resource import delete_by_name_receita_resource

def resources(app):
    #categoria_despesa
    add_receita_resource(app)
    delete_by_name_categoria_despesa_resource(app)
    categoria_despesa_resource(app)

    #categoria_receita
    add_categoria_receita_resource(app)
    delete_by_name_categoria_receita_resource(app)  
    categoria_receita_resource(app)

    #despesa
    add_despesa_resource(app)
    delete_by_name_despesa_resource(app)
    despesa_resource(app)

    #forma_pagamento
    add_forma_pagamento_resource(app)
    delete_by_name_forma_pagamento_resource(app)
    forma_pagamento_resource(app)

    #receita
    add_receita_resource(app)
    delete_by_name_receita_resource(app)
    receita_resource(app)