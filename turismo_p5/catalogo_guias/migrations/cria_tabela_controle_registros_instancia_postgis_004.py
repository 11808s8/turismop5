from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
            ('catalogo_guias','0001_initial'),
    ]
    operations = [
        CreateExtension('postgis'),
        migrations.RunSQL(
            [("Create table controle_registro (nro_registro bigint PRIMARY KEY);")],
            ),
        migrations.RunSQL(
            "ALTER TABLE public.catalogo_guias_pessoa_juridica ADD CONSTRAINT catalogo_guias_pessoa_juridica_numero_registro_fk_id foreign key (numero_registro) references public.controle_registro(nro_registro) ON DELETE CASCADE",
            reverse_sql="ALTER TABLE public.catalogo_guias_pessoa_juridica DROP CONSTRAINT catalogo_guias_pessoa_juridica_numero_registro_fk_id"
        )
    ]
