from models.repository.despesa_repository import DespesaRepository

class DespesaController:
    def despesa(self):
        try:
            despesasrepository = DespesaRepository()
            data = despesasrepository.get_all()
            response = self.__format_response(data)
            return {"success": 200, "data": response}
        except Exception as e:
            return {"success": 500, "error": str(e)}
    
    def __format_response(self, data):
        return {
            "cont" : len(data),
            "total" : sum(data),
            "data": data
        }