# Sistema de Parse em Python com FastAPI

Este sistema em Python utiliza o framework FastAPI para criar uma API de parse de arquivos CNAB (Centro Nacional de Automação Bancária). O script consiste em um servidor que recebe arquivos de texto em formato CNAB, lê cada linha do arquivo e armazena as informações em um banco de dados SQLite (Banco mais versátil e de fácil utilização para o modelo).

## Instalação

No seu ambiente linux já configurado e atualizado, vamos instalar o python da seguinte forma.
Apt-get
Para instalar o Python 3 e o gerenciador de pacotes pip (Opcional), digite em um terminal, digite em um terminal:
```bash
$ sudo apt-get install python3 python3-pip
```

## Instalação e Uso

Para utilizar este sistema, é necessário ter o Python e as bibliotecas FastAPI, SQlite3 e uvicorn instaladas, você pode instala-las de duas maneiras:
### Por fora do projeto
```bash
pip install fastapi
```
```bash
pip install uvicorn
```
```bash
pip install pysqlite
```
### Por dentro do projeto, 
acessando diretamente a pasta do projeto você irá localizar o arquivo requeriments.txt e rodar no terminal o seguinte comando:
```bash
pip install -r requirements.txt
```

Pronto, está tudo pronto para iniciar o sistema!

## Funcionamento
Separei o projeto em duas partes para simplificar o entendimento:
primeiramente iremos rodar o script de criação do banco de dados que será rodado uma única vez, dados pelo comando que você irá rodar dentro da pasta do projeto:
```bash
python database.py
```
ao finalizar irá aparecer a mensagem *Banco de dados criado com sucesso!!!*

ainda na mesma pasta vamos rodar o comando para iniciar o servidor uvicorn com fastapi, rode o comando abaixo:
```bash
python main.py
```
Esse comando iniciará o serviço na porta especificada dentro do projeto, podendo ser mudada para não impactar outros serviços e exibirá uma mensagem de exemplo abaixo:
```bash
INFO:     Started server process [24156]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Agora basta ir para qualquer browser de preferencia e acessar a página principal em 
```bash
http://localhost:8000/ 
```
para fazer o upload do arquivo CNAB. Após o tratamento e inserção dos dados que foram armazenados, você será encaminhado automativamente para a página de visualização que podem ser visualizados em 
```bash
http://localhost:8000/visualizar-dados
```

Internamente ainda foi melhorado os scripts utilizam as classes ConverterHoras, Moeda, FormatarCPF e FormatarData, presentes nos módulos utils.converter_hora, utils.converter_moeda, utils.formatar_cpf e utils.formatar_data, respectivamente, para formatar os dados antes de inseri-los no banco de dados.

## As rotas disponíveis são:
- / -> página inicial com formulário para upload do arquivo CNAB.

- /uploadfile -> rota para upload do arquivo CNAB. Aceita apenas arquivos com extensão .txt.

- /visualizar-dados -> página que exibe os dados armazenados no banco de dados.

## Banco de Dados
O sistema utiliza um banco de dados SQLite para armazenar os dados do arquivo CNAB. O arquivo de banco de dados é criado automaticamente quando o script é executado e as informações são armazenadas na tabela dados. A tabela tipo_transacoes é utilizada para fazer o mapeamento entre o tipo de transação no arquivo CNAB e sua descrição correspondente.

## Documentação da API

Para acessar as rotas e a documentação da API é só acessar a pagina: http://localhost:8000/docs

## Testes Unitários

Para executar esses testes a partir do terminal, execute abaixo para executar os testes:
```bash
pytest <nome_do_arquivo_de_teste>
```
todos os testes estão dentro da pasta tests do repositório, execute os demais testes conforme necessidade, segue:
```bash
test_banco.py
```
```bash
test_criar_arquivo.py
```
```bash
test_ler_dados.py
```
```bash
test_ler_raiz.py
```