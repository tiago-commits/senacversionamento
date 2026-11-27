import mysql.connector


class Conexao:
    def conectar(self):
        return mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="senacrs",
            database="senac"
        )


conn = Conexao().conectar()
print("Conectado ao banco!")
conn.close()