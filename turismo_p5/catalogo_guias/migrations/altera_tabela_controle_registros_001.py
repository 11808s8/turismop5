from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
            ('catalogo_guias','cria_tabela_controle_registros_003'),
    ]
    operations = [
        migrations.RunSQL(
            [("alter table controle_registro alter column nro_registro type varchar")])
    ]
