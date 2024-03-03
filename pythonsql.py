import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Arlesson-PC\sqlexpress;"
    "Database=bdpythonsql;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id = 3
cliente = "Carlos Alexandre"
produto = "Curso"
data = "02/03/2024"
preco = 500
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()