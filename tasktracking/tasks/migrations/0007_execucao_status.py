# Generated by Django 3.1.2 on 2020-11-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20201126_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='execucao',
            name='status',
            field=models.CharField(choices=[('1', 'Parada'), ('2', 'Executando'), ('3', 'Pausada')], max_length=1, null=True),
        ),
    ]
