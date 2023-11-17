from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login
# Create your views here.
import json


def first(request):
    return HttpResponse("My first django page")
def second(request):
    return HttpResponse("My second django page")
def third(request):
    return render(request,"third.html")
def fourth(request):
    return render(request,"fourth.html")
def reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            a=register(fname=fname,lname=lname,dob=dob,gender=gender,phone=phone,email=email,address=address,username=username,password=password)
            a.save()
            return HttpResponse("Registration success")
        else:
            return HttpResponse("Password is Incorrect")
    return render(request,"registration.html")
# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         a=register.objects.all()
#         for i in a:
#             if(i.email==email and i.password==password):
#                 return HttpResponse("Login Successfully")
#         else:
#             return HttpResponse("Login Failed")
#
#     return render(request,"login.html")
def index(request):
    return render(request,"index.html")
def fileup(request):
    if request.method=='POST':
        filename=request.POST.get('item_name')
        fileimg=request.FILES.get('fileimg')
        description=request.POST.get('description')
        b=fileupload(item_name=filename,fileimg=fileimg,description=description)
        b.save()
        return HttpResponse("File Upload Successfully")
    return render(request,"fileupload.html")

def filedisplay(request):
    id=[]
    item_name=[]
    fileimg=[]
    description=[]
    a=fileupload.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        name=i.item_name
        item_name.append(name)
        img=str(i.fileimg).split('/')[-1]
        fileimg.append(img)
        des=i.description
        description.append(des)
    mylist=zip(id,item_name,fileimg,description)
    return render(request,'filedisplay.html',{'data':mylist})

def emp(request):
    if request.method=='POST':
        ename=request.POST.get('ename')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        designation=request.POST.get('designation')
        company_name=request.POST.get('company_name')
        b=employee(ename=ename,phone=phone,email=email,designation=designation,company_name=company_name)
        b.save()
        return HttpResponse("Employee Added Successfully")
    return render(request,"employee_register.html")

def display(request):
    a=register.objects.all()
    return render(request,'display.html',{'data':a})

def empdisplay(request):
    a=employee.objects.all()
    return render(request,'empdisplay.html',{'data':a})
def empsearch(request):
    if request.method=='POST':
        ename=request.POST.get('ename')
        phone=request.POST.get('phone')
        b=employee.objects.all()
        for i in b:
            if (i.ename==ename and int(i.phone)==int(phone)):
                return HttpResponse("Employee Found...")
        else:
            return HttpResponse("Employee Not Found!")
    return render(request,"employee_search.html")

