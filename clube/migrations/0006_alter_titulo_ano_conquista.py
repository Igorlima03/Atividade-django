# Generated by Django 5.0.2 on 2024-03-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0005_alter_titulo_ano_conquista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='ano_conquista',
            field=models.PositiveIntegerField(default=0, verbose_name='Ano da consquista'),
        ),
    ]
