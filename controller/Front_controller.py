from dao.front_dao import FrontDb
from model.frontend import FrontEnd


class FrontController:
    def __init__(self):
        self.dao = FrontDb()

    def select_all(self):
        lista = self.dao.select_all()
        lista_retorno = []
        for b in lista:
            ba = FrontEnd(b[0], b[1], b[2], b[3])
            lista_retorno.append(ba)
        return lista_retorno
        
    
    def select_by_id(self, id):
        lista = self.dao.select_by_id(id)
        b = FrontEnd(lista[0],lista[1],lista[2],lista[3])
        return b
    
    def update(self, front : FrontEnd):
        self.dao.update(front)

    def insert(self, front : FrontEnd):
        self.dao.insert(front)
        
    def delete(self, id):
        self.dao.delete(id)

        