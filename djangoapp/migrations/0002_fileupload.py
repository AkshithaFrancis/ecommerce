# Generated by Django 4.2.4 on 2023-08-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('fileimg', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
