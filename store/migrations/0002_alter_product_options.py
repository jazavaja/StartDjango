# Generated by Django 5.1.5 on 2025-02-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'permissions': [('increase_price', 'Product can increase price')], 'verbose_name': 'Product', 'verbose_name_plural': 'products'},
        ),
    ]
