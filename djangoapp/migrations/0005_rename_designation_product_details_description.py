# Generated by Django 4.2.4 on 2023-08-22 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_product_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_details',
            old_name='designation',
            new_name='description',
        ),
    ]
