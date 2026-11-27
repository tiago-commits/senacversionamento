class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: str, altura: float):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


    def obter_nome(self) -> str:
        return self.nome

    def obter_idade(self) -> int:
        return self.idade

    def obter_sexo(self) -> str:
        return self.sexo

    def obter_altura(self) -> float:
        return self.altura


    def trazer_dados(self) -> str:
        return (
            f"Nome: {self.obter_nome()} | "
            f"Idade: {self.obter_idade()} anos | "
            f"Sexo: {self.obter_sexo()} | "
            f"Altura: {self.obter_altura():.2f} m"
        )



pessoa1 = Pessoa("Lucas", 24, "Masculino", 1.78)
pessoa2 = Pessoa("Marina", 19, "Feminino", 1.65)
pessoa3 = Pessoa("Rafael", 31, "Masculino", 1.82)


pessoas = [pessoa1, pessoa2, pessoa3]

for i, pessoa in enumerate(pessoas, start=1):
    print(f"--- Pessoa {i} ---")
    print(pessoa.trazer_dados())