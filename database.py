import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='112233',
    database='db',
)
# iniciando conexao
cursor = connection.cursor()
# # fechar conexao
# cursor.close()
# connection.close()
