'''crie uma class no phyton (pessoa) que possua os seguintes atributos:
- nome
- idade
- sexo
- altura

criar metodo para cada atributo para setar cada dado da classe
criar 3 objetos, print da tela informando as informações de cada objeto'''

class Pessoa:
    def __init__(self,nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

    def printar(self):

        print (f'nome: {self.nome}, idade: {self.idade}, sexo: {self.sexo}, altura: {self.altura}')


p1 = Pessoa('joao',60,'masc',1.76)

p2 = Pessoa('maria',57,'fem',1.57)

p3 = Pessoa('marcos',35,'masc',1.72)

p1.printar()
p2.printar()
p3.printar()