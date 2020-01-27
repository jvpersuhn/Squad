from dao.squad_dao import Squad, SquadDao
from controller.Back_controller import BackController
from controller.Front_controller import FrontController
from controller.sgbd_controller import SGBD_controller

class SquadController:
    def __init__(self):
        self.sd = SquadDao()

    def select_all(self):
        lista = self.sd.select_all()
        retorno = []
        sc = SGBD_controller()
        bc = BackController()
        fc = FrontController()
        for i in lista:
            squad = Squad(i[0],i[1],i[2],i[3])
            squad.id_sgbd = i[4]
            squad.id_linguagemBack = i[5]
            squad.id_linguagemFront = i[6]
            if i[6] != None:
                squad.sgbd = sc.select_byId(i[6])
            if i[5] != None:
                squad.linguagemBack = bc.select_by_id(i[5])
            if i[4] != None:
                squad.linguagemFront = fc.select_by_id(i[4])
            retorno.append(squad)

        return retorno

    def select_byId(self, id):
        s = self.sd.select_byId(id)
        squad = Squad(s[0],s[1],s[2],s[3])
        squad.id_sgbd = s[4]
        squad.id_linguagemBack = s[5]
        squad.id_linguagemFront = s[6]
        return squad

    def insert(self, squad : Squad):
        self.sd.insert(squad)
    
    def update(self, squad : Squad):
        self.sd.update(squad)

    def delete(self,id):
        self.sd.delete(id)