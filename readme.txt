Versão do Python utilizada: 3.6.6 (sendo 3+ já está de bom tamanho)
Banco de dados utilizado: Postgresql 10
Extensão do postgresql necessária (suas dependências também. Na hora de rodar a migração ele acusa quais são necessárias): Postgis2.4

Com seu virtualenv ativo, execute, dentro dele:
pip3 install -r requirements.txt 

Disso, você pode copiar o projeto para seu virtualenv, mantendo o nome turismop5

Entre na pasta do projeto e execute:
python3 manage.py migrate

pra rodar as migrações.

!!Importante!!
Para inserir os dados de registros do CADASTUR, é necessário
executar o script na pasta crontab:
$ python3 insercao_registros_novos.py

Para rodar o servidor local:

python3 manage.py runserver
