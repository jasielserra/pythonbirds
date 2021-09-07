class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    sofia = Pessoa(nome='Sofia', idade='8 meses')
    lis = Pessoa(nome='Liz', idade='8 meses')
    sara = Pessoa(sofia, lis, nome='Sara')
    print(Pessoa.cumprimentar(sara))
    print(id(sara))
    print(sara.cumprimentar())
    print(sara.idade)
    print(sara.nome)
    for filhos in sara.filhos:
        print(filhos.nome, filhos.idade)
    sara.sobrenome = 'Serra'
    print(sara.__dict__)
    del sara.filhos
    print(sara.__dict__)