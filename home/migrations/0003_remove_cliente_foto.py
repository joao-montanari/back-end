# Generated by Django 4.1.1 on 2022-12-01 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
    ]
