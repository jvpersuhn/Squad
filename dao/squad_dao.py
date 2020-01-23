from dao.conexao import Conexao
from model.squad import Squad
from model.backend import BackEnd
from model.frontend import FrontEnd
from model.sgbd import SGBD

class SquadDao(Conexao):
    def select_all(self):
        self.cursor.execute("SELECT * FROM 02_JVP_SQUAD")
        ret = self.cursor.fetchall()
        return ret

    def select_byId(self, id):
        self.cursor.execute(f"SELECT * FROM 02_JVP_SQUAD WHERE Id = {id}")
        ret = self.cursor.fetchone()
        return ret

    def update(self, squad : Squad):
        self.cursor.execute(f"update 02_JVP_SQUAD set Nome = '{squad.nome}', Descricao = '{squad.descricao}', NumeroPessoas = '{squad.numeroPessoas}', LinguagemBack = '{squad.linguagemBack}', FrameworkFront = '{squad.frameFront}'  where Id = {squad.id}")
        self.conexao.commit()

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM 02_JVP_SQUAD WHERE Id = {id}")
        self.conexao.commit()
    
    def insert(self, squad : Squad, id_back, id_front, id_sgbd):
        self.cursor.execute(f"insert into 02_JVP_SQUAD (Nome,Descricao,NumeroPessoas,id_front,id_back,id_sgbd) values ('{squad.nome}','{squad.descricao}',{squad.numeroPessoas}, {id_back},{id_front},{id_sgbd})")
        self.conexao.commit()