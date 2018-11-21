import  pandas as pd
import datetime as dt
import requests
import psycopg2


tabela = 'controle_ultima_verificacao_registro'
#aqui checa no banco o último verificado

# Linha de conexão com o banco
conn_string = "host='localhost' dbname='turismop5' user='postgres' password='postgres'"
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM controle_ultima_verificacao_registro")

count = cursor.fetchall()
count = count[0][0]
ano = dt.datetime.now().year
trimestre = int(dt.datetime.now().month/3) # já arredonda o mês


# caso não tenha sequer 1 registro (usualmente ocorre na implantação dos migrates)
if(count==0):
	insert = "insert into {0} (ano, trimestre) values ({1}, {2})".format(tabela,ano,trimestre)
	cursor.execute(insert)
	conn.commit() # persiste a inserção
else:
	select ="SELECT ano,trimestre FROM {0} where ano = {1} and trimestre = {2};".format(tabela,ano,trimestre)
	
	cursor.execute(select)
	resultado = cursor.fetchall()

	# Atualiza o registro caso não seja o último
	if(len(resultado)==0):
		update = "update {0} set ano = {1}, trimestre = {2} where id = 1;".format(tabela,ano,trimestre)
		cursor.execute(insert)
		conn.commit() # persiste a atualização
	select = "select count(*) FROM controle_registro;"
	cursor.execute(select)
	total = cursor.fetchall()
	print(total[0][0])
	if(total[0][0]==0):
		trimestre = "0{}".format(trimestre)

		url = 'http://www.turismo.gov.br/dadosabertos/cadasturpf/{0}{1}TrimestrePF.csv'.format(ano,trimestre)

		codigo_retorno = requests.head(url).status_code

		if(codigo_retorno == 200):
			c = pd.read_csv(url, sep=';', encoding='latin-1')
			i =0
			for linha in c['Número do Certificado']:
				linha = linha.replace('.','')
				linha = linha.replace('-','')
				insert = "Insert into controle_registro (nro_registro) values ({0});".format(linha)
				cursor.execute(insert)
				conn.commit() # persiste a inserção
			print("Csv lido com sucesso!")
		else:
			print("Não foi possível ler o csv!")
	else:
		print("Base de dados já atualizada!")

conn.close()
