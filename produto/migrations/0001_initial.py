# Generated by Django 3.2.6 on 2021-08-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('fornecedor', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField(max_length=100)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
