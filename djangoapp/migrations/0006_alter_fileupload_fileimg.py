# Generated by Django 4.2.4 on 2023-08-23 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_rename_designation_product_details_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='fileimg',
            field=models.FileField(upload_to='djangoapp/static'),
        ),
    ]
