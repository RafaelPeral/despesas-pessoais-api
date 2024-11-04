from src.models.configs.connection import DBConnectionHendler
from src.models.entities.categoria_despesa import CategoriaDespesa


class categoriaDespesaRepository:
    def get_all(self):
        with DBConnectionHendler() as db:
            def sum_despesas(despesa):
                return sum([despesa.valor for despesa in despesa])
            
            data = db.session.query(CategoriaDespesa).all()

            return [{
                'id': categoria_despesa.id,
                'name': categoria_despesa.name,
                'despesa': sum_despesas(categoria_despesa.despesas)
            }for categoria_despesa in data]
    
    def insert(self, categoria_despesa: CategoriaDespesa):
        with DBConnectionHendler() as db:
            db.session.add(categoria_despesa)
            db.session.commit()
    
    def delete_by_name(self, name: str):
        with DBConnectionHendler() as db:
            db.session.query(CategoriaDespesa).filter(CategoriaDespesa.name == name).delete()
            db.session.commit()
    