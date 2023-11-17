# Generated by Django 4.2.4 on 2023-08-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pro_company_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('expdate', models.DateField()),
                ('designation', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
