class pessoa:
    def __init__(self,nome,idade,sexo,altura):
        self.nome=nome
        self.idade=idade
        self.sexo=sexo
        self.altura=altura
    def describe(self):
        print(f"Nome:{self.nome}\nIdade:{self.idade}\nSexo:{self.sexo}\nAltura:{self.altura}")
obj01=pessoa("Brás",60,"masculino",1.79)
obj02=pessoa("Rubião",38,"masculino",1.86)
obj03=pessoa("Bento",34,"masculino",1.83)
obj03.describe()