def product(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        pro_company_name=request.POST.get('pro_company_name')
        quantity=request.POST.get('quantity')
        expdate=request.POST.get('expdate')
        description=request.POST.get('description')
        price=request.POST.get('price')
        c=product_details(pname=pname,pro_company_name=pro_company_name,quantity=quantity,expdate=expdate,description=description,price=price)
        c.save()
        return HttpResponse("Product Added Successfully...")

    return render(request,"product_details.html")
def product_search(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        pro_company_name=request.POST.get('pro_company_name')
        c=product_details.objects.all()
        for i in c:
            if (i.pname==pname and i.pro_company_name==pro_company_name):
                return HttpResponse("Product Found...")
        else:
            return HttpResponse("Product Not Found!")
    return render(request,"search_product.html")

def upload_file(request):
    if request.method=='POST':
        audio_name=request.POST.get('audio_name')
        audio=request.FILES.get('audio')
        video_name = request.POST.get('video_name')
        video = request.FILES.get('video')
        pdf_name=request.POST.get('pdf_name')
        pdf=request.FILES.get('pdf')
        f=upload(audio_name=audio_name,audio=audio,video_name=video_name,video=video,pdf_name=pdf_name,pdf=pdf)
        f.save()
        return HttpResponse('Files Upload Successfully...')

    return render(request,"files_upload.html")

def uploaddisplay(request):
    id=[]
    audio_name=[]
    audio=[]
    video_name=[]
    video=[]
    pdf_name=[]
    pdf=[]
    a=upload.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        aud=i.audio_name
        audio_name.append(aud)
        audi=str(i.audio).split('/')[-1]
        audio.append(audi)
        vid=i.video_name
        video_name.append(vid)
        vide=str(i.video).split('/')[-1]
        video.append(vide)
        pd=i.pdf_name
        pdf_name.append(pd)
        pd2=str(i.pdf).split('/')[-1]
        pdf.append(pd2)
    list=zip(id,audio_name,audio,video_name,video,pdf_name,pdf)
    return render(request,'files_display.html',{'data':list})

def update_data(request,id):
    a=register.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get('lname')
        if len(str(request.POST.get('dob')))>0:
            a.dob=request.POST.get('dob')
        else:
            a.save()
        if str(request.POST.get('gender'))=='female' or str(request.POST.get('gender'))=='male':
            a.gender=request.POST.get('gender')
        else:
            a.save()
        a.phone=request.POST.get('phone')
        a.email=request.POST.get('email')
        a.address=request.POST.get('address')
        a.username=request.POST.get('username')

        a.save()
        return redirect(display)
    
    return render(request,'editprofile.html',{'data':a})

def emp_update(request,id):
    a=employee.objects.get(id=id)
    if request.method=='POST':
        a.ename=request.POST.get('ename')
        a.phone=request.POST.get('phone')
        a.email=request.POST.get('email')
        a.designation=request.POST.get('designation')
        a.company_name=request.POST.get('company_name')
        a.save()
        return redirect(empdisplay)
    return render(request,'empedit.html',{'data':a})

def file_edit(request,id):
    a=fileupload.objects.get(id=id)
    image=str(a.fileimg).split('/')[-1]
    if request.method=='POST':
        a.item_name=request.POST.get('item_name')
        if request.FILES.get('fileimg')==None:
            a.save()
        else:
            a.fileimg = request.FILES.get('fileimg')
            a.save()
        a.description=request.POST.get('description')
        a.save()
        return redirect(filedisplay)
    return render(request,'filesedit.html',{'data':a,'img':image})

def edituploadfile(request,id):
    a=upload.objects.get(id=id)
    if request.method=='POST':
        a.audio_name=request.POST.get('audio_name')
        if request.FILES.get('audio')==None:
            a.save()
        else:
            a.audio=request.FILES.get('audio')
            a.save()
        a.video_name=request.POST.get('video_name')
        if request.FILES.get('video')==None:
            a.save()
        else:
            a.video=request.FILES.get('video')
            a.save()
        a.pdf_name=request.POST.get('pdf_name')
        if request.FILES.get('pdf')==None:
            a.save()
        else:
            a.pdf=request.FILES.get('pdf')
            a.save()
        a.save()
        return redirect(uploaddisplay)

    return render(request,'editupload.html',{'data':a})
def selectbox(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        state=request.POST.get('state')
        english=request.POST.get('english')
        if english=='on':
            english=True
        else:
            english=False
        malayalam = request.POST.get('malayalam')
        if malayalam=='on':
            malayalam=True
        else:
            malayalam=False
        hindi = request.POST.get('hindi')
        if hindi=='on':
            hindi=True
        else:
            hindi=False
        a=select(full_name=full_name,state=state,english=english,malayalam=malayalam,hindi=hindi)
        a.save()
        return HttpResponse('Success')
    return render(request,"select.html")

# delete
def user_delete(request,id):
    a=register.objects.get(id=id)
    a.delete()
    return redirect(display)

def files_delete(request,id):
    a=upload.objects.get(id=id)
    a.delete()
    return redirect(uploaddisplay)

def file_delete(request,id):
    a=fileupload.objects.get(id=id)
    a.delete()
    return redirect(filedisplay)
def empdelete(request,id):
    a=employee.objects.get(id=id)
    a.delete()
    return redirect(empdisplay)


def userreg(request):
    if request.method=='POST':
        a=user_reg(request.POST)
        if a.is_valid():
            u=request.POST.get('username')
            f=request.POST.get('first_name')
            l=request.POST.get('last_name')
            e=request.POST.get('email')
            ps=request.POST.get('password')
            b=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=ps)
            b.save()
            return HttpResponse("authenticated user added")
        else:
            return HttpResponse("User not added")
    else:
        form=user_reg()
        return render(request,'user_register.html',{'form':form})

def userregist(request):
    if request.method=='POST':
        a=userform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            fn=a.cleaned_data['first_name']
            ln=a.cleaned_data['last_name']
            em=a.cleaned_data['email']
            pa=a.cleaned_data['password']
            conf=a.cleaned_data['conf']
            if pa == conf:
                b=User(username=us,first_name=fn,last_name=ln,email=em)
                b.set_password(pa)
                b.save()
                return HttpResponse("Registered Successfully")
            else:
                return HttpResponse("Password Doesn't match")
        else:
            return HttpResponse("Failed")
    else:
        form=userform()
        return render(request,'userreg.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Logged in successfully.')
            else:
                return HttpResponse('Invalid username or password')
        else:
            return HttpResponse('login failed')
    return render(request,'log.html')




def read_response():
    with open(r"C:\Users\User\PycharmProjects\Django_Project\djangoproject\djangoapp\movie.json","r",encoding="utf8") as f:
        data=json.load(f)
        return data

from rest_framework.views import APIView
class myresponse(APIView):
    def get(self,request):
        data = read_response()
        return render(request,'movies_api.html',{'data':data})

def read_media():
    with open(r"C:\Users\User\PycharmProjects\Django_Project\djangoproject\djangoapp\fileupload_api.json","r",encoding="utf8") as n:
        data = json.load(n)
        return data

class file_respone(APIView):
    def get(self,request):
        data = read_media()
        return render(request,'files_api.html',{'data':data})

