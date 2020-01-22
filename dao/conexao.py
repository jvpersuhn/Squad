import MySQLdb

class Conexao():
    def __init__(self):
        self.host = 'mysql.topskills.study'
        self.database = 'topskills01'
        self.user = 'topskills01'
        self.paswd = 'ts2019'

        self.conexao = MySQLdb.connect(host=self.host, database=self.database, user=self.user, passwd=self.paswd)
        self.cursor = self.conexao.cursor()