from django.shortcuts import render,redirect
from .models import Post #import database post table
from .models import Items #import database post items
from .models import User_Manage #import database post user_manage
from .models import UploadFileForm #import database post items
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.core.files.images import ImageFile
import datetime
from django.db import connection

from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

from .forms import GeeksForm

db_type_items = ["Computer PC", "Notebook", "Netbook"]
db_os_items = ["Windows XP", "Windows 7", "Windows 10","Windows 11", "Android", "IOS", "Linux"]
db_act_type = ["Windows XP", "Windows 7", "Windows 10","Windows 11", "Android", "IOS", "Linux"]

# Create your views here.
def index(request):
    #Query ข้อมูล จาก Model
    data_registeritem= Items.objects.order_by('-Regist_datetime')[:3]
    #Query set จาก User_Manage id=1 แยก items
    #dd= User_Manage.objects.get(id=1)
    #print(dd.items_set.filter(PositionID_id='1').values())
    #print(dd.Name)
    db_index01=connection.cursor()
    db_index01.execute("SELECT blogs_items.id,blogs_items.Regist_datetime,\
                blogs_items.Number_item,blogs_items.Type,blogs_items.Type_details,\
                blogs_items.OS,blogs_user_manage.Name,blogs_user_manage.LastName,\
                blogs_items.Software,blogs_items.Status FROM blogs_items \
                INNER JOIN blogs_user_manage ON blogs_items.PositionID_id=blogs_User_Manage.PositionID ORDER BY id DESC LIMIT 3")
    result_db_index01=db_index01.fetchall()
    return render(request,'index.html',{'items':result_db_index01})

def page1(request):
    tags=['น้ำตก','ลาบ']
    rating = 2
    return render(request,'page1.html',
    {
        'name' : 'บทความ',
        'author':'konfqf',
        'tags':tags,
        'rating':rating
    })

def createForm(request):
    return render(request,'form.html',)

def addUser(request):
    username = request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username).exists():
            #print("Username นี้มีคนใช้แล้ว")
            messages.info(request,'Username นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            #print("Email นี้เคยลงทะเบียนแล้ว")
            messages.info(request,'email นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        else :
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
                )
            user.save()
            #return render(request,'result.html')
            return redirect('/')
    else :
        messages.info(request,'รหัสผ่านไม่ตรงกันนะ')
        return redirect('/addForm')

def loginForm(request):
    return render(request,'login.html',)

def login(request):
    username = request.POST['username']
    password=request.POST['password']

    #check user name password login
    user=auth.authenticate(username=username,password=password)
    
    if user is not None :
        auth.login(request,user)
        return redirect('/')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register_item(request):
    User_Manage_Name = User_Manage.objects.all()
    return render(request,'register_item.html',{'User_Manage_Name':User_Manage_Name})

def addItem(request):
    if request.method == 'POST':
        softwares = request.POST.getlist('softwares[]')
        print(softwares)
    item=Items.objects.create(
        Regist_datetime=datetime.datetime.now(),
        Number_item=request.POST.get('Numberitem'),
        Type=request.POST.get('Type'),
        Type_details=request.POST.get('TypeDetails'),
        OS=request.POST.get('OS'),
        PositionID_id=request.POST.get('PositionID'),
        #Software=request.POST.get('Software'),
        Software=request.POST.getlist('softwares'),
        Status=request.POST.get('Status'),
        )
    item.save()
    return redirect('/')

def edit_item(request):
    #load_data.OS
    if request.POST:
        if 'search' in request.POST:
            print('search')
            if request.POST.get('Search_Numberitem'):
                Numberitem = request.POST['Search_Numberitem']
                load_data = Items.objects.get(Number_item=Numberitem)
                count=0
                type_data_str=""
                db_data_str=""
                # for type_data_str in db_type_items:
                #     count+=1
                #     if count == int(load_data.Type):
                #         break
                # for db_data_str in db_os_items:
                #     count+=1
                #     if count == int(load_data.os):
                #         break
                print(load_data.Software)
                return render(request, 'edit_item.html',{
                    'Regist_datetime_data':load_data.Regist_datetime,
                    'Number_item_data':load_data.Number_item,
                    'Type_data':load_data.Type,
                    'Type_details_data':load_data.Type_details,
                    'OS_data':load_data.OS,
                    'Software_data':load_data.Software,
                    'Status_data':load_data.Status,
                    'PositionID_id_data':load_data.PositionID_id,
                    'db_type_data':db_type_items,
                    'db_os_data':db_os_items,
                }
                )
        elif 'save' in request.POST:
            print('confirm')
            # item=Items.objects.create(
            #     Number_item=request.POST.get('Numberitem_new'),
            #     Type=request.POST.get('Type_new'),
            #     Type_details=request.POST.get('TypeDetails_new'),
            #     OS=request.POST.get('OS_new'),
            #     PositionID_id=request.POST.get('PositionID_new'),
            #     Software=request.POST.get('Software_new'),
            #     Status=request.POST.get('Status_new'),
            #     )
            obj = Items.objects.get(pk=2)
            obj.Number_item = request.POST.get('Numberitem_new')
            obj.save()
            return redirect('/')
    return render(request, 'edit_item.html',)

def load_item(request):
    Numberitem = request.POST['Numberitem']
    print(Numberitem)
    Items_data = Items.objects.get(Number_item=Numberitem)
    print(Items_data.Type)
    #return redirect('/edit_item')
    # return redirect('/edit_item',
    # {#Items_data.Type
    #     'Type' : '1234',
    # })
    return render(request,'edit_item.html',{'Type':Items_data.Type})

    # if password==repassword :
    #     if User.objects.filter(username=username).exists():
    #         #print("Username นี้มีคนใช้แล้ว")
    #         messages.info(request,'Username นี้มีคนใช้แล้ว')
    #         return redirect('/edit_item')
    #     elif User.objects.filter(email=email).exists():
    #         #print("Email นี้เคยลงทะเบียนแล้ว")
    #         messages.info(request,'email นี้มีคนใช้แล้ว')
    #         return redirect('/edit_item')
    #     else :
    #         user=User.objects.create_user(
    #             username=username,
    #             password=password,
    #             email=email,
    #             first_name=firstname,
    #             last_name=lastname
    #             )
    #         user.save()
    #         return redirect('/')
    # else :
    #     messages.info(request,'รหัสผ่านไม่ตรงกันนะ')
    #     return redirect('/load_item')

def home_act(request):
    #Query ข้อมูล จาก Model
    acts = UploadFileForm.objects.all()
    return render(request,'home_act.html',{'acts':acts})

def register_act(request):
    User_Manage_Name = User_Manage.objects.all()
    return render(request,'register_act.html',{'User_Manage_Name':User_Manage_Name})

def add_act(request):
    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["geeks_field"])
    else:
        form = GeeksForm()
    context['form'] = form
    return render(request, "register_act.html", context)

