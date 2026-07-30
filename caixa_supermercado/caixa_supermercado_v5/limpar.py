import sqlite3
con = sqlite3.connect('Dados/mercado.db')
con.execute('DELETE FROM produtos')
con.execute("DELETE FROM sqlite_sequence WHERE name='produtos'")
con.commit()
con.close()
print('Limpo!')