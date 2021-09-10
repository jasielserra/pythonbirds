class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

class Humano(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3



if __name__ == '__main__':
    sofia = Humano(nome='Sofia', idade='8 meses')
    lis = Pessoa(nome='Liz', idade='8 meses')
    paulo = Mutante(nome='Paulo')
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
    sara.olhos = 1
    del sara.olhos
    print(sofia.__dict__)
    print(sara.__dict__)
    Pessoa.olhos = 2
    print(Pessoa.olhos)
    print(sara.olhos)
    print(lis.olhos)
    print(id(Pessoa.olhos), id(sara.olhos), id(lis.olhos))
    print(isinstance(sofia,Humano))
    print(sara.cumprimentar())
    print(sofia.cumprimentar())