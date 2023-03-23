from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
import sqlite3
from utils.converter_hora import ConverterHoras as ch
from utils.converter_moeda import Moeda as mod
from utils.formatar_cpf import FormatarCPF as fcpf
from utils.formatar_data import FormatarData as fdt

app = FastAPI()

# Conecta ao banco de dados
conn = sqlite3.connect('cnab.db', check_same_thread=False)
c = conn.cursor()


@app.get("/")
async def read_root():
    with open('index.html', 'r') as f:
        content = f.read()
    return HTMLResponse(content=content)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if file.filename.endswith(".txt"):
        contents = await file.read()
        lines = contents.decode().split('\n')

        for line in lines:
            # Separa os campos do arquivo texto
            tipo = line[0:1]
            data = line[1:9]
            valor = line[9:19]
            cpf = line[19:30]
            cartao = line[30:42]
            hora = line[42:48]
            nome_dono_loja = line[48:62]
            nome_loja = line[62:81]

            # formatando as horas para o UTC -03:00
            n_hora = ch.horas(hora)

            # formatando as valor para Moeda dividido por 100 conforme requesito
            n_valor = mod.converterparamoeda(valor)

            # Insere no banco de dados
            c.execute("INSERT INTO dados VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                      (tipo, data, n_valor, cpf, cartao, str(n_hora),
                       nome_dono_loja, nome_loja))
        # Salva a transação
        conn.commit()
        # return {"file_size": len(contents)}
        return RedirectResponse(url=f"/visualizar-dados", status_code=303)
    return {"error": "Arquivo inválido!"}


@app.get("/visualizar-dados")
async def read_data():
    # Executa a consulta SQL
    c.execute('''SELECT t.descricao as tipo, 
             d.data as data, 
             d.valor as valor, 
             d.cpf as cpf, 
             d.cartao as cartao, 
             d.hora as hora, 
             d.nome_dono_loja as nome_dono_loja, 
             d.nome_loja as nome_loja
             FROM dados d inner join tipo_transacoes t
             on (d.tipo = t.tipo)
             order by nome_dono_loja
             ''')
    data = c.fetchall()

    # Gera o conteúdo HTML
    content = '''
    <!DOCTYPE html>
<html>
<head>
	<title>CNAB's Recebidos</title>
	<style>
		.center {
			margin: auto;
			border-collapse: separate;
			border-spacing: 2px;
		}
		th {
			background-color: #ddd;
            border: 1px solid black;
		}
        td{
			border: 1px solid black;
		}
	</style>
</head>
<body>
	<table class="center">
		<thead>
			<tr>
				<th>Tipo</th>
				<th>Data</th>
				<th>Valor R$</th>
				<th>CPF</th>
				<th>Cartão</th>
				<th>Hora</th>
				<th>Nome do Dono da Loja</th>
				<th>Nome da Loja</th>
			</tr>
		</thead>

    '''
    # content += "<tr><th>Tipo</th><th>Data</th><th>Valor</th><th>CPF</th><th>Cartão</th><th>Hora</th><th>Nome do Dono da Loja</th><th>Nome da Loja</th></tr>"
    vlr_total = 0.00
    cont = 0
    for row in data:
        content += f'''<tr><td>{row[0]}</td><td>{fdt.data_cnab(row[1])}</td><td style="text-align:right;">{str("{:0,.2f}".format(float(row[2])))}</td><td>{fcpf.formata_cpf(row[3])}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td></tr>'''
        cont = cont + 1
        vlr_total = vlr_total + float(row[2])
    
    content += f'''<tr>
                    <th colspan="3" style="font-size: 20px; text-align: center;">Qtd</th>
                    <th colspan="5" style="font-size: 20px; text-align: center;">Total CNAB</th>
                   </tr>
                   <tr>
                    <td colspan="3" style="font-size: 20px; text-align: center;">{cont}</td>
                    <td colspan="5" style="font-size: 20px; text-align: center;">{str("{:0,.2f}".format(float(vlr_total)))} R$</td>
                   </tr>'''
    content += '''	</table>   
                </body>
               </html>
               '''

    return HTMLResponse(content=content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)