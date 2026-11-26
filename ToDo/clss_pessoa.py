class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura


p = Pessoa("Jonathan", 25, "M", 1.75)

print("Nome:", p.get_nome())
print("Idade:", p.get_idade())
print("Sexo:", p.get_sexo())
print("Altura:", p.get_altura())

p.set_idade(26)
p.set_altura(1.80)

print("Nova idade:", p.get_idade())
print("Nova altura:", p.get_altura())