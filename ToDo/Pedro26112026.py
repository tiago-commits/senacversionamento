class Pessoa:
    def __init__(self,nome,idade,sexo,altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
    
    def chamada(self):
        return(f"Eu me chamo {self.nome} e estou aqui.")
    
    def medida(self):
        return(f"Eu meço {self.altura:.2f}.")

    def aniversário(self):
        return(f"Estou fazendo {self.idade} hoje!")

    def qual_sexo(self):
        return(f"O meu sexo é {self.sexo}.")

obj1 = Pessoa("João",18,"masculino",1.70)
obj2 = Pessoa("Julia",30,"feminino",1.64)
obj3 = Pessoa("Marcos",25,"masculino",1.90)

def mostrar_info(obj):
    print(f"{obj.chamada()}\n{obj.medida()}\n{obj.aniversário()}\n{obj.qual_sexo()}\n")

mostrar_info(obj1)
mostrar_info(obj2)
mostrar_info(obj3)

