from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
            ('catalogo_guias','0001_initial'),
    ]
    operations = [
        migrations.RunSQL(
            [("Create table controle_registro (id SERIAL PRIMARY KEY,nro_registro int);")])
    ]
