import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="senac"
    )
    if conn.is_connected():
        print("Conectado no banco.")
        conn.close()
except Exception as error:
    print("Erro:", error)
