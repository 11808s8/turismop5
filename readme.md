# Projeto Turismo P5

Versão do Python utilizada: 3.6.6 (3+)
<br>Banco de dados utilizado: Postgresql 10
<br>Extensão do postgresql necessária (suas dependências também. Na hora de rodar a migração ele acusa quais são necessárias): Postgis2.4

Com seu virtualenv ativo, execute, dentro dele:
pip3 install -r requirements.txt 

É necessário ter o db pertinente ao projeto já criado (info sobre o nome dentro do settings.py)

Disso, você pode clonar o projeto para seu virtualenv, mantendo o nome turismop5

Entre na pasta do projeto e execute pra rodar as migrações do banco:<br>
python3 manage.py migrate<br>
<br>
OBS: se reclamar que não encontrou o postgis.control, rodar primeiro sudo apt-get install postgis postgresql-9.6-postgis-scripts

!!Importante!!<br>
Para inserir os dados de registros do CADASTUR, é necessário<br>
executar o script na pasta crontab APÓS a execução das migrações:<br>
$ python3 insercao_registros_novos.py<br>

Para rodar o servidor local:

python3 manage.py runserver
