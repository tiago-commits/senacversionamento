class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__sexo = ""
        self.__altura = 0.0

    # Métodos GET
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_sexo(self):
        return self.__sexo

    def get_altura(self):
        return self.__altura

    # Métodos SET
    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_altura(self, altura):
        self.__altura = altura


# Primeiro objeto
pessoa1 = Pessoa()
pessoa1.set_nome("Carlos")
pessoa1.set_idade(25)
pessoa1.set_sexo("Masculino")
pessoa1.set_altura(1.80)

# Segundo objeto
pessoa2 = Pessoa()
pessoa2.set_nome("Ana")
pessoa2.set_idade(30)
pessoa2.set_sexo("Feminino")
pessoa2.set_altura(1.65)

# Terceiro objeto
pessoa3 = Pessoa()
pessoa3.set_nome("Pedro")
pessoa3.set_idade(22)
pessoa3.set_sexo("Masculino")
pessoa3.set_altura(1.75)

# Exibindo os três objetos na tela
for pessoa in [pessoa1, pessoa2, pessoa3]:
    print("-------------------------")
    print("Nome:", pessoa.get_nome())
    print("Idade:", pessoa.get_idade())
    print("Sexo:", pessoa.get_sexo())
    print("Altura:", pessoa.get_altura())