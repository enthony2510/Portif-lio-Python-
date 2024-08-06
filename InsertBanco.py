import sqlite3

# Conectando ao banco de dados (ou criando, se não existir)
conn = sqlite3.connect('fila.db')
cursor = conn.cursor()

# Criando a tabela para a fila
cursor.execute('''
CREATE TABLE IF NOT EXISTS fila (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor TEXT NOT NULL
)
''')

# Confirmando as mudanças
conn.commit()

def inserir_na_fila(valor):
    cursor.execute('INSERT INTO fila (valor) VALUES (?)', (valor,))
    conn.commit()

def reverter_fila():
    cursor.execute('SELECT id, valor FROM fila ORDER BY id DESC')
    elementos = cursor.fetchall()
    
    # Limpando a tabela
    cursor.execute('DELETE FROM fila')
    conn.commit()
    
    # Reinserindo os elementos em ordem reversa
    for id, valor in elementos:
        cursor.execute('INSERT INTO fila (valor) VALUES (?)', (valor,))
    conn.commit()

def verificar_fila():
    cursor.execute('SELECT valor FROM fila ORDER BY id')
    elementos = cursor.fetchall()
    for elemento in elementos:
        print(elemento[0])

# Inserindo alguns valores na fila
inserir_na_fila('Primeiro')
inserir_na_fila('Segundo')
inserir_na_fila('Terceiro')

# Verificando a fila
print("Fila original:")
verificar_fila()

# Revertendo a fila
reverter_fila()

# Verificando a fila após reversão
print("Fila revertida:")
verificar_fila()

# Fechando a conexão
conn.close()



