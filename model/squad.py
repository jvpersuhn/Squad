class Squad:
    def __init__(self, id, nome, descricao, numeroPessoas):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.numeroPessoas = numeroPessoas
        self.__linguagemBack = 'Null'
        self.__linguagemFront = 'Null'
        self.__sgbd = 'Null'
    
    def __str__(self):
        return f'{self.id} {self.nome} {self.descricao} {self.numeroPessoas} {self.linguagemBack} {self.linguagemFront} {self.sgbd}' 
    
    @property
    def linguagemBack(self):
        return self.__linguagemBack

    @linguagemBack.setter
    def linguagemBack(self, l):
        self.__linguagemBack = l

    @property
    def linguagemFront(self):
        return self.__linguagemFront

    @linguagemFront.setter
    def linguagemFront(self, l):
        self.__linguagemFront = l

    @property
    def sgbd(self):
        return self.__sgbd

    @sgbd.setter
    def sgbd(self, l):
        self.__sgbd = l