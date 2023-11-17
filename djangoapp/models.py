from django.db import models

# Create your models here.
class register(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    dob=models.DateField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class fileupload(models.Model):
    item_name=models.CharField(max_length=30)
    fileimg=models.FileField(upload_to='djangoapp/static')
    description=models.CharField(max_length=100)

class employee(models.Model):
    ename=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    designation=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
class product_details(models.Model):
    pname=models.CharField(max_length=30)
    pro_company_name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    expdate=models.DateField()
    description=models.CharField(max_length=50)
    price=models.IntegerField()

class upload(models.Model):
    audio_name=models.CharField(max_length=50)
    audio=models.FileField(upload_to='djangoapp/static')
    video_name=models.CharField(max_length=50)
    video=models.FileField(upload_to='djangoapp/static')
    pdf_name=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='djangoapp/static')

class select(models.Model):
    choice=[
        ('Kerala','Kerala'),
        ('Delhi','Delhi'),
        ('Karnataka','Karnataka')
    ]
    full_name=models.CharField(max_length=30)
    state=models.CharField(max_length=30,choices=choice)
    english=models.BooleanField(default=False)
    malayalam=models.BooleanField(default=False)
    hindi=models.BooleanField(default=False)