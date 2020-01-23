import MySQLdb
from model.frontend import FrontEnd
from dao.conexao import Conexao

class FrontDb(Conexao):
    def select_all(self):
        comand = 'SELECT * FROM 02_JM_FrontEnd;'
        self.cursor.execute(comand)
        ret = self.cursor.fetchall()
        return ret

    def select_by_id(self,id):
        comand = f"SELECT * FROM 02_JM_FrontEnd WHERE ID={id}"
        self.cursor.execute(comand)
        ret = self.cursor.fetchone()
        return ret
        
    def update(self, front : FrontEnd):
        comand = f"UPDATE 02_JM_FrontEnd  SET Nome = '{front.Nome}', Descricao = '{front.Descricao}', Versao = '{front.Versao}' WHERE ID = {front.id}"
        self.cursor.execute(comand)
        self.conexao.commit()

    def insert(self, front: FrontEnd):
        comand = f"""INSERT INTO 02_JM_FrontEnd
        ( 
            Nome
           ,Descricao
           ,Versao
        )
        VALUES(
            '{front.Nome}'
            ,'{front.Descricao}'
            ,'{front.Versao}'
        )"""
        self.cursor.execute(comand)
        self.conexao.commit()
    
    def delete(self,id):
        comand = f"DELETE FROM 02_JM_FrontEnd WHERE ID={id};"
        self.cursor.execute(comand)
        self.conexao.commit()

        
