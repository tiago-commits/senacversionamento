class Pessoa:
    
    def cadastrar(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Sexo: {self.sexo}")
        print(f"Altura: {self.altura:.2f} m")
        print("-" * 30)


###########  OBJETOS   #############
objeto1 = Pessoa()
objeto2 = Pessoa()
objeto3 = Pessoa()

objeto1.cadastrar("Betinho De Boa", 22, "Masculino", 1.75)
objeto2.cadastrar("Aline Meia Lua", 19, "Feminino", 1.68)
objeto3.cadastrar("Tonho Papai Noel", 55, "Masculino", 1.82)

########  PRINT   ##############
objeto1.exibir()
objeto2.exibir()
objeto3.exibir()

#######   CADASTRO IMPUT PARA BRINCAR   ############
print("CADASTRO DE NOVA PESSOA")

nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
sexo = input("Informe o sexo: ")
altura = float(input("Informe a altura: ").replace(",", "."))

objeto4 = Pessoa()
objeto4.cadastrar(nome, idade, sexo, altura)

print("\nPESSOA CADASTRADA:")
objeto4.exibir()