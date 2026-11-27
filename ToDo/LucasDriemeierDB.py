import mysql.connector
from mysql.connector import Error


class ConexaoMySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conexao.is_connected():
                print("Conectado ao MySQL com sucesso")
        except Error as err:
            print(f"Erro ao conectar: {err}")

    def desconectar(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão encerrada.")
a=ConexaoMySQL('localhost','root','','DALE')
ConexaoMySQL.conectar(a)
ConexaoMySQL.desconectar(a)
