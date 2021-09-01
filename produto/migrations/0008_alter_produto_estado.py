# Generated by Django 3.2.6 on 2021-08-31 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_produto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estado',
            field=models.CharField(choices=[('Disponível', 'Disponível'), ('Vendido', 'Vendido')], max_length=12),
        ),
    ]
