# Generated by Django 3.2.6 on 2021-08-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('cartucho', 'cartucho'), ('impressora', 'impressora')], max_length=100),
        ),
    ]