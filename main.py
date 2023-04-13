import psycopg2

"Criando conecção com o Bd "
conect = psycopg2.connect(
    host="localhost",
    database="eusouanderson",
    user="eusouanderson",
    password="123",
)

"Criando uma tabela de usuários:"
table = str(input('Digite o nome da tabela: '))

cursor = conect.cursor()
cursor.execute(f'''
        CREATE TABLE {table} (id SERIAL PRIMARY KEY,
        nome VARCHAR(50), idade INTEGER 
    )
''')
conect.commit()

"Inserindo alguns registros na tabela de usuários:"

cursor.execute('''
        INSERT INTO usuarios(nome, idade)
        VALUES('João', 25),
               ('Maria', 30),
               ('Pedro', 40) 
''')
conect.commit()

"Recuperando os registros da tabela de usuários:"

cursor.execute("SELECT * FROM usuarios ")
registros = cursor.fetchall()


for registro in registros:
    print(registro)

"Fechando a conexão com o banco de dados:"

cursor.execute("DROP TABLE usuarios")
conect.commit()

cursor.close()
conect.close()