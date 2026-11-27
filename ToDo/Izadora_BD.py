import mysql.connector
from mysql.connector import Error


class ConexaoBanco:
    def __init__(self, host="127.0.0.1", port=3306, user="root", database="senac"):
        self.host = host
        self.port = port
        self.user = user
        self.database = database
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                database=self.database,
            )
            print("Conectado!")
            return True
        except Error as erro:
            print(f"Nao conectado: {erro}")
            return False

    def desconectar(self):
        if self.conexao:
            self.conexao.close()


if __name__ == "__main__":
    banco = ConexaoBanco()
    if banco.conectar():
        banco.desconectar()