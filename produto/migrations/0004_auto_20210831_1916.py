# Generated by Django 3.2.6 on 2021-08-31 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('', 'Selecione:'), ('CO', 'Cosmético'), ('IN', 'Industrial'), ('ALM', 'Alimentício')], max_length=100),
        ),
    ]