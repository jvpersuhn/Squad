class FrontEnd:
    def __init__(self, id, Nome, Descricao, Versao):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.Versao = Versao

    def __str__(self):
        return  f"{self.id},{self.Nome},{self.Descricao},{self.Versao}"