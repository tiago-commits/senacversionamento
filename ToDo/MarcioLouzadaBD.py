import mysql.connector
from mysql.connector import Error

class MysqlInserter:
    def __init__(self,host,port, user, password,database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None   # atributo exclusico class MysqlInserter
        self.cursor = None # atributo exclusico class MysqlInserter

    def conectar(self):
        try:
          self.conexao = mysql.connector.connect(
              host=self.host,
              port = self.port,
              user=self.user,
              password = self.password,
              database = self.database
              )
          if self.conexao.is_connected():
                self.cursor = self.conexao.cursor()
        except Error as e:
              print(f'erro ao conectar {e}')

    def deletar(self, sql, valor):
        try:
            self.conectar()
            self.cursor.execute(sql,valor)
            self.conexao.commit()
            print(f'{self.cursor.rowcount} registros deletados')
        except Error as e:
            print(f'erro ao deletar no banco de dados {e}')
        finally:
            self.fechar()

    def inserir(self,sql,valor):
        try:
            self.conectar()
            self.cursor.execute(sql,valor)
            self.conexao.commit()
            print(f'{self.cursor.rowcount} registros inseridos')
        except Error as e:
            print(f'erro ao inserir no banco de dados {e}')
        finally:
            self.fechar()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()


########### OBJETO DE CONEXÃO  ###################

banco = MysqlInserter(
    host="localhost",
    port=3307,
    user="root",
    password="senacrs",
    database="PI_BASE"
)



        






















# def insert(nome, endereco):
#   try:
#     # Estabelece a conexão com o banco de dados
#     conexao = mysql.connector.connect(
#         host='localhost',
#         user='seu_usuario',
#         password='sua_senha',
#         database='nome_do_banco',
#     )

#     cursor = conexao.cursor()

#     # Query SQL parametrizada para evitar SQL Injection
#     sql = 'INSERT INTO clientes (nome, endereco) VALUES (%s, %s)'
#     valores = (nome, endereco)

#     # Executa a inserção
#     cursor.execute(sql, valores)

#     # Confirma a transação no banco de dados
#     conexao.commit()

#     print(f'{cursor.rowcount} registro(s) inserido(s) com sucesso!')

#   except mysql.connector.Error as erro:
#     print(f'Erro ao inserir dados: {erro}')

#   finally:
#     # Fecha o cursor e a conexão
#     if 'cursor' in locals() and cursor:
#       cursor.close()
#     if 'conexao' in locals() and conexao.is_connected():
#       conexao.close()


# insert()