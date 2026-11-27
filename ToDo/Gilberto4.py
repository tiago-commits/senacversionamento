import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="senac"
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")
        conexao.close()

except mysql.connector.Error as erro:
    print(f"Erro na conexão: {erro}")
