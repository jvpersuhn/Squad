from dao.squad_dao import Squad, SquadDao

class SquadController:
    def __init__(self):
        self.sd = SquadDao()

    def select_all(self):
        lista = self.sd.select_all()
        retorno = []
        for i in lista:
            squad = Squad(i[0],i[1],i[2],i[3],i[4],i[5])
            retorno.append(squad)

        return retorno

    def select_byId(self, id):
        s = self.sd.select_byId(id)
        squad = Squad(s[0],s[1],s[2],s[3],s[4],s[5])
        return squad

    def insert(self, squad : Squad):
        self.sd.insert(squad)
    
    def update(self, squad : Squad):
        self.sd.update(squad)

    def delete(self,id):
        self.sd.delete(id)