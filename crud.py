import mysql as mysql
import mysql.connector
#driver de conector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdcrud',
)


print("conexao bem sucedida")
#CRUD
#CREAD
"""
nome_produto = "Bolacha recheada"
valor = 3
comando = f'''INSERT INTO vendas (nome_produto, valor) values ("{nome_produto}", {valor});'''
cursor.execute(comando) #executa o comando
#conexao.commit() #edita o banco de dados
"""

#READ
# comando = f'SELECT * FROM bdcrud.vendas;'
# cursor = conexao.cursor()
# cursor.execute(comando) #executa o comando
# resultado = cursor.fetchall() #armazena o resultado do cursor em formato de lista dentro de lista
# #conexao.commit() #edita o banco de dados
# print(resultado[0][0])


#UPDATE
# valor = 6
# nome_produto = "toddynho"
# comando = f'UPDATE VENDAS SET valor = {valor} WHERE nome_produto = "{nome_produto}";'
# cursor = conexao.cursor()
# cursor.execute(comando) #executa o comando
# conexao.commit() #edita o banco de dados

#DELETE
nome_produto = "toddynho"
comando = f'DELETE FROM VENDAS WHERE nome_produto = "{nome_produto}";'
cursor = conexao.cursor()
cursor.execute(comando) #executa o comando
conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()