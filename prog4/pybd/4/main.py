'''
    Integrantes do grupo: Guilherme Cordeiro Costa, Fillipy Costa e Pablo Nistal.
    Grupo: Soul Society
'''


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="serra12345678",
  database="publicacao"
)

mycursor = mydb.cursor()

sql = "UPDATE titulos SET TITULO_LIVRO = 'titulo atualizado', DATA_PUBLICACAO = '2025-11-17' WHERE ID_TITULO = 1032"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")