class Squad:
    def __init__(self, id, nome, descricao, numeroPessoas, linguagemBack, frameFront):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.numeroPessoas = numeroPessoas
        self.linguagemBack = linguagemBack
        self.frameFront = frameFront
    
    def __str__(self):
        return f'{self.id} {self.nome} {self.descricao} {self.numeroPessoas} {self.linguagemBack} {self.frameFront}' 