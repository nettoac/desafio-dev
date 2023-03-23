import sqlite3

def test_criar_tabela_dados():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    c.execute('''CREATE TABLE dados
                 (tipo int, 
                 data date, 
                 valor varchar(50), 
                 cpf varchar(11), 
                 cartao varchar(12), 
                 hora timestamp(6), 
                 nome_dono_loja varchar(50), 
                 nome_loja varchar(50))''')
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dados'")
    result = c.fetchone()
    assert result is not None

    conn.close()
