from models.configs.connection import DBConnectionHendler
from models.entities.categoria_despesa import categoriaDespesa


class categoriaDespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            data = db.session.query(categoriaDespesa).all()
            return [{
                'id': categoria_despesa.id,
                'name': categoria_despesa.name
            }for categoria_despesa in data]
    
    def insert(self, categoria_despesa: categoriaDespesa):
        with DBConnectionHendler() as db:
            db.session.add(categoria_despesa)
            db.session.commit()
    
    def delete_by_name(self, name: str):
        with DBConnectionHendler() as db:
            db.session.query(categoriaDespesa).filter(categoriaDespesa.name == name).delete()
            db.session.commit()
    