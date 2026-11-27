class pessoa:
    def __init__(self,nome,idade,sexo,altura):
        self.nome=nome
        self.idade=idade
        self.sexo=sexo
        self.altura=altura
    def describe(self):
        print(f"Nome:{self.nome}\nIdade:{self.idade}\nSexo:{self.sexo}\nAltura:{self.altura}")
    def nome(self):
        print(f"{self.nome}")
    
    def altura(self):
        print(f"{self.altura}")

    def idade(self):
        print(f"{self.idade}")

    def sexo(self):
        print(f"{self.sexo}")

obj01=pessoa("Brás",60,"masculino",1.79)
obj02=pessoa("Rubião",38,"masculino",1.86)
obj03=pessoa("Bento",34,"masculino",1.83)
obj03.describe()
print('\n')
pessoa.nome(obj01)
pessoa.altura(obj01)
pessoa.idade(obj01)
pessoa.sexo(obj01)
