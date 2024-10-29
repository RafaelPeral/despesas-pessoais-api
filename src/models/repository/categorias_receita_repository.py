from models.configs.connection import DBConnectionHendler
from models.entities.categorias_receitas import CategoriasReceitas


class CategoriasReceitaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(CategoriasReceitas).all()
            return [{
                'id': categorias_receitas.id,
                'name': categorias_receitas.name
            } for categorias_receitas in data]

    def insert(self, categoria):
        with DBConnectionHendler() as db:
            db.session.add(categoria)
            db.session.commit()

    def delete_by_name(self, name: str):
        with DBConnectionHendler() as db:
            db.session.query(CategoriasReceitas).filter(CategoriasReceitas.name == name).delete()
            db.session.commit()