import copy

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def __str__(self):
        return f'nome: {self.nome}, Idade: {self.idade}'
        

    def clone(self):
        return copy.copy(self)



class PessoaManager:
    def __init__(self):
        self.pessoas = {}

    def add_pessoas(self, nome, idade, id):
        pessoa = Pessoa(nome, idade)
        self.pessoas[id] = pessoa
        


    def get_pessoas(self, id):
        return self.pessoas[id].clone()
    
#criar pessoas
manager = PessoaManager()

manager.add_pessoas("Joao", 30 , 1)
manager.add_pessoas("Maria", 12 , 2)
manager.add_pessoas("Pedro", 25 , 3)
manager.add_pessoas("carlos", 32 , 4)

#Clonar pessoa
pessoa1 = manager.get_pessoas(1)


#modificação
pessoa1.idade = 18
pessoa1.nome = 'tiao'


#para imprimir
print(manager.get_pessoas(1))
print(manager.get_pessoas(2))
print(manager.get_pessoas(3))
print(manager.get_pessoas(4))
print(pessoa1)
