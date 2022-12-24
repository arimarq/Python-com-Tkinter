# importando SQLite
import sqlite3 as lite

# criando conexao com BD
con = lite.connect('dados.db')

# criando operacoes do CRUD (create, read, update, delete)


# inserir dados (CREATE)
def inserir_registro(dado):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO formulario (nome, email, telefone, dia_em, estado, sobre) VALUES (?, ?, ?, ?, ?, ?)'
        cur.execute(query, dado)


# lendo dados (READY)
def mostrar_registros():
    lista = []
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM formulario'
        cur.execute(query)
        registro = cur.fetchall()
        for v in registro:
            lista.append(v)
    return lista


# atualizar dados (UPDATE)
def atualizar_registro(dado):
    with con:
        cur = con.cursor()
        query = 'UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, sobre=? WHERE id=?'
        cur.execute(query, dado)


# deletar dados (DELETE)
def deletar_registro(dado):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM formulario WHERE id=?'
        cur.execute(query, dado)
