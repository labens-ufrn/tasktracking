# Generated by Django 3.1.2 on 2020-11-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_usuario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='fechada_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
