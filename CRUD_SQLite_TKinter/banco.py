# importando SQLite
import sqlite3 as lite

# criando conexao com BD (se o BD não existir vai ser criado automaticamente)
con = lite.connect('dados.db')

# criando tabelas no BD
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE formulario('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'nome TEXT, '
                'email TEXT, '
                'telefone TEXT, '
                'dia_em DATE, '
                'estado TEXT, '
                'sobre TEXT)')

