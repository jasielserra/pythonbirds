class Pessoa:
    def __init__(self, *filhos,nome=None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    sofia = Pessoa(nome='Sofia', idade=0.8)
    lis = Pessoa(nome='Liz', idade=0.8)
    sara = Pessoa(sofia,lis,nome='Sara')
    print(Pessoa.cumprimentar(sara))
    print(id(sara))
    print(sara.cumprimentar())
    print(sara.idade)
    for filhos in sara.filhos:
        print(filhos.nome, filhos.idade)
    print(sara.nome)
    print(sara.idade)