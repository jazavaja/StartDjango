# Generated by Django 5.1.5 on 2025-03-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_alter_productapi_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='productapi',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_picture/'),
        ),
    ]
