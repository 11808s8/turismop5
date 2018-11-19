Versão do Python utilizada: 3.6.6 (sendo 3+ já está de bom tamanho)
Banco de dados utilizado: Postgresql 10
Extensão do postgresql necessária (suas dependências também. Na hora de rodar a migração ele acusa quais são necessárias): 
Postgis2.4

Com seu virtualenv ativo, execute, dentro dele:
pip3 install -r requirements.txt 

É necessário ter o db pertinente ao projeto já criado (info sobre o nome dentro do settings.py)

Disso, você pode clonar o projeto para seu virtualenv, mantendo o nome turismop5

Entre na pasta do projeto e execute:
python3 manage.py migrate

pra rodar as migrações.

!!Importante!!
Para inserir os dados de registros do CADASTUR, é necessário
executar o script na pasta crontab APÓS a execução das migrações:
$ python3 insercao_registros_novos.py

Para rodar o servidor local:

python3 manage.py runserver

////////////////////////////////////////////////////////////////////////

Beleza tu quer fazer no windows prepare-se para se estressar

Versão do Python utilizada: 3.6.6 (sendo 3+ já está de bom tamanho)
Banco de dados utilizado: Postgresql 10

-	clona o projeto

-	cria um virtualenv

- 	ativa o cretino
		myvenv\Scripts\activate

- instala o pip
		python3 -m pip install --upgrade pip

- reza um terço. e roda isso
	pip install -r requirements.txt
	não funiconou tenta isso
	- python -m pip install -r requirements.txt

continua dano pau vamos a lista de coisa que se deve fazer/revisar

1-vericar se tem instalados os ddl do visual studio C++ 14.0
	(se não tem instala o visual studio e mais simples do que instalar os as ddl separdas)
2-verifica se algumas versão da lib dentro dos requerimentos está encarnado com tuas configuraçoes
	se encomodar tira a version ex  lib==version -> lib


Se deus quiser tu passa dos requirimentos em 1 dia

- roda o migrate 	(com postgree ja instalado e base criada) 
	 python manage.py migrate
- deu pau instala o postgre conforme este link
	https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install/#windows

não funcionou, fudeu a barca baixa o ubuntu e faz dual boot

- seguindo isso roda para pegar os dados da cadastrur
	python3 insercao_registros_novos.py
 