# Generated by Django 5.1.5 on 2025-03-06 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_authorapi_bookapi'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookapi',
            table='books_api',
        ),
    ]
