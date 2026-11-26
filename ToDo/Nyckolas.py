class pessoa:
    def __init__(self,nome,idade,sexo,altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

    def imprimir(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Sexo:", self.sexo)
        print("Altura:", self.altura)


p1 = pessoa("Matheus", 18, "M", 1.75)
p2 = pessoa("Maria", 16, "F", 1.60)
p3 = pessoa("Victor", 16, "M", 1.70)

p1.imprimir()
p2.imprimir()
p3.imprimir()

