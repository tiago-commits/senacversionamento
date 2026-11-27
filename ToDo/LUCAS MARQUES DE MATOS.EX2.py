import mysql.connector
from mysql.connector import Error

class Conexao:
    def __init__(self, host, port, database, user, password): # classe mãe onde tem propriedades e metodos (apos o self)
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.conexao = None # Propriedade unica e exclusiva da classe

    def conectar(self):
        try:
            # só vai executar o try se o bloco der sucesso
            self.conexao = mysql.connector.connect(
                host = self.host, # host vai receber o valor de host da classe mãe
                database = self.database, # db vai receber o valor de db da classe mãe
                port = self.port, # port vai receber o valor de port da classe mãe
                user = self.user, # user vai receber o valor de user da classe mãe
                password = self.password # password vai receber o valor de password da classe mãe                
            )

            if self.conexao.is_connected(): # se isto der sucesso
                print('Conectou com sucesso ao banco de dados!')

        except Error as e:
            # se o bloco do try falhar, vai executar o except
            print(f'Falhou ao conectar no banco mysql:{e}')

obj = Conexao(host="localhost", port=3306, database="senac", user="root", password="") # instancia um objeto de Conexão

obj.conectar()