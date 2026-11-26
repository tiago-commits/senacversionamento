lista_pessoa = []

class Pessoa:
    def __init__(self, nome=None, idade=None, sexo=None, altura=None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

    def input(self):
        self.nome = input("informe o nome: ")
        self.idade = int(input("informe a idade: "))
        self.sexo = input("informe o sexo: ")
        self.altura = int(input("informe a altura: "))
        lista_pessoa.append(self)

pessoa1 = Pessoa()
pessoa1.input()
print(f"Dados cadastrados:\n{lista_pessoa[0].nome}\n{lista_pessoa[0].idade} anos\n{lista_pessoa[0].sexo}\n{lista_pessoa[0].altura}cm")