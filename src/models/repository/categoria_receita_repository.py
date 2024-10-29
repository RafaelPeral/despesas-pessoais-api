from models.configs.connection import DBConnectionHendler
from models.entities.categoria_receita import categoriareceita


class categoriaReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(categoriareceita).all()
            return [{
                'id': categoria_receita.id,
                'name': categoria_receita.name
            } for categoria_receita in data]

    def insert(self, categoria):
        with DBConnectionHendler() as db:
            db.session.add(categoria)
            db.session.commit()

    def delete_by_name(self, name: str):
        with DBConnectionHendler() as db:
            db.session.query(categoriareceita).filter(categoriareceita.name == name).delete()
            db.session.commit()