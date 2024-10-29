from models.configs.connection import DBConnectionHendler
from models.entities.categoria_despesa import CategoriaDespesa


class categoriaDespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(CategoriaDespesa).all()
            return [{
                'id': categoria_despesa.id,
                'name': categoria_despesa.name
            }for categoria_despesa in data]
    
    def insert(self, categoria_despesa: CategoriaDespesa):
        with DBConnectionHendler() as db:
            db.session.add(categoria_despesa)
            db.session.commit()
    
    def delete_by_name(self, name: str):
        with DBConnectionHendler() as db:
            db.session.query(CategoriaDespesa).filter(CategoriaDespesa.name == name).delete()
            db.session.commit()
    