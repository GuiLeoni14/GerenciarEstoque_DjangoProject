# Generated by Django 3.2.6 on 2021-08-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data',
            field=models.DateField(),
        ),
    ]