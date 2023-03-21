import sqlite3

conn = sqlite3.connect('cnab.db')
c = conn.cursor()

# Cria tabela de Dados
c.execute('''CREATE TABLE dados
             (tipo int, 
             data date, 
             valor varchar(50), 
             cpf varchar(11), 
             cartao varchar(12), 
             hora timestamp(6), 
             nome_dono_loja varchar(50), 
             nome_loja varchar(50))''')

# Cria tabela de Tipo de transacao
c.execute('''CREATE TABLE tipo_transacoes
          (tipo int, descricao varchar(30), natureza varchar(30))
          ''')
# insert na tabela de tipo de transação
c.execute('''INSERT INTO tipo_transacoes (tipo, descricao, natureza) values 
          ('1','Débito','Entrada'),
          ('2','Boleto','Saída'),
          ('3','Financiamento','Saída'),
          ('4','Crédito','Entrada'),
          ('5','Recebimento Empréstimo','Entrada'),
          ('6','Vendas','Entrada'),
          ('7','Recebimento TED','Entrada'),
          ('8','Recebimento DOC','Entrada'),
          ('9','Aluguel','Saída')
          ''')

# Salva a transação
conn.commit()

# Fecha a conexão
conn.close()

print("Banco de dados criado com sucesso!!!")