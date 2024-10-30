from models.configs.connection import DBConnectionHendler
from models.entities.categoria_receita import CategoriaReceita


class categoriaReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            def sum_receitas(receita):
                return sum([receita.valor for receita in receita])
            
            data = db.session.query(CategoriaReceita).all()

            return [{
                'id': categoria_receita.id,
                'name': categoria_receita.name,
                'receita': sum_receitas(categoria_receita.receitas)
            } for categoria_receita in data]

    def insert(self, categoria):
        with DBConnectionHendler() as db:
            db.session.add(categoria)
            db.session.commit()

    def delete_by_name(self, name: str):
        with DBConnectionHendler() as db:
            db.session.query(CategoriaReceita).filter(CategoriaReceita.name == name).delete()
            db.session.commit()