def edit_act(request):
    #load_data.OS
    if request.POST:
        if 'search' in request.POST:
            print('search')
            if request.POST.get('Search_Numberitem'):
                Numberitem = request.POST['Search_Numberitem']
                load_data = Items.objects.get(Number_item=Numberitem)
                count=0
                type_data_str=""
                db_data_str=""
                print(load_data.Software)
                return render(request, 'edit_item.html',{
                    'Regist_datetime_data':load_data.Regist_datetime,
                    'Number_item_data':load_data.Number_item,
                    'Type_data':load_data.Type,
                    'Type_details_data':load_data.Type_details,
                    'OS_data':load_data.OS,
                    'Software_data':load_data.Software,
                    'Status_data':load_data.Status,
                    'PositionID_id_data':load_data.PositionID_id,
                    'db_type_data':db_type_items,
                    'db_os_data':db_os_items,
                }
                )
        elif 'save' in request.POST:
            print('confirm')
            obj = Items.objects.get(pk=2)
            obj.Number_item = request.POST.get('Numberitem_new')
            obj.save()
            return redirect('/')
    return render(request, 'edit_act.html',)

def load_act(request):
    Numberitem = request.POST['Numberitem']
    print(Numberitem)
    Items_data = Items.objects.get(Number_item=Numberitem)
    print(Items_data.Type)
    return render(request,'edit_act.html',{'Type':Items_data.Type})

#image01
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'index.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')

# Python program to view
# for displaying images


def display_hotel_images(request):

	if request.method == 'GET':

		# getting all the objects of hotel.
		Hotels = Hotel.objects.all()
		return render((request, 'display_hotel_images.html',
					{'hotel_images': Hotels}))

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

from .forms import GeeksForm

def handle_uploaded_file(f):  
    import os
    with open(os.path.join("E:/", "shared")+'/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  

from .models import UploadFileForm

# Create your views here.
def home_view(request):
    if request.method == 'POST':  
        pdf = UploadFileForm(request.POST, request.FILES)  
        if pdf.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            model_instance = pdf.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        pdf = UploadFileForm()  
        return render(request,"home.html",{'form':pdf}) 

def register_view(request):
    if request.method == 'POST':  
        pdf = UploadFileForm()
        #pdf = UploadFileForm(request.POST, request.FILES)  
        #if pdf.is_valid():  
            # handle_uploaded_file(request.FILES['file'])  
            # pdf.Act_Status = "abcdwrfe"
            # #model_instance = pdf.save(commit=False)
            # pdf.Act_Status = "abcdwrfe"
            # print(pdf.Act_Status)
            # pdf.save()
            # #model_instance.save()
            # #return HttpResponse("File uploaded successfuly")  
            # #return render(request,"register_act.html",{'form':pdf})
            # return redirect('/')
            
        handle_uploaded_file(request.FILES['file'])  
        pdf.Act_Status = "abcdwrfe"
        pdf.Date_Register = datetime.datetime.now()
        pdf.Date_Act_Notice  = datetime.datetime.now()
        pdf.Date_Act_Use =datetime.datetime.now()
        pdf.Act_Freq_Repeat = 0
        pdf.file = request.FILES['file']
        print(pdf.Act_Status)
        pdf.save()
        return redirect('/home_act')
    else:  
        pdf = UploadFileForm()
        return render(request,"register_act.html",{'form':pdf}) 