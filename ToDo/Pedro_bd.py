import mysql.connector
from mysql.connector import Error 

class Conexao:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conexao = None

    def conectar(self):
        try:

            self.conexao = mysql.connector.connect(
                host = self.host, 
                database = self.database, 
                user = self.user,
                password = self.password
            )

            if self.conexao.is_connected(): 
                print('Conectou com sucesso ao banco de dados!')

        except Error as e:
            print(f'Falhou ao conectar no banco mysql:{e}')

    def fechar(self):
        if self.conexao.is_connected():
            self.conexao.close()
            print('Conexao encerrada com sucesso.')

obj1 = Conexao("localhost",3306,"senac","root","")

obj1.conectar()

obj1.fechar()