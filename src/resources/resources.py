from resources.despesa_resource import despesa_resource
from resources.receita_resource import receita_resource

def resources(app):
    despesa_resource(app)
    receita_resource(app)