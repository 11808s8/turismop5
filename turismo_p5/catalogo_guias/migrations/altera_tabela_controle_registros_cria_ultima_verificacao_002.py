from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
            ('catalogo_guias','cria_tabela_controle_registros_instancia_postgis_004'),
    ]
    operations = [
        migrations.RunSQL(
            # [("alter table controle_registro alter column nro_registro type varchar")],
            [("Create table controle_ultima_verificacao_registro (id SERIAL PRIMARY KEY,ano int, trimestre int);")])
    ]
