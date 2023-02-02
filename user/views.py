import datetime
from gc import get_objects
from http.client import HTTPResponse
from tokenize import group
import uuid
from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm,SirketRegisterForm,CalisanRegisterForm,MaasRegisterForm,monthform,calisanturform,engelliform,MaliMusavirRegisterForm,denemeform,SubeRegisterForm,malisirketRegisterForm,employeelistaylar,sgkisyeriregisterform,iskurregisterform
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required,permission_required, user_passes_test
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from .models import maas,sirket,calisan,mali_musavir,bordro,sube,mali_sirket,subs,maintence,iskur,sgkisyeri
from django.http import HttpResponse
from app.views import autouser,sendlist
from app.tekayhesaplama import hesaplama1
from django.db.models import Q
from django.template import RequestContext

from django.urls import reverse
import datetime

from datetime import datetime, timedelta

@login_required(login_url='user:login')
def index(request):
    sirket1=[]
    sirket2=None
    if maintence.objects.first().maintence:
        return render(request,'maintence.html')

    if request.user.groups.filter(name='admin').exists():
        calisantab=False
        sirkettab=False
        user=None
        sirket1=sirket.objects.all()


    else :

        if request.user.groups.filter(name='mali_musavir').exists():
            calisantab=False
            user=mali_musavir.objects.get(mali_musavir_id=request.user)
            malisirket=mali_sirket.objects.get(id=user.mali_sirket_id.id)

            sirkettab=False
            sirket1=malisirket.mali_sirket_bagli_sirketler.all()


        elif request.user.groups.filter(name='muhasebe').exists():
            calisantab=True
            sirkettab=False
            user=calisan.objects.get(calisan_id=request.user)
            sirket1.append(sirket.objects.get(id=user.calisan_sirket_id.id).id)
            sirket2=sirket1[0]

           
        else:
            calisantab=False
            sirkettab=False
            user=calisan.objects.get(calisan_id=request.user)
            sirket1.append(sirket.objects.get(id=user.calisan_sirket_id.id).id)
            sirket2=sirket1[0]

    mainpage=True

    dolar=getdolar()[0][1]
    euro=geteuro()[0][1]


    context={
        'sirket_id':sirket2,
        'calisantab':calisantab,
        'sirkettab':sirkettab,
        'user1':user,
        'mainpage':mainpage,
        'dolar':dolar,
        'euro':euro,
        'sirketedit':False,
        'subeedit':False,



    }
    return render(request,'homepage.html',context)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def getdolar():
    startDate= ""
    endDate=""
    if int(datetime.now().hour)<15 and int(datetime.now().minute)<30:
        date_today = (datetime.today()-timedelta(days=1)).date().strftime("%d-%m-%Y")

        startDate=date_today


        endDate=date_today

    else:
        date_today = (datetime.today()).date().strftime("%d-%m-%Y")
        startDate=date_today

        endDate=date_today


    i=1
    while True:

        series ="TP.DK.USD.A.YTL"
        series_name="Dolar_Kuru"
        typee="csv"
        key="dJqoNMHhsC"
        aggregationTypes="avg"
        formulas="0"
        frequency = "2"
        url= 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(series,
        startDate,endDate,typee,key,aggregationTypes,formulas,frequency)
        try:
            dolar = pd.read_csv(url)
            break
        except:
            date_today = (datetime.today()-timedelta(days=i)).date().strftime("%d-%m-%Y")
            startDate= date_today
            endDate=date_today
            i+=1






    dolar1=dolar.values.tolist()


    return dolar1
def geteuro():
    startDate= ""
    endDate=""
    if int(datetime.now().hour)<15 and int(datetime.now().minute)<30:
        date_today = (datetime.today()-timedelta(days=1)).date().strftime("%d-%m-%Y")
        startDate=date_today


        endDate=date_today

    else:
        date_today = (datetime.today()).date().strftime("%d-%m-%Y")
        startDate=date_today
        endDate=date_today

    i=1
    while True:
        series ="TP.DK.EUR.A.YTL"
        series_name="Euro_Kuru"
        typee="csv"
        key="dJqoNMHhsC"
        aggregationTypes="avg"
        formulas="0"
        frequency = "2"
        url= 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(series,
        startDate,endDate,typee,key,aggregationTypes,formulas,frequency)
        try:
            euro = pd.read_csv(url)
            break
        except:
            date_today = (datetime.today()-timedelta(days=i)).date().strftime("%d-%m-%Y")
            startDate= date_today
            endDate=date_today
            i+=1

    euro1=euro.values.tolist()

    return euro1

def hesapla(request,id,year,tesvik,engelli,indirim):
    employee=calisan.objects.get(id=id)
    user1=User.objects.get(id=employee.calisan_id_id)
    maass=maas.objects.filter(calisan_id=employee,yil=year)

    argegun=[]
    ucret=[]
    gun=[]
    gun.append(maass[0].gunsayisi1)
    gun.append(maass[0].gunsayisi2)
    gun.append(maass[0].gunsayisi3)
    gun.append(maass[0].gunsayisi4)
    gun.append(maass[0].gunsayisi5)
    gun.append(maass[0].gunsayisi6)
    gun.append(maass[0].gunsayisi7)
    gun.append(maass[0].gunsayisi8)
    gun.append(maass[0].gunsayisi9)
    gun.append(maass[0].gunsayisi10)
    gun.append(maass[0].gunsayisi11)
    gun.append(maass[0].gunsayisi12)
    argegun.append(maass[0].argegun1)
    argegun.append(maass[0].argegun2)
    argegun.append(maass[0].argegun3)
    argegun.append(maass[0].argegun4)
    argegun.append(maass[0].argegun5)
    argegun.append(maass[0].argegun6)
    argegun.append(maass[0].argegun7)
    argegun.append(maass[0].argegun8)
    argegun.append(maass[0].argegun9)
    argegun.append(maass[0].argegun10)
    argegun.append(maass[0].argegun11)
    argegun.append(maass[0].argegun12)
    ucret.append(maass[0].maas_tutari1)
    ucret.append(maass[0].maas_tutari2)
    ucret.append(maass[0].maas_tutari3)
    ucret.append(maass[0].maas_tutari4)
    ucret.append(maass[0].maas_tutari5)
    ucret.append(maass[0].maas_tutari6)
    ucret.append(maass[0].maas_tutari7)
    ucret.append(maass[0].maas_tutari8)
    ucret.append(maass[0].maas_tutari9)
    ucret.append(maass[0].maas_tutari10)
    ucret.append(maass[0].maas_tutari11)
    ucret.append(maass[0].maas_tutari12)
    parabirimi=maass[0].para_birimi



    return autouser(request,ucret,gun,argegun,tesvik,engelli,indirim,year,parabirimi,False)

def getlist(request,id,year,):
    if request.user.groups.filter(name='admin').exists():
        pass
    elif request.user.groups.filter(name='mali_musavir').exists():
        if sirket.objects.get(sirket_mali_musavir_id=request.user,id=calisan.objects.get(id=id).calisan_sirket_id.id).sirket_mali_musavir_id!=request.user:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    elif request.user.groups.filter(name='calisan').exists():
        if request.user.id != calisan.objects.get(id=id).calisan_id_id:
            return HttpResponseNotFound("Yetkisiz Erişim")

    employee=calisan.objects.filter(id=id)
    tesvik=employee[0].calisan_tesvik
    engelli=employee[0].calisan_engelli
    indirim=employee[0].calisan_indirim





    return getlist1(request,id,year,tesvik,engelli,indirim)


def getlist1(request,id,year,tesvik,engelli,indirim):
    employee=calisan.objects.get(id=id)
    maass=maas.objects.filter(calisan_id=employee,yil=year)
    ucret=[]
    parabirimi=maass[0].para_birimi
    argegun=[]
    gun=[]
    gun.append(maass[0].gunsayisi1)
    gun.append(maass[0].gunsayisi2)
    gun.append(maass[0].gunsayisi3)
    gun.append(maass[0].gunsayisi4)
    gun.append(maass[0].gunsayisi5)
    gun.append(maass[0].gunsayisi6)
    gun.append(maass[0].gunsayisi7)
    gun.append(maass[0].gunsayisi8)
    gun.append(maass[0].gunsayisi9)
    gun.append(maass[0].gunsayisi10)
    gun.append(maass[0].gunsayisi11)
    gun.append(maass[0].gunsayisi12)
    argegun.append(maass[0].argegun1)
    argegun.append(maass[0].argegun2)
    argegun.append(maass[0].argegun3)
    argegun.append(maass[0].argegun4)
    argegun.append(maass[0].argegun5)
    argegun.append(maass[0].argegun6)
    argegun.append(maass[0].argegun7)
    argegun.append(maass[0].argegun8)
    argegun.append(maass[0].argegun9)
    argegun.append(maass[0].argegun10)
    argegun.append(maass[0].argegun11)
    argegun.append(maass[0].argegun12)
    ucret.append(maass[0].maas_tutari1)
    ucret.append(maass[0].maas_tutari2)
    ucret.append(maass[0].maas_tutari3)
    ucret.append(maass[0].maas_tutari4)
    ucret.append(maass[0].maas_tutari5)
    ucret.append(maass[0].maas_tutari6)
    ucret.append(maass[0].maas_tutari7)
    ucret.append(maass[0].maas_tutari8)
    ucret.append(maass[0].maas_tutari9)
    ucret.append(maass[0].maas_tutari10)
    ucret.append(maass[0].maas_tutari11)
    ucret.append(maass[0].maas_tutari12)
    empmaas=list(sendlist(request,ucret,gun,argegun,tesvik,engelli,indirim,year,parabirimi))



    return empmaas
def select_register_type(request):
    return render(request,'registertype.html')

def register(request):
    form = RegisterForm(request.POST or None)
    form2=calisanturform(request.POST or None)
    form3=engelliform(request.POST or None)
    form4=MaliMusavirRegisterForm(request.POST or None,request.FILES or None)
    form5=malisirketRegisterForm(request.POST or None)
    if form.is_valid()  and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
        username=form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()


        mali = form4.save(commit=False)
        zaman=datetime.now()
        mali.deneme_suresi=True
        mali.mali_musavir_id=newUser
        malis=form5.save(commit=False)
        malis.mali_sirket_davet_kodu=uuid.uuid1()
        print(malis.mali_sirket_davet_kodu)
        malis.save()

        mali.deneme_bitis_tarihi=zaman.date()+timedelta(days=15)
        if  not mali.mali_musavir_photo :
            if mali.mali_musavir_gender=="pick1":
                mali.mali_musavir_photo="/calisan_photo/default.png"
            elif mali.mali_musavir_gender=="pick2":
                mali.mali_musavir_photo="/calisan_photo/defaultw.png"
            else:
                mali.mali_musavir_photo="/calisan_photo/default.png"
        malis1=mali_sirket.objects.get(mali_sirket_davet_kodu=malis.mali_sirket_davet_kodu)
        mali.mali_sirket_id=malis1
        mali.save()
        mali1= mali_musavir.objects.get(mali_musavir_tc=mali.mali_musavir_tc)
        mali2= User.objects.get(id=mali1.mali_musavir_id_id)





        newUser.groups.add(Group.objects.get(name='mali_musavir'))
        login(request, newUser)
        messages.success(request, 'Kayıt İşlemi Başarılı')

        return redirect('user:homepage')
    context = {
            'form': form,
            'form2':form2,
            'form3':form3,
            'form4':form4,
            'form5':form5,
            }
    return render(request, 'user/register.html',context)

def register_with_company(request):
    form = RegisterForm(request.POST or None)
    form3 = SirketRegisterForm(request.POST or None)
    calisan1=CalisanRegisterForm(request.POST or None,request.FILES or None)
    form1=calisanturform(request.POST or None)
    form2=engelliform(request.POST or None)

    if  calisan1.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
        username=request.POST.get('username1')
        password = request.POST.get('password1')
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.is_active=True
        newUser.save()
        sirket1=form3.save(commit=False)
        sirket1.sirket_davet_kodu=uuid.uuid1()
        sirket1.save()
        company1=sirket.objects.get(sirket_davet_kodu=sirket1.sirket_davet_kodu,sirket_adi=sirket1.sirket_adi,sirket_adres=sirket1.sirket_adres)
        sube.objects.create(sube_adi="Merkez",sube_adres=company1.sirket_adres,sube_sirket_id=company1)


        calisan2=calisan1.save(commit=False)



        newUser.groups.add(Group.objects.get(name='muhasebe'))
        sube2=sube.objects.get(sube_sirket_id=company1,sube_adi="Merkez")
        sgkisyeri.objects.create(sube_id=sube2)
        iskur.objects.create(sube_id=sube2)
        time=datetime.now()
        subs.objects.create(subs_sirket_adi=company1.sirket_adi,subs_aktiflik=False,subs_baslangic_tarihi=time,subs_gun_sayisi=5,subs_maksimum_calisan=2)
        company1.sirket_uyelik=subs.objects.get(subs_sirket_adi=company1.sirket_adi,subs_aktiflik=True,subs_baslangic_tarihi=time,subs_gun_sayisi=5,subs_maksimum_calisan=2)
        

        calisan2.calisan_sube_id=sube2
        calisan2.calisan_sirket_id=company1
        calisan2.calisan_engelli=form2.cleaned_data.get('engelli')
        lastid=User.objects.get(username=username)
        calisan2.calisan_id=lastid
        company1.save()
        calisan2.calisan_tur="pick1"
        if not calisan2.calisan_photo:
            if calisan2.calisan_gender=="pick1":
                calisan2.calisan_photo="/calisan_photo/default.png"
            elif calisan2.calisan_gender=="pick2":
                calisan2.calisan_photo="/calisan_photo/defaultw.png"
            else:
                calisan2.calisan_photo="/calisan_photo/default.png"
        
        calisan2.save()
        temp=maas.objects.create(calisan_id=calisan.objects.get(calisan_id=lastid),yil=datetime.now().year)
        temp.save()
        maas1=maas.objects.get(calisan_id=calisan.objects.get(calisan_id=lastid),yil=datetime.now().year)
        bordro.objects.create(maas_id=maas1,calisan_id=calisan.objects.get(calisan_id=lastid))
        user=authenticate(username=username,password=password)
        login(request, user)


        return redirect('user:homepage')

    else:
         context = {
            'form': form,
            'calisan':calisan1,
            'form1':form1,
            'form2':form2,
            'form3':form3,

            }
    return render(request, 'muhaseberegister.html',context)


@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def companyregister(request):
    form = SirketRegisterForm(request.POST or None)
    if form.is_valid():

        company=form.save(commit=False)

        temp=uuid.uuid1()
        company.sirket_davet_kodu=temp
        company.save()
        company1=sirket.objects.get(sirket_adi=company.sirket_adi,sirket_adres=company.sirket_adres,sirket_davet_kodu=temp)
        sube.objects.create(sube_adi="Merkez",sube_adres=company.sirket_adres,sube_sirket_id=company1)
        time=datetime.now()
        subs.objects.create(subs_sirket_adi=company1.sirket_adi,subs_aktiflik=True,subs_baslangic_tarihi=time,subs_gun_sayisi=5,subs_maksimum_calisan=2)
        company1.sirket_uyelik=subs.objects.get(subs_sirket_adi=company1.sirket_adi,subs_aktiflik=False,subs_baslangic_tarihi=time,subs_gun_sayisi=5,subs_maksimum_calisan=2)
        company1.save()
        if request.user.groups.filter(name='mali_musavir').exists():
            mali=mali_musavir.objects.get(mali_musavir_id=request.user)
            mali1=mali_sirket.objects.get(id=mali.mali_sirket_id_id)
            sirket1=sirket.objects.get(sirket_adi=company.sirket_adi,sirket_adres=company.sirket_adres,sirket_davet_kodu=company.sirket_davet_kodu)
            mali1.mali_sirket_bagli_sirketler.add(sirket1)
            mali1.save()
        return redirect('user:homepage')

    context = {
            'form': form
            }
    return render(request, 'addcompany.html',context)


def suberegister(request,id):
    form = SubeRegisterForm(request.POST or None)
    if form.is_valid():
        sube=form.save(commit=False)
        sube.sube_sirket_id=sirket.objects.get(id=id)
        sube.save()
        redirect(reverse('user:subelist', kwargs={'id':id}))

    context = {
            'form': form
            }
    return render(request, 'addsube.html',context)


def turkish_id_no_check(tc_no):
    ''' turkish_id_no_check(long) -> bool
        
    Return the validation of Turkish Identification Number
      
    >>> turkish_id_no_check(98768109974)
    True 
    '''
    if len(str(tc_no)) != 11:
        return False
    list_tc = list(map(int,str(tc_no)))
    tc10 = (sum(list_tc[0:10:2])*7 - sum(list_tc[1:9:2])) % 10
    tc11 = (sum(list_tc[0:9]) + tc10) % 10
    return True if list_tc[9] == tc10 and list_tc[10] == tc11 else False
def listsube(request,id):
    sube1=sube.objects.filter(sube_sirket_id=id)
    aylar=employeelistaylar(request.POST or None)
    form=denemeform(request.POST or None)
    if (sirket.objects.filter(id=id)).exists():
        company=sirket.objects.get(id=id)
    else:
        return handler404(request,exception=404)
    if( request.user.groups.filter(name='mali_musavir').exists() or request.user.groups.filter(name='admin').exists() or request.user.groups.filter(name='muhasebe').exists()  ):
        employees1=[]
        deneme=[]
        deneme1=[]
        count=0
        for i in sube1:
            employees1.append(calisan.objects.filter(calisan_sube_id=i.id,calisan_isten_ayrilma=False).order_by('calisan_soyadi'))


        if employees1:
            for i in employees1:
                for k in i:

                    if maas.objects.filter(calisan_id=k.id,yil=date.today().year).exists():
                        deneme.append(maas.objects.filter(calisan_id=k.id,yil=date.today().year))
                    count=count+1

        if deneme :
            for i in deneme:

                if bordro.objects.filter(maas_id=i[0].id,).exists():
                    deneme1.append(bordro.objects.filter(maas_id=i[0].id))

        calisantab=False
        month=datetime.now().month
        maxuser=subs.objects.filter(id=company.sirket_uyelik.id)
        maxuser=maxuser[0].subs_maksimum_calisan
        calisansayi=count

        uyelik=True
        uyelik1=True
        if subs.objects.filter(id=company.sirket_uyelik_id).exists():
            subs1=subs.objects.get(id=company.sirket_uyelik_id)
        if subs1.subs_baslangic_tarihi + timedelta(subs1.subs_gun_sayisi)<datetime.now().date():
             subs1.subs_aktiflik=False
             subs1.save()
        if subs.objects.get(id=company.sirket_uyelik_id).subs_aktiflik==False:
            uyelik=False
        if subs.objects.get(id=company.sirket_uyelik_id).subs_maksimum_calisan<=calisansayi:
            uyelik1=False
        if request.method == 'POST':
            employees=[]
            for i in employees1:
                for k in i:
                    employees.append(k)
            if employees :
                for i in employees:
                    
                        if maas.objects.filter(calisan_id=i,yil=date.today().year).exists():
                            deneme.append(maas.objects.filter(calisan_id=i,yil=date.today().year))
                        else:
                            deneme.append(maas.objects.none())
            if "infobutton" in request.POST:
                for i in range(1,len(employees)+1):
                    if request.POST.get("input1"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input1"+str(employees[i-1].id)+""))!=0:
                        if not request.POST.get("input1"+str(employees[i-1].id)+"").isdigit():
                            employees[i-1].calisan_adi=request.POST.get("input1"+str(employees[i-1].id)+"")
                        else:
                             messages.error(request, 'Lütfen isim alanına sayı girmeyiniz')
                             return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input2"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input2"+str(employees[i-1].id)+""))!=0:
                        if not request.POST.get("input2"+str(employees[i-1].id)+"").isdigit():
                            employees[i-1].calisan_soyadi=request.POST.get("input2"+str(employees[i-1].id)+"")
                        else:
                                messages.error(request, 'Lütfen soyisim alanına sayı girmeyiniz')
                                return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input3"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input3"+str(employees[i-1].id)+""))!=0:
                        if turkish_id_no_check(request.POST.get("input3"+str(employees[i-1].id)+"")):
                            employees[i-1].calisan_tc=request.POST.get("input3"+str(employees[i-1].id)+"")
                        else:
                            messages.error(request, 'Lütfen geçerli bir TC kimlik numarası giriniz')
                            return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input4"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input4"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_mail=request.POST.get("input4"+str(employees[i-1].id)+"")
                    if request.POST.get("input5"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input5"+str(employees[i-1].id)+""))!=0:
                        if request.POST.get("input5"+str(employees[i-1].id)+"").isdigit():
                            employees[i-1].calisan_telefon=request.POST.get("input5"+str(employees[i-1].id)+"")
                        else:
                            messages.error(request, 'Lütfen telefon alanına harf girmeyiniz')
                            return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input6"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input6"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_adres=request.POST.get("input6"+str(employees[i-1].id)+"")
                    if request.POST.get("input7"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input7"+str(employees[i-1].id)+""))!=0:
                        d=request.POST.get("input7"+str(employees[i-1].id)+"")
                        employees[i-1].calisan_dogum_tarihi=d
                    if request.POST.get("input8"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input8"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_ise_giris_tarihi=request.POST.get("input8"+str(employees[i-1].id)+"")
                    if request.POST.get("calisanengel"+str(employees[i-1].id)+"") is not None and len(request.POST.get("calisanengel"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_engelli=request.POST.get("calisanengel"+str(employees[i-1].id)+"")
                    if request.POST.get("calisanemekli"+str(employees[i-1].id)+"") is not None and len(request.POST.get("calisanemekli"+str(employees[i-1].id)+""))!=0:
                        print(request.POST.get("calisanemekli"+str(employees[i-1].id)+""))
                        employees[i-1].calisan_emekli=request.POST.get("calisanemekli"+str(employees[i-1].id)+"")
                    if request.POST.get("calisanogrenim"+str(employees[i-1].id)+"") is not None and len(request.POST.get("calisanogrenim"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_ogrenim_durumu=request.POST.get("calisanogrenim"+str(employees[i-1].id)+"")
                    if request.POST.get("inputiban"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputiban"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_iban=request.POST.get("inputiban"+str(employees[i-1].id)+"")
                    employees[i-1].save()
                    
            if "maasbuton" in request.POST:

                for i in range(1,len(employees)+1):
                    if request.POST.get("calisantesvik"+str(employees[i-1].id)+"") is not None:
                        employees[i-1].calisan_tesvik=request.POST.get("calisantesvik"+str(employees[i-1].id)+"")
                    employees[i-1].save()

                    if request.POST.get("maas"+str(employees[i-1].id)+"") is not None and len(request.POST.get("maas"+str(employees[i-1].id)+""))!=0:

                        if maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).exists():
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(ucret=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                            ay=request.POST.get("aylar")
                            bordro1=bordro.objects.get(maas_id=maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id)
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(ucrettipi=request.POST.get("ucrettipi"+str(employees[i-1].id)+""))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(para_birimi=request.POST.get("parabirimi"+str(employees[i-1].id)+""))

                            
                            if ay=="ocak":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)

                                bordro1.ocak_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.ocak_brut=data[0]
                                bordro1.ocak_calisilan_gun=data[1]
                                bordro1.ocak_arge_gun=data[2]
                                bordro1.ocak_bordroyaesasbrut=data[3]
                                bordro1.ocak_sgk_matrahi=data[4]
                                bordro1.ocak_sgk_kesintisi=data[5]
                                bordro1.ocak_issizlik_kesintisi=data[6]
                                bordro1.ocak_vergi_matrahi=data[7]
                                bordro1.ocak_kumulatif_vergi=data[8]
                                bordro1.ocak_istisna_oncesi_gelir=data[9]
                                bordro1.ocak_kumulatif_asgari_ucret=data[10]
                                bordro1.ocak_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.ocak_damga_vergisi=data[12]
                                bordro1.ocak_gelir_vergisi=data[13]
                                bordro1.ocak_net_ucret=data[14]
                                bordro1.ocak_isveren_sgk_kesintisi=data[15]
                                bordro1.ocak_isveren_issizlik_kesintisi=data[16]
                                bordro1.ocak_toplam_sgk_kesintisi=data[17]
                                bordro1.ocak_sgk_istisnasi=data[18]
                                bordro1.ocak_odenecek_sgk=data[19]
                                bordro1.ocak_odenecek_gelir_vergisi=data[21]
                                bordro1.ocak_odenecek_damga_vergisi=data[22]
                                bordro1.ocak_istisna_oncesi_damga=data[23]
                                bordro1.ocak_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.ocak_toplam_maliyet=data[25]
                                bordro1.ocak_vergi_dilimi=data[26]
                                bordro1.ocak_gelir_vergisi_istisnasi=data[27]
                                bordro1.ocak_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="subat":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.subat_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.subat_brut=data[0]
                                bordro1.subat_calisilan_gun=data[1]
                                bordro1.subat_arge_gun=data[2]
                                bordro1.subat_bordroyaesasbrut=data[3]
                                bordro1.subat_sgk_matrahi=data[4]
                                bordro1.subat_sgk_kesintisi=data[5]
                                bordro1.subat_issizlik_kesintisi=data[6]
                                bordro1.subat_vergi_matrahi=data[7]
                                bordro1.subat_kumulatif_vergi=data[8]
                                bordro1.subat_istisna_oncesi_gelir=data[9]
                                bordro1.subat_kumulatif_asgari_ucret=data[10]
                                bordro1.subat_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.subat_damga_vergisi=data[12]
                                bordro1.subat_gelir_vergisi=data[13]
                                bordro1.subat_net_ucret=data[14]
                                bordro1.subat_isveren_sgk_kesintisi=data[15]
                                bordro1.subat_isveren_issizlik_kesintisi=data[16]
                                bordro1.subat_toplam_sgk_kesintisi=data[17]
                                bordro1.subat_sgk_istisnasi=data[18]
                                bordro1.subat_odenecek_sgk=data[19]
                                bordro1.subat_odenecek_gelir_vergisi=data[21]
                                bordro1.subat_odenecek_damga_vergisi=data[22]
                                bordro1.subat_istisna_oncesi_damga=data[23]
                                bordro1.subat_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.subat_toplam_maliyet=data[25]
                                bordro1.subat_vergi_dilimi=data[26]
                                bordro1.subat_gelir_vergisi_istisnasi=data[27]
                                bordro1.subat_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()

                            elif ay=="mart":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.mart_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.mart_brut=data[0]
                                bordro1.mart_calisilan_gun=data[1]
                                bordro1.mart_arge_gun=data[2]
                                bordro1.mart_bordroyaesasbrut=data[3]
                                bordro1.mart_sgk_matrahi=data[4]
                                bordro1.mart_sgk_kesintisi=data[5]
                                bordro1.mart_issizlik_kesintisi=data[6]
                                bordro1.mart_vergi_matrahi=data[7]
                                bordro1.mart_kumulatif_vergi=data[8]
                                bordro1.mart_istisna_oncesi_gelir=data[9]
                                bordro1.mart_kumulatif_asgari_ucret=data[10]
                                bordro1.mart_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.mart_damga_vergisi=data[12]
                                bordro1.mart_gelir_vergisi=data[13]
                                bordro1.mart_net_ucret=data[14]
                                bordro1.mart_isveren_sgk_kesintisi=data[15]
                                bordro1.mart_isveren_issizlik_kesintisi=data[16]
                                bordro1.mart_toplam_sgk_kesintisi=data[17]
                                bordro1.mart_sgk_istisnasi=data[18]
                                bordro1.mart_odenecek_sgk=data[19]
                                bordro1.mart_odenecek_gelir_vergisi=data[21]
                                bordro1.mart_odenecek_damga_vergisi=data[22]
                                bordro1.mart_istisna_oncesi_damga=data[23]
                                bordro1.mart_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.mart_toplam_maliyet=data[25]
                                bordro1.mart_vergi_dilimi=data[26]
                                bordro1.mart_gelir_vergisi_istisnasi=data[27]
                                bordro1.mart_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="nisan":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.nisan_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.nisan_brut=data[0]
                                bordro1.nisan_calisilan_gun=data[1]
                                bordro1.nisan_arge_gun=data[2]
                                bordro1.nisan_bordroyaesasbrut=data[3]
                                bordro1.nisan_sgk_matrahi=data[4]
                                bordro1.nisan_sgk_kesintisi=data[5]
                                bordro1.nisan_issizlik_kesintisi=data[6]
                                bordro1.nisan_vergi_matrahi=data[7]
                                bordro1.nisan_kumulatif_vergi=data[8]
                                bordro1.nisan_istisna_oncesi_gelir=data[9]
                                bordro1.nisan_kumulatif_asgari_ucret=data[10]
                                bordro1.nisan_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.nisan_damga_vergisi=data[12]
                                bordro1.nisan_gelir_vergisi=data[13]
                                bordro1.nisan_net_ucret=data[14]
                                bordro1.nisan_isveren_sgk_kesintisi=data[15]
                                bordro1.nisan_isveren_issizlik_kesintisi=data[16]
                                bordro1.nisan_toplam_sgk_kesintisi=data[17]
                                bordro1.nisan_sgk_istisnasi=data[18]
                                bordro1.nisan_odenecek_sgk=data[19]
                                bordro1.nisan_odenecek_gelir_vergisi=data[21]
                                bordro1.nisan_odenecek_damga_vergisi=data[22]
                                bordro1.nisan_istisna_oncesi_damga=data[23]
                                bordro1.nisan_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.nisan_toplam_maliyet=data[25]
                                bordro1.nisan_vergi_dilimi=data[26]
                                bordro1.nisan_gelir_vergisi_istisnasi=data[27]
                                bordro1.nisan_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="mayis":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.mayis_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.mayis_brut=data[0]
                                bordro1.mayis_calisilan_gun=data[1]
                                bordro1.mayis_arge_gun=data[2]
                                bordro1.mayis_bordroyaesasbrut=data[3]
                                bordro1.mayis_sgk_matrahi=data[4]
                                bordro1.mayis_sgk_kesintisi=data[5]
                                bordro1.mayis_issizlik_kesintisi=data[6]
                                bordro1.mayis_vergi_matrahi=data[7]
                                bordro1.mayis_kumulatif_vergi=data[8]
                                bordro1.mayis_istisna_oncesi_gelir=data[9]
                                bordro1.mayis_kumulatif_asgari_ucret=data[10]
                                bordro1.mayis_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.mayis_damga_vergisi=data[12]
                                bordro1.mayis_gelir_vergisi=data[13]
                                bordro1.mayis_net_ucret=data[14]
                                bordro1.mayis_isveren_sgk_kesintisi=data[15]
                                bordro1.mayis_isveren_issizlik_kesintisi=data[16]
                                bordro1.mayis_toplam_sgk_kesintisi=data[17]
                                bordro1.mayis_sgk_istisnasi=data[18]
                                bordro1.mayis_odenecek_sgk=data[19]
                                bordro1.mayis_odenecek_gelir_vergisi=data[21]
                                bordro1.mayis_odenecek_damga_vergisi=data[22]
                                bordro1.mayis_istisna_oncesi_damga=data[23]
                                bordro1.mayis_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.mayis_toplam_maliyet=data[25]
                                bordro1.mayis_vergi_dilimi=data[26]
                                bordro1.mayis_gelir_vergisi_istisnasi=data[27]
                                bordro1.mayis_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="haziran":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.haziran_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.haziran_brut=data[0]
                                bordro1.haziran_calisilan_gun=data[1]
                                bordro1.haziran_arge_gun=data[2]
                                bordro1.haziran_bordroyaesasbrut=data[3]
                                bordro1.haziran_sgk_matrahi=data[4]
                                bordro1.haziran_sgk_kesintisi=data[5]
                                bordro1.haziran_issizlik_kesintisi=data[6]
                                bordro1.haziran_vergi_matrahi=data[7]
                                bordro1.haziran_kumulatif_vergi=data[8]
                                bordro1.haziran_istisna_oncesi_gelir=data[9]
                                bordro1.haziran_kumulatif_asgari_ucret=data[10]
                                bordro1.haziran_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.haziran_damga_vergisi=data[12]
                                bordro1.haziran_gelir_vergisi=data[13]
                                bordro1.haziran_net_ucret=data[14]
                                bordro1.haziran_isveren_sgk_kesintisi=data[15]
                                bordro1.haziran_isveren_issizlik_kesintisi=data[16]
                                bordro1.haziran_toplam_sgk_kesintisi=data[17]
                                bordro1.haziran_sgk_istisnasi=data[18]
                                bordro1.haziran_odenecek_sgk=data[19]
                                bordro1.haziran_odenecek_gelir_vergisi=data[21]
                                bordro1.haziran_odenecek_damga_vergisi=data[22]
                                bordro1.haziran_istisna_oncesi_damga=data[23]
                                bordro1.haziran_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.haziran_toplam_maliyet=data[25]
                                bordro1.haziran_vergi_dilimi=data[26]
                                bordro1.haziran_gelir_vergisi_istisnasi=data[27]
                                bordro1.haziran_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="temmuz":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.temmuz_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.temmuz_brut=data[0]
                                bordro1.temmuz_calisilan_gun=data[1]
                                bordro1.temmuz_arge_gun=data[2]
                                bordro1.temmuz_bordroyaesasbrut=data[3]
                                bordro1.temmuz_sgk_matrahi=data[4]
                                bordro1.temmuz_sgk_kesintisi=data[5]
                                bordro1.temmuz_issizlik_kesintisi=data[6]
                                bordro1.temmuz_vergi_matrahi=data[7]
                                bordro1.temmuz_kumulatif_vergi=data[8]
                                bordro1.temmuz_istisna_oncesi_gelir=data[9]
                                bordro1.temmuz_kumulatif_asgari_ucret=data[10]
                                bordro1.temmuz_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.temmuz_damga_vergisi=data[12]
                                bordro1.temmuz_gelir_vergisi=data[13]
                                bordro1.temmuz_net_ucret=data[14]
                                bordro1.temmuz_isveren_sgk_kesintisi=data[15]
                                bordro1.temmuz_isveren_issizlik_kesintisi=data[16]
                                bordro1.temmuz_toplam_sgk_kesintisi=data[17]
                                bordro1.temmuz_sgk_istisnasi=data[18]
                                bordro1.temmuz_odenecek_sgk=data[19]
                                bordro1.temmuz_odenecek_gelir_vergisi=data[21]
                                bordro1.temmuz_odenecek_damga_vergisi=data[22]
                                bordro1.temmuz_istisna_oncesi_damga=data[23]
                                bordro1.temmuz_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.temmuz_toplam_maliyet=data[25]
                                bordro1.temmuz_vergi_dilimi=data[26]
                                bordro1.temmuz_gelir_vergisi_istisnasi=data[27]
                                bordro1.temmuz_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="agustos":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.agustos_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.agustos_brut=data[0]
                                bordro1.agustos_calisilan_gun=data[1]
                                bordro1.agustos_arge_gun=data[2]
                                bordro1.agustos_bordroyaesasbrut=data[3]
                                bordro1.agustos_sgk_matrahi=data[4]
                                bordro1.agustos_sgk_kesintisi=data[5]
                                bordro1.agustos_issizlik_kesintisi=data[6]
                                bordro1.agustos_vergi_matrahi=data[7]
                                bordro1.agustos_kumulatif_vergi=data[8]
                                bordro1.agustos_istisna_oncesi_gelir=data[9]
                                bordro1.agustos_kumulatif_asgari_ucret=data[10]
                                bordro1.agustos_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.agustos_damga_vergisi=data[12]
                                bordro1.agustos_gelir_vergisi=data[13]
                                bordro1.agustos_net_ucret=data[14]
                                bordro1.agustos_isveren_sgk_kesintisi=data[15]
                                bordro1.agustos_isveren_issizlik_kesintisi=data[16]
                                bordro1.agustos_toplam_sgk_kesintisi=data[17]
                                bordro1.agustos_sgk_istisnasi=data[18]
                                bordro1.agustos_odenecek_sgk=data[19]
                                bordro1.agustos_odenecek_gelir_vergisi=data[21]
                                bordro1.agustos_odenecek_damga_vergisi=data[22]
                                bordro1.agustos_istisna_oncesi_damga=data[23]
                                bordro1.agustos_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.agustos_toplam_maliyet=data[25]
                                bordro1.agustos_vergi_dilimi=data[26]
                                bordro1.agustos_gelir_vergisi_istisnasi=data[27]
                                bordro1.agustos_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="eylul":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.eylul_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.eylul_brut=data[0]
                                bordro1.eylul_calisilan_gun=data[1]
                                bordro1.eylul_arge_gun=data[2]
                                bordro1.eylul_bordroyaesasbrut=data[3]
                                bordro1.eylul_sgk_matrahi=data[4]
                                bordro1.eylul_sgk_kesintisi=data[5]
                                bordro1.eylul_issizlik_kesintisi=data[6]
                                bordro1.eylul_vergi_matrahi=data[7]
                                bordro1.eylul_kumulatif_vergi=data[8]
                                bordro1.eylul_istisna_oncesi_gelir=data[9]
                                bordro1.eylul_kumulatif_asgari_ucret=data[10]
                                bordro1.eylul_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.eylul_damga_vergisi=data[12]
                                bordro1.eylul_gelir_vergisi=data[13]
                                bordro1.eylul_net_ucret=data[14]
                                bordro1.eylul_isveren_sgk_kesintisi=data[15]
                                bordro1.eylul_isveren_issizlik_kesintisi=data[16]
                                bordro1.eylul_toplam_sgk_kesintisi=data[17]
                                bordro1.eylul_sgk_istisnasi=data[18]
                                bordro1.eylul_odenecek_sgk=data[19]
                                bordro1.eylul_odenecek_gelir_vergisi=data[21]
                                bordro1.eylul_odenecek_damga_vergisi=data[22]
                                bordro1.eylul_istisna_oncesi_damga=data[23]
                                bordro1.eylul_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.eylul_toplam_maliyet=data[25]
                                bordro1.eylul_vergi_dilimi=data[26]
                                bordro1.eylul_gelir_vergisi_istisnasi=data[27]
                                bordro1.eylul_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="ekim":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.ekim_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.ekim_brut=data[0]
                                bordro1.ekim_calisilan_gun=data[1]
                                bordro1.ekim_arge_gun=data[2]
                                bordro1.ekim_bordroyaesasbrut=data[3]
                                bordro1.ekim_sgk_matrahi=data[4]
                                bordro1.ekim_sgk_kesintisi=data[5]
                                bordro1.ekim_issizlik_kesintisi=data[6]
                                bordro1.ekim_vergi_matrahi=data[7]
                                bordro1.ekim_kumulatif_vergi=data[8]
                                bordro1.ekim_istisna_oncesi_gelir=data[9]
                                bordro1.ekim_kumulatif_asgari_ucret=data[10]
                                bordro1.ekim_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.ekim_damga_vergisi=data[12]
                                bordro1.ekim_gelir_vergisi=data[13]
                                bordro1.ekim_net_ucret=data[14]
                                bordro1.ekim_isveren_sgk_kesintisi=data[15]
                                bordro1.ekim_isveren_issizlik_kesintisi=data[16]
                                bordro1.ekim_toplam_sgk_kesintisi=data[17]
                                bordro1.ekim_sgk_istisnasi=data[18]
                                bordro1.ekim_odenecek_sgk=data[19]
                                bordro1.ekim_odenecek_gelir_vergisi=data[21]
                                bordro1.ekim_odenecek_damga_vergisi=data[22]
                                bordro1.ekim_istisna_oncesi_damga=data[23]
                                bordro1.ekim_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.ekim_toplam_maliyet=data[25]
                                bordro1.ekim_vergi_dilimi=data[26]
                                bordro1.ekim_gelir_vergisi_istisnasi=data[27]
                                bordro1.ekim_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="kasim":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.kasim_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.kasim_brut=data[0]
                                bordro1.kasim_calisilan_gun=data[1]
                                bordro1.kasim_arge_gun=data[2]
                                bordro1.kasim_bordroyaesasbrut=data[3]
                                bordro1.kasim_sgk_matrahi=data[4]
                                bordro1.kasim_sgk_kesintisi=data[5]
                                bordro1.kasim_issizlik_kesintisi=data[6]
                                bordro1.kasim_vergi_matrahi=data[7]
                                bordro1.kasim_kumulatif_vergi=data[8]
                                bordro1.kasim_istisna_oncesi_gelir=data[9]
                                bordro1.kasim_kumulatif_asgari_ucret=data[10]
                                bordro1.kasim_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.kasim_damga_vergisi=data[12]
                                bordro1.kasim_gelir_vergisi=data[13]
                                bordro1.kasim_net_ucret=data[14]
                                bordro1.kasim_isveren_sgk_kesintisi=data[15]
                                bordro1.kasim_isveren_issizlik_kesintisi=data[16]
                                bordro1.kasim_toplam_sgk_kesintisi=data[17]
                                bordro1.kasim_sgk_istisnasi=data[18]
                                bordro1.kasim_odenecek_sgk=data[19]
                                bordro1.kasim_odenecek_gelir_vergisi=data[21]
                                bordro1.kasim_odenecek_damga_vergisi=data[22]
                                bordro1.kasim_istisna_oncesi_damga=data[23]
                                bordro1.kasim_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.kasim_toplam_maliyet=data[25]
                                bordro1.kasim_vergi_dilimi=data[26]
                                bordro1.kasim_gelir_vergisi_istisnasi=data[27]
                                bordro1.kasim_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="aralik":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.aralik_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.aralik_brut=data[0]
                                bordro1.aralik_calisilan_gun=data[1]
                                bordro1.aralik_arge_gun=data[2]
                                bordro1.aralik_bordroyaesasbrut=data[3]
                                bordro1.aralik_sgk_matrahi=data[4]
                                bordro1.aralik_sgk_kesintisi=data[5]
                                bordro1.aralik_issizlik_kesintisi=data[6]
                                bordro1.aralik_vergi_matrahi=data[7]
                                bordro1.aralik_kumulatif_vergi=data[8]
                                bordro1.aralik_istisna_oncesi_gelir=data[9]
                                bordro1.aralik_kumulatif_asgari_ucret=data[10]
                                bordro1.aralik_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.aralik_damga_vergisi=data[12]
                                bordro1.aralik_gelir_vergisi=data[13]
                                bordro1.aralik_net_ucret=data[14]
                                bordro1.aralik_isveren_sgk_kesintisi=data[15]
                                bordro1.aralik_isveren_issizlik_kesintisi=data[16]
                                bordro1.aralik_toplam_sgk_kesintisi=data[17]
                                bordro1.aralik_sgk_istisnasi=data[18]
                                bordro1.aralik_odenecek_sgk=data[19]
                                bordro1.aralik_odenecek_gelir_vergisi=data[21]
                                bordro1.aralik_odenecek_damga_vergisi=data[22]
                                bordro1.aralik_istisna_oncesi_damga=data[23]
                                bordro1.aralik_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.aralik_toplam_maliyet=data[25]
                                bordro1.aralik_vergi_dilimi=data[26]
                                bordro1.aralik_gelir_vergisi_istisnasi=data[27]
                                bordro1.aralik_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()

                        else:
                            print("maas yok")


            if "cikis" in request.POST:
                for i in range(1,len(employees)+1):
                    if request.POST.get("inputc"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputc"+str(employees[i-1].id)+""))!=0:
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma_kodu=request.POST.get("inputc"+str(employees[i-1].id)+""))
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma=True)
                    if request.POST.get("inputb"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputb"+str(employees[i-1].id)+""))!=0:
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma_tarihi=request.POST.get("inputb"+str(employees[i-1].id)+""))
                    if request.POST.get("inputa"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputa"+str(employees[i-1].id)+""))!=0:
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma_nedeni=request.POST.get("inputa"+str(employees[i-1].id)+""))
                    
                         
            if form.is_valid():
                for i in range(1,len(employees)+1):               
                    if "pdf"+str(employees[i-1].id) in request.POST:
                        if maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).exists():
                            maas1=maas.objects.get(calisan_id=employees[i-1],yil=date.today().year)
                            aylar=form.cleaned_data.get("aylar")
                            print(aylar)
                            bordro1=bordro.objects.get(maas_id=maas1.id)
                            calisan1=calisan.objects.get(id=bordro1.calisan_id_id)
                            sirket1=sirket.objects.get(id=employees[i-1].calisan_sirket_id_id)
                            buffer=io.BytesIO()
                            pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

                            p=canvas.Canvas(buffer)
                            p.setFont('Vera', 5)
                            x=2.5
                            y=19
                            p.setPageSize( landscape(A4) )

                            response=FileResponse(content_type ='application/ms-excel')
                            response['Content-Disposition'] = 'attachment; filename="bordro.xls"'
                            wb=xlwt.Workbook(encoding='utf-8')
                            ws=wb.add_sheet('Bordro')
                            row_num=0
                            font_style=xlwt.XFStyle()
                            font_style.font.bold=True

                            p.line(1*cm, (y+1)*cm, 28.5*cm, (y+1)*cm)#üst çizgi
                            p.drawString(2*cm, (y+0.7)*cm, "Firma Adı")
                            p.drawString(5.2*cm, (y+0.7)*cm, sirket1.sirket_adi)
                            p.line(1*cm, (y+0.5)*cm, 28.5*cm, (y+0.5)*cm)#üstün altı
                            p.line(1*cm, (y+0)*cm, 28.5*cm, (y+0)*cm)#alt çizgi
                            p.drawString(2*cm, (y+0.2)*cm, "Sgk İşyeri Numarası")
                            p.line(1*cm, (y-(0.5))*cm, 28.5*cm, (y-(0.5))*cm)#sağ çizgi
                            p.drawString(2*cm, (y-0.3)*cm, "Adres")
                            p.drawString(5.2*cm, (y-0.3)*cm, sirket1.sirket_adres)
                            p.line(1*cm, (y-1)*cm, 28.5*cm, (y-1)*cm)#sağ çizgi
                            p.drawString(2*cm, (y-0.8)*cm, "Vergi Dairesi")
                            p.drawString(5.2*cm, (y-0.8)*cm, sirket1.sirket_vergi_dairesi.vd_adi)
                            p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#sağ çizgi
                            p.drawString(2*cm, (y-1.3)*cm, "Vergi Numarası")
                            p.drawString(5.2*cm, (y-1.3)*cm, sirket1.sirket_vergi_numarasi)
                            p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
                            p.drawString(2*cm, (y-1.8)*cm, "Mersis Numarası")
                            p.drawString(5.2*cm, (y-1.8)*cm, sirket1.sirket_mersis_no)
                            p.line(1*cm, (y-2)*cm, 1*cm, (y+1)*cm)#sol çizgi
                            p.line(5*cm, (y-2)*cm, 5*cm, (y+1)*cm)#sağ çizgi
                            p.line(28.5*cm, (y-2)*cm, 28.5*cm, (y+1)*cm)#sağ çizgi
                            ## üst taraf
                            y=y-2
                            p.line(1*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#üst çizgi
                            p.drawString(1.1*cm, (y-1)*cm, "Ad-Soyad")
                            p.drawString(1.1*cm, (y-1.3)*cm, "Tc Kimlik No")
                            if len(""+calisan1.calisan_adi+" "+calisan1.calisan_soyadi+"") <= 19:
                                p.setFont('Vera', 4)
                                p.drawString(1.1*cm, (y-1.8)*cm, calisan1.calisan_adi + " " + calisan1.calisan_soyadi)
                            else:
                                p.setFont('Vera', 4)
                                p.drawString(1.1*cm, (y-1.7)*cm, calisan1.calisan_adi)
                                p.drawString(1.1*cm, (y-1.9)*cm, calisan1.calisan_soyadi)
                            p.setFont('Vera', 5)
                            p.drawString(1.1*cm, (y-2.3)*cm, calisan1.calisan_tc)
                            p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#üstün altı
                            p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
                            p.line(1*cm, (y-2.5)*cm, 28.5*cm, (y-2.5)*cm)#sol çizgi
                            p.line(1*cm, (y-2.5)*cm, 1*cm, (y-0.7)*cm)#sağ çizgi
                            p.line(28.5*cm, (y-2.5)*cm, 28.5*cm, (y-0.7)*cm)#sağ çizgi
                            p.line(2.8*cm, (y-2.5)*cm, 2.8*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(2.9*cm, (y-1)*cm, "Kanun No")
                            p.drawString(2.9*cm, (y-1.3)*cm, "Prim Günü")
                            if aylar[0] == 'ocak':
                                if bordro1.ocak_kanun_no=="pick1":
                                    p.drawString(2.9*cm, (y-1.8)*cm, "Standart")
                                else:
                                    p.drawString(2.9*cm, (y-1.8)*cm, bordro1.ocak_kanun_no)

                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi1))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ocak_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ocak_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ocak_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ocak_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ocak_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ocak_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ocak_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ocak_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ocak_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ocak_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ocak_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ocak_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ocak_damga_vergisi_istisnasi))
                            elif aylar[0] == "subat":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.subat_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi2))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.subat_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.subat_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.subat_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.subat_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.subat_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.subat_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.subat_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.subat_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.subat_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.subat_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.subat_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.subat_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.subat_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.subat_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.subat_damga_vergisi_istisnasi))
                            elif aylar[0] == "mart":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.mart_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi3))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.mart_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.mart_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.mart_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.mart_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.mart_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.mart_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.mart_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.mart_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.mart_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.mart_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.mart_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.mart_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.mart_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.mart_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.mart_damga_vergisi_istisnasi))
                            elif aylar[0] == "nisan":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.nisan_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi4))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.nisan_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.nisan_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.nisan_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.nisan_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.nisan_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.nisan_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.nisan_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.nisan_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.nisan_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.nisan_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.nisan_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.nisan_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.nisan_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.nisan_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.nisan_damga_vergisi_istisnasi))
                            elif aylar[0] == "mayis":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.mayis_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi5))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.mayis_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.mayis_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.mayis_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.mayis_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.mayis_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.mayis_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.mayis_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.mayis_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.mayis_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.mayis_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.mayis_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.mayis_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.mayis_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.mayis_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.mayis_damga_vergisi_istisnasi))
                            elif aylar[0] == "haziran":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.haziran_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi6))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.haziran_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.haziran_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.haziran_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.haziran_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.haziran_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.haziran_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.haziran_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.haziran_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.haziran_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.haziran_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.haziran_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.haziran_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.haziran_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.haziran_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.haziran_damga_vergisi_istisnasi))
                            elif aylar[0] == "temmuz":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.temmuz_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi7))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.temmuz_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.temmuz_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.temmuz_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.temmuz_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.temmuz_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.temmuz_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.temmuz_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.temmuz_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.temmuz_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.temmuz_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.temmuz_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.temmuz_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.temmuz_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.temmuz_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.temmuz_damga_vergisi_istisnasi))
                            elif aylar[0] == "agustos":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.agustos_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi8))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.agustos_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.agustos_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.agustos_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.agustos_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.agustos_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.agustos_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.agustos_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.agustos_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.agustos_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.agustos_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.agustos_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.agustos_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.agustos_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.agustos_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.agustos_damga_vergisi_istisnasi))
                            elif aylar[0] == "eylul":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.eylul_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi9))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.eylul_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.eylul_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.eylul_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.eylul_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.eylul_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.eylul_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.eylul_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.eylul_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.eylul_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.eylul_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.eylul_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.eylul_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.eylul_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.eylul_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.eylul_damga_vergisi_istisnasi))
                            elif aylar[0] == "ekim":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.ekim_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi10))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ekim_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ekim_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ekim_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ekim_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ekim_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ekim_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ekim_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ekim_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ekim_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ekim_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ekim_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ekim_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ekim_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ekim_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ekim_damga_vergisi_istisnasi))
                            elif aylar[0] == "kasim":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.kasim_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi11))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.kasim_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.kasim_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.kasim_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.kasim_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.kasim_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.kasim_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.kasim_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.kasim_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.kasim_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.kasim_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.kasim_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.kasim_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.kasim_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.kasim_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.kasim_damga_vergisi_istisnasi))
                            elif aylar[0] == "aralik":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.aralik_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi12))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.aralik_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.aralik_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.aralik_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.aralik_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.aralik_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.aralik_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.aralik_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.aralik_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.aralik_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.aralik_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.aralik_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.aralik_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.aralik_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.aralik_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.aralik_damga_vergisi_istisnasi))
                            p.line(4*cm, (y-2.5)*cm, 4*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(4.1*cm, (y-1)*cm, "Brüt Ücret")
                            p.drawString(4.1*cm, (y-1.3)*cm, "Sair Öd.")

                            p.line(5.8*cm, (y-2.5)*cm, 5.8*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(5.9*cm, (y-1)*cm, "Sair Öd.2")
                            p.drawString(5.9*cm, (y-1.3)*cm, "Sair Öd.3")
                            p.line(7.3*cm, (y-2.5)*cm, 7.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(7.4*cm, (y-1)*cm, "Fazla Mesai")
                            p.drawString(7.4*cm, (y-1.3)*cm, "Kesinti 1")
                            p.line(9*cm, (y-2.5)*cm, 9*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(9.1*cm, (y-1)*cm, "Kesinti 2")
                            p.drawString(9.1*cm, (y-1.3)*cm, "Kesinti 3")
                            p.line(10.3*cm, (y-2.5)*cm, 10.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(10.4*cm, (y-1)*cm, "Toplam Brüt")
                            p.drawString(10.4*cm, (y-1.3)*cm, "SGK İşçi Payı")

                            p.line(12.3*cm, (y-2.5)*cm, 12.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(12.4*cm, (y-1)*cm, "SGK İşçi İşz.")
                            p.drawString(12.4*cm, (y-1.3)*cm, "Küm. Vergi M.")

                            p.line(13.9*cm, (y-2.5)*cm, 13.9*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(14*cm, (y-1)*cm, "Vergi Matrahı")
                            p.drawString(14*cm, (y-1.3)*cm, "Gelir Vergisi")

                            p.line(15.3*cm, (y-2.5)*cm, 15.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(15.4*cm, (y-1)*cm, "Asgari Ü. Gelir V. İst.")
                            p.drawString(15.4*cm, (y-1.3)*cm, "Kalan Gelir Vergisi")

                            p.line(17.9*cm, (y-2.5)*cm, 17.9*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(18*cm, (y-1)*cm, "Damga Vergisi")
                            p.drawString(18*cm, (y-1.3)*cm, "Net Ücret")

                            p.line(21*cm, (y-2.5)*cm, 21*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(21.1*cm, (y-1.3)*cm, "SGK İsveren Primi")
                            p.drawString(21.1*cm, (y-1)*cm, "SGK İşveren İşsizlik Primi")

                            p.line(23.8*cm, (y-2.5)*cm, 23.8*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(23.9*cm, (y-1.3)*cm, "Gelir Vergisi İstisnası")
                            p.drawString(23.9*cm, (y-1)*cm, "Damga Vergisi İstisnası")

                            p.line(26.4*cm, (y-2.5)*cm, 26.4*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(26.5*cm, (y-1.3)*cm, "Sgk Prim İstisnası")
                            p.drawString(26.5*cm, (y-1)*cm, "Sgk İşsizlik Prim İst.")
                            #orta kısım
                            y=y-7
                            p.line(1*cm, (y-0.7)*cm, 5.25*cm, (y-0.7)*cm)#üst çizgi
                            p.line(5.85*cm, (y-0.7)*cm, 10.1*cm, (y-0.7)*cm)#alt çizgi
                            p.line(10.7*cm, (y-0.7)*cm, 14.95*cm, (y-0.7)*cm)#alt çizgi
                            p.line(15.55*cm, (y-0.7)*cm, 19.8*cm, (y-0.7)*cm)#alt çizgi
                            p.line(20.4*cm, (y-0.7)*cm, 24.65*cm, (y-0.7)*cm)#alt çizgi
                            p.line(25.25*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#alt çizgi
                            p.line(1*cm, (y-0.7)*cm, 1*cm, (y-9)*cm)#üst çizgi
                            p.line(5.25*cm, (y-0.7)*cm, 5.25*cm, (y-9)*cm)#üst çizgi
                            p.line(5.85*cm, (y-0.7)*cm, 5.85*cm, (y-9)*cm)#üst çizgi
                            p.line(10.1*cm, (y-0.7)*cm, 10.1*cm, (y-9)*cm)#üst çizgi
                            p.line(10.7*cm, (y-0.7)*cm, 10.7*cm, (y-9)*cm)#üst çizgi
                            p.line(14.95*cm, (y-0.7)*cm, 14.95*cm, (y-9)*cm)#üst çizgi
                            p.line(15.55*cm, (y-0.7)*cm, 15.55*cm, (y-9)*cm)#üst çizgi
                            p.line(19.8*cm, (y-0.7)*cm, 19.8*cm, (y-9)*cm)#üst çizgi
                            p.line(20.4*cm, (y-0.7)*cm, 20.4*cm, (y-9)*cm)#üst çizgi
                            p.line(24.65*cm, (y-0.7)*cm, 24.65*cm, (y-9)*cm)#üst çizgi
                            p.line(25.25*cm, (y-0.7)*cm, 25.25*cm, (y-9)*cm)#üst çizgi
                            p.line(28.5*cm, (y-0.7)*cm, 28.5*cm, (y-9)*cm)#üst çizgi
                            p.line(1*cm, (y-9)*cm, 5.25*cm, (y-9)*cm)
                            p.drawString(2.6*cm, (y-1.1)*cm, "Brüt Toplam")
                            p.line(5.85*cm, (y-9)*cm, 10.1*cm, (y-9)*cm)
                            p.drawString(7.8*cm, (y-1.1)*cm, "SGK")
                            p.line(10.7*cm, (y-9)*cm, 14.95*cm, (y-9)*cm)
                            p.drawString(12.3*cm, (y-1.1)*cm, "Gelir Vergisi")
                            p.line(15.55*cm, (y-9)*cm, 19.8*cm, (y-9)*cm)
                            p.drawString(17.1*cm, (y-1.1)*cm, "Damga Vergisi")
                            p.line(20.4*cm, (y-9)*cm, 24.65*cm, (y-9)*cm)
                            p.drawString(22.1*cm, (y-1.1)*cm, "Net Ücret")
                            p.line(25.25*cm, (y-9)*cm, 28.5*cm, (y-9)*cm)
                            p.drawString(26.6*cm, (y-1.1)*cm, "Günler")
                            p.line(3*cm, (y-1.3)*cm, 3*cm, (y-9)*cm)#üst çizgi
                            p.line(8*cm, (y-1.3)*cm, 8*cm, (y-9)*cm)#üst çizgi
                            p.line(12.7*cm, (y-1.3)*cm, 12.7*cm, (y-9)*cm)#üst çizgi
                            p.line(17.6*cm, (y-1.3)*cm, 17.6*cm, (y-9)*cm)#üst çizgi
                            p.line(22.5*cm, (y-1.3)*cm, 22.5*cm, (y-9)*cm)#üst çizgi
                            p.line(26.8*cm, (y-1.3)*cm, 26.8*cm, (y-9)*cm)#üst çizgi
                            p.line(1*cm, (y-1.3)*cm, 5.25*cm, (y-1.3)*cm)
                            p.drawString(1.2*cm, (y-1.7)*cm, "Brüt Ücret")
                            p.line(5.85*cm, (y-1.3)*cm, 10.1*cm, (y-1.3)*cm)
                            p.drawString(6.1*cm, (y-1.7)*cm, "SGK İşveren Payı")
                            p.line(10.7*cm, (y-1.3)*cm, 14.95*cm, (y-1.3)*cm)
                            p.drawString(10.8*cm, (y-1.7)*cm, "Hesaplanan Gelir V.")
                            p.line(15.55*cm, (y-1.3)*cm, 19.8*cm, (y-1.3)*cm)
                            p.drawString(15.6*cm, (y-1.7)*cm, "Hesaplanan Damga V.")
                            p.line(20.4*cm, (y-1.3)*cm, 24.65*cm, (y-1.3)*cm)
                            p.drawString(20.5*cm, (y-1.7)*cm, "Asıl Ücret")
                            p.line(25.25*cm, (y-1.3)*cm, 28.5*cm, (y-1.3)*cm)
                            p.drawString(25.4*cm, (y-1.7)*cm, "Çalışma Günü")
                            p.line(1*cm, (y-2)*cm, 5.25*cm, (y-2)*cm)
                            p.drawString(1.2*cm, (y-2.5)*cm, "Sair Ödeme1")
                            p.line(5.85*cm, (y-2)*cm, 10.1*cm, (y-2)*cm)
                            p.drawString(6.1*cm, (y-2.5)*cm, "Sgk İşçi Payı")
                            p.line(10.7*cm, (y-2)*cm, 14.95*cm, (y-2)*cm)
                            p.drawString(10.8*cm, (y-2.5)*cm, "ASgari Ü. Gelir V. İst.")
                            p.line(15.55*cm, (y-2)*cm, 19.8*cm, (y-2)*cm)
                            p.drawString(15.6*cm, (y-2.5)*cm, "İst. Damga Vergisi")
                            p.line(20.4*cm, (y-2)*cm, 24.65*cm, (y-2)*cm)
                            p.drawString(20.5*cm, (y-2.5)*cm, "Fazla Mesai")
                            p.line(25.25*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)
                            p.drawString(25.4*cm, (y-2.5)*cm, "Haftasonu Günü")
                            p.line(1*cm, (y-2.7)*cm, 5.25*cm, (y-2.7)*cm)
                            p.drawString(1.2*cm, (y-3.2)*cm, "Sair Ödeme2")
                            p.line(5.85*cm, (y-2.7)*cm, 10.1*cm, (y-2.7)*cm)
                            p.drawString(6.1*cm, (y-3.2)*cm, "Sgk İşv. İşz. Payı")
                            p.line(10.7*cm, (y-2.7)*cm, 14.95*cm, (y-2.7)*cm)
                            p.drawString(10.8*cm, (y-3.2)*cm, "Terkin E. Gelir V.")
                            p.line(15.55*cm, (y-2.7)*cm, 19.8*cm, (y-2.7)*cm)
                            p.line(20.4*cm, (y-2.7)*cm, 24.65*cm, (y-2.7)*cm)
                            p.drawString(20.5*cm, (y-3.2)*cm, "Sair Ödeme 1")
                            p.line(25.25*cm, (y-2.7)*cm, 28.5*cm, (y-2.7)*cm)
                            p.drawString(25.5*cm, (y-3.2)*cm, "Genel Tatil")
                            p.line(1*cm, (y-3.4)*cm, 5.25*cm, (y-3.4)*cm)
                            p.drawString(1.2*cm, (y-3.9)*cm, "Sair Ödeme3")
                            p.line(5.85*cm, (y-3.4)*cm, 10.1*cm, (y-3.4)*cm)
                            p.drawString(6.1*cm, (y-3.9)*cm, "Sgk İşçi İşz. Payı")
                            p.line(10.7*cm, (y-3.4)*cm, 14.95*cm, (y-3.4)*cm)

                            p.line(20.4*cm, (y-3.4)*cm, 24.65*cm, (y-3.4)*cm)
                            p.drawString(20.5*cm, (y-3.9)*cm, "Sair Ödeme 2")
                            p.line(25.25*cm, (y-3.4)*cm, 28.5*cm, (y-3.4)*cm)
                            p.drawString(25.5*cm, (y-3.9)*cm, "Yıllık İzin")
                            p.line(1*cm, (y-4.1)*cm, 5.25*cm, (y-4.1)*cm)
                            p.drawString(1.2*cm, (y-4.6)*cm, "Fazla Mesai")
                            p.line(5.85*cm, (y-4.1)*cm, 10.1*cm, (y-4.1)*cm)
                            p.drawString(6.1*cm, (y-4.6)*cm, "Sgk Prim Desteği İst.")
                            p.line(20.4*cm, (y-4.1)*cm, 24.65*cm, (y-4.1)*cm)
                            p.drawString(20.5*cm, (y-4.6)*cm, "Sair Ödeme 3")
                            p.line(25.25*cm, (y-4.1)*cm, 28.5*cm, (y-4.1)*cm)
                            p.drawString(25.5*cm, (y-4.6)*cm, "Sıhhi İzin")
                            p.line(1*cm, (y-4.8)*cm, 5.25*cm, (y-4.8)*cm)
                            p.drawString(1.2*cm, (y-5.3)*cm, "Kesinti 1")
                            p.line(5.85*cm, (y-4.8)*cm, 10.1*cm, (y-4.8)*cm)
                            p.drawString(6.1*cm, (y-5.3)*cm, "Sgk İşs. Prim Des. İst.")
                            p.line(20.4*cm, (y-4.8)*cm, 24.65*cm, (y-4.8)*cm)
                            p.drawString(20.5*cm, (y-5.3)*cm, "Kesinti 1")
                            p.line(25.25*cm, (y-4.8)*cm, 28.5*cm, (y-4.8)*cm)
                            p.drawString(25.5*cm, (y-5.3)*cm, "Ucretsiz İzin")
                            p.line(1*cm, (y-5.5)*cm, 5.25*cm, (y-5.5)*cm)
                            p.drawString(1.2*cm, (y-6)*cm, "Kesinti 2")
                            p.line(5.85*cm, (y-5.5)*cm, 10.1*cm, (y-5.5)*cm)
                            p.line(20.4*cm, (y-5.5)*cm, 24.65*cm, (y-5.5)*cm)
                            p.drawString(20.5*cm, (y-6)*cm, "Kesinti 2")
                            p.line(25.25*cm, (y-5.5)*cm, 28.5*cm, (y-5.5)*cm)
                            p.drawString(25.5*cm, (y-6)*cm, "Ücretli İzin")
                            p.line(1*cm, (y-6.2)*cm, 5.25*cm, (y-6.2)*cm)
                            p.drawString(1.2*cm, (y-6.7)*cm, "Kesinti 3")
                            p.line(20.4*cm, (y-6.2)*cm, 24.65*cm, (y-6.2)*cm)
                            p.drawString(20.5*cm, (y-6.7)*cm, "Kesinti 3")
                            p.line(25.25*cm, (y-6.2)*cm, 28.5*cm, (y-6.2)*cm)
                            p.drawString(25.5*cm, (y-6.7)*cm, "Mazeret İzin")
                            p.line(1*cm, (y-6.9)*cm, 5.25*cm, (y-6.9)*cm)
                            p.line(20.4*cm, (y-6.9)*cm, 24.65*cm, (y-6.9)*cm)
                            p.line(25.25*cm, (y-6.9)*cm, 28.5*cm, (y-6.9)*cm)
                            p.drawString(25.5*cm, (y-7.4)*cm, "Prim Günü")

                            p.line(1*cm, (y-7.6)*cm, 5.25*cm, (y-7.6)*cm)

                            p.line(5.85*cm, (y-7.6)*cm, 10.1*cm, (y-7.6)*cm)

                            p.line(10.7*cm, (y-7.6)*cm, 14.95*cm, (y-7.6)*cm)

                            p.line(15.55*cm, (y-7.6)*cm, 19.8*cm, (y-7.6)*cm)

                            p.line(20.4*cm, (y-7.6)*cm, 24.65*cm, (y-7.6)*cm)

                            p.line(25.25*cm, (y-7.6)*cm, 28.5*cm, (y-7.6)*cm)
                            p.line(1*cm, (y-8.3)*cm, 5.25*cm, (y-8.3)*cm)
                            p.drawString(1.2*cm, (y-8.7)*cm, "Brüt Toplam")
                            p.line(5.85*cm, (y-8.3)*cm, 10.1*cm, (y-8.3)*cm)
                            p.drawString(10.7*cm, (y-8.7)*cm, "Ödenecek SGK Primi")

                            p.line(10.7*cm, (y-8.3)*cm, 14.95*cm, (y-8.3)*cm)
                            p.drawString(15.55*cm, (y-8.7)*cm, "Ödenecek Gelir V.")
                            p.line(15.55*cm, (y-8.3)*cm, 19.8*cm, (y-8.3)*cm)
                            p.drawString(20.5*cm, (y-8.7)*cm, "Ödenecek Damga V.")
                            p.line(20.4*cm, (y-8.3)*cm, 24.65*cm, (y-8.3)*cm)
                            p.drawString(25.5*cm, (y-8.7)*cm, "Net Ödenecek Ücret")
                            p.line(25.25*cm, (y-8.3)*cm, 28.5*cm, (y-8.3)*cm)

                            tur=form.cleaned_data.get('export')
                            print(tur)

                            if tur == "pdf":
                                p.showPage()
                                p.save()
                                buffer.seek(0)
                                return FileResponse(buffer, as_attachment=False, filename='bordro.pdf')
                            elif tur == "xls":
                                output = io.BytesIO()
                                wb.save(output)
                                output.seek(0)
                                return FileResponse(output, as_attachment=False, filename='bordro.xls')
                            else:
                                return HttpResponseNotFound("404")

            return redirect(reverse('user:subelist', kwargs={'id':id}))


    context={
        'subes':sube1,
        'company':company,
        'uyelik':uyelik,
        'employees':employees1,
        'calisantab':calisantab,
        'sirketid':id,
        'deneme':deneme,
        'aylar':aylar,
        'bordro':deneme1,
        'month':month,
        'form':form,
        'maxuser':maxuser,
        'calisansayi':calisansayi,
        'uyelik':uyelik,
        'uyelik1':uyelik1,
        'sirketedit':False,
        'subeedit':True,

    }
    return render(request,'subelist.html',context)

def passiveemployee(request,id):
    sube1=sube.objects.filter(sube_sirket_id=id)
    aylar=employeelistaylar(request.POST or None)
    form=denemeform(request.POST or None)
    if (sirket.objects.filter(id=id)).exists():
        company=sirket.objects.get(id=id)
    else:
        return handler404(request,exception=404)
    if( request.user.groups.filter(name='mali_musavir').exists() or request.user.groups.filter(name='admin').exists() or request.user.groups.filter(name='muhasebe').exists()  ):
        employees1=[]
        deneme=[]
        deneme1=[]
        count=0
        for i in sube1:
            employees1.append(calisan.objects.filter(calisan_sube_id=i.id,calisan_isten_ayrilma=True).order_by('calisan_soyadi'))


        if employees1:
            for i in employees1:
                for k in i:

                    if maas.objects.filter(calisan_id=k.id,yil=date.today().year).exists():
                        deneme.append(maas.objects.filter(calisan_id=k.id,yil=date.today().year))
                    count=count+1

        if deneme :
            for i in deneme:

                if bordro.objects.filter(maas_id=i[0].id,).exists():
                    deneme1.append(bordro.objects.filter(maas_id=i[0].id))

        calisantab=False
        month=datetime.now().month
        maxuser=subs.objects.filter(id=company.sirket_uyelik.id)
        maxuser=maxuser[0].subs_maksimum_calisan
        calisansayi=count

        uyelik=True
        uyelik1=True
        if subs.objects.filter(id=company.sirket_uyelik_id).exists():
            subs1=subs.objects.get(id=company.sirket_uyelik_id)
        if subs1.subs_baslangic_tarihi + timedelta(subs1.subs_gun_sayisi)<datetime.now().date():
             subs1.subs_aktiflik=False
             subs1.save()
        if subs.objects.get(id=company.sirket_uyelik_id).subs_aktiflik==False:
            uyelik=False
        if subs.objects.get(id=company.sirket_uyelik_id).subs_maksimum_calisan<=calisansayi:
            uyelik1=False
        if request.method == 'POST':
            employees=[]
            for i in employees1:
                for k in i:
                    employees.append(k)
            if employees :
                for i in employees:
                    
                        if maas.objects.filter(calisan_id=i,yil=date.today().year).exists():
                            deneme.append(maas.objects.filter(calisan_id=i,yil=date.today().year))
                        else:
                            deneme.append(maas.objects.none())
            if "infobutton" in request.POST:
                for i in range(1,len(employees)+1):
                    if request.POST.get("input1"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input1"+str(employees[i-1].id)+""))!=0:
                        if not request.POST.get("input1"+str(employees[i-1].id)+"").isdigit():
                            employees[i-1].calisan_adi=request.POST.get("input1"+str(employees[i-1].id)+"")
                        else:
                             messages.error(request, 'Lütfen isim alanına sayı girmeyiniz')
                             return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input2"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input2"+str(employees[i-1].id)+""))!=0:
                        if not request.POST.get("input2"+str(employees[i-1].id)+"").isdigit():
                            employees[i-1].calisan_soyadi=request.POST.get("input2"+str(employees[i-1].id)+"")
                        else:
                                messages.error(request, 'Lütfen soyisim alanına sayı girmeyiniz')
                                return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input3"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input3"+str(employees[i-1].id)+""))!=0:
                        if turkish_id_no_check(request.POST.get("input3"+str(employees[i-1].id)+"")):
                            employees[i-1].calisan_tc=request.POST.get("input3"+str(employees[i-1].id)+"")
                        else:
                            messages.error(request, 'Lütfen geçerli bir TC kimlik numarası giriniz')
                            return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input4"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input4"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_mail=request.POST.get("input4"+str(employees[i-1].id)+"")
                    if request.POST.get("input5"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input5"+str(employees[i-1].id)+""))!=0:
                        if request.POST.get("input5"+str(employees[i-1].id)+"").isdigit():
                            employees[i-1].calisan_telefon=request.POST.get("input5"+str(employees[i-1].id)+"")
                        else:
                            messages.error(request, 'Lütfen telefon alanına harf girmeyiniz')
                            return redirect(reverse('user:subelist', kwargs={'id':id}))
                    if request.POST.get("input6"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input6"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_adres=request.POST.get("input6"+str(employees[i-1].id)+"")
                    if request.POST.get("input7"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input7"+str(employees[i-1].id)+""))!=0:
                        d=request.POST.get("input7"+str(employees[i-1].id)+"")
                        employees[i-1].calisan_dogum_tarihi=d
                    if request.POST.get("input8"+str(employees[i-1].id)+"") is not None and len(request.POST.get("input8"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_ise_giris_tarihi=request.POST.get("input8"+str(employees[i-1].id)+"")
                    if request.POST.get("calisanengel"+str(employees[i-1].id)+"") is not None and len(request.POST.get("calisanengel"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_engelli=request.POST.get("calisanengel"+str(employees[i-1].id)+"")
                    if request.POST.get("calisanemekli"+str(employees[i-1].id)+"") is not None and len(request.POST.get("calisanemekli"+str(employees[i-1].id)+""))!=0:
                        print(request.POST.get("calisanemekli"+str(employees[i-1].id)+""))
                        employees[i-1].calisan_emekli=request.POST.get("calisanemekli"+str(employees[i-1].id)+"")
                    if request.POST.get("calisanogrenim"+str(employees[i-1].id)+"") is not None and len(request.POST.get("calisanogrenim"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_ogrenim_durumu=request.POST.get("calisanogrenim"+str(employees[i-1].id)+"")
                    if request.POST.get("inputiban"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputiban"+str(employees[i-1].id)+""))!=0:
                        employees[i-1].calisan_iban=request.POST.get("inputiban"+str(employees[i-1].id)+"")
                    employees[i-1].save()
                    
            if "maasbuton" in request.POST:

                for i in range(1,len(employees)+1):
                    if request.POST.get("calisantesvik"+str(employees[i-1].id)+"") is not None:
                        employees[i-1].calisan_tesvik=request.POST.get("calisantesvik"+str(employees[i-1].id)+"")
                    employees[i-1].save()

                    if request.POST.get("maas"+str(employees[i-1].id)+"") is not None and len(request.POST.get("maas"+str(employees[i-1].id)+""))!=0:

                        if maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).exists():
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(ucret=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                            ay=request.POST.get("aylar")
                            bordro1=bordro.objects.get(maas_id=maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id)
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(ucrettipi=request.POST.get("ucrettipi"+str(employees[i-1].id)+""))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(para_birimi=request.POST.get("parabirimi"+str(employees[i-1].id)+""))

                            
                            if ay=="ocak":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)

                                bordro1.ocak_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.ocak_brut=data[0]
                                bordro1.ocak_calisilan_gun=data[1]
                                bordro1.ocak_arge_gun=data[2]
                                bordro1.ocak_bordroyaesasbrut=data[3]
                                bordro1.ocak_sgk_matrahi=data[4]
                                bordro1.ocak_sgk_kesintisi=data[5]
                                bordro1.ocak_issizlik_kesintisi=data[6]
                                bordro1.ocak_vergi_matrahi=data[7]
                                bordro1.ocak_kumulatif_vergi=data[8]
                                bordro1.ocak_istisna_oncesi_gelir=data[9]
                                bordro1.ocak_kumulatif_asgari_ucret=data[10]
                                bordro1.ocak_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.ocak_damga_vergisi=data[12]
                                bordro1.ocak_gelir_vergisi=data[13]
                                bordro1.ocak_net_ucret=data[14]
                                bordro1.ocak_isveren_sgk_kesintisi=data[15]
                                bordro1.ocak_isveren_issizlik_kesintisi=data[16]
                                bordro1.ocak_toplam_sgk_kesintisi=data[17]
                                bordro1.ocak_sgk_istisnasi=data[18]
                                bordro1.ocak_odenecek_sgk=data[19]
                                bordro1.ocak_odenecek_gelir_vergisi=data[21]
                                bordro1.ocak_odenecek_damga_vergisi=data[22]
                                bordro1.ocak_istisna_oncesi_damga=data[23]
                                bordro1.ocak_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.ocak_toplam_maliyet=data[25]
                                bordro1.ocak_vergi_dilimi=data[26]
                                bordro1.ocak_gelir_vergisi_istisnasi=data[27]
                                bordro1.ocak_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="subat":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.subat_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.subat_brut=data[0]
                                bordro1.subat_calisilan_gun=data[1]
                                bordro1.subat_arge_gun=data[2]
                                bordro1.subat_bordroyaesasbrut=data[3]
                                bordro1.subat_sgk_matrahi=data[4]
                                bordro1.subat_sgk_kesintisi=data[5]
                                bordro1.subat_issizlik_kesintisi=data[6]
                                bordro1.subat_vergi_matrahi=data[7]
                                bordro1.subat_kumulatif_vergi=data[8]
                                bordro1.subat_istisna_oncesi_gelir=data[9]
                                bordro1.subat_kumulatif_asgari_ucret=data[10]
                                bordro1.subat_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.subat_damga_vergisi=data[12]
                                bordro1.subat_gelir_vergisi=data[13]
                                bordro1.subat_net_ucret=data[14]
                                bordro1.subat_isveren_sgk_kesintisi=data[15]
                                bordro1.subat_isveren_issizlik_kesintisi=data[16]
                                bordro1.subat_toplam_sgk_kesintisi=data[17]
                                bordro1.subat_sgk_istisnasi=data[18]
                                bordro1.subat_odenecek_sgk=data[19]
                                bordro1.subat_odenecek_gelir_vergisi=data[21]
                                bordro1.subat_odenecek_damga_vergisi=data[22]
                                bordro1.subat_istisna_oncesi_damga=data[23]
                                bordro1.subat_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.subat_toplam_maliyet=data[25]
                                bordro1.subat_vergi_dilimi=data[26]
                                bordro1.subat_gelir_vergisi_istisnasi=data[27]
                                bordro1.subat_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()

                            elif ay=="mart":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.mart_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.mart_brut=data[0]
                                bordro1.mart_calisilan_gun=data[1]
                                bordro1.mart_arge_gun=data[2]
                                bordro1.mart_bordroyaesasbrut=data[3]
                                bordro1.mart_sgk_matrahi=data[4]
                                bordro1.mart_sgk_kesintisi=data[5]
                                bordro1.mart_issizlik_kesintisi=data[6]
                                bordro1.mart_vergi_matrahi=data[7]
                                bordro1.mart_kumulatif_vergi=data[8]
                                bordro1.mart_istisna_oncesi_gelir=data[9]
                                bordro1.mart_kumulatif_asgari_ucret=data[10]
                                bordro1.mart_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.mart_damga_vergisi=data[12]
                                bordro1.mart_gelir_vergisi=data[13]
                                bordro1.mart_net_ucret=data[14]
                                bordro1.mart_isveren_sgk_kesintisi=data[15]
                                bordro1.mart_isveren_issizlik_kesintisi=data[16]
                                bordro1.mart_toplam_sgk_kesintisi=data[17]
                                bordro1.mart_sgk_istisnasi=data[18]
                                bordro1.mart_odenecek_sgk=data[19]
                                bordro1.mart_odenecek_gelir_vergisi=data[21]
                                bordro1.mart_odenecek_damga_vergisi=data[22]
                                bordro1.mart_istisna_oncesi_damga=data[23]
                                bordro1.mart_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.mart_toplam_maliyet=data[25]
                                bordro1.mart_vergi_dilimi=data[26]
                                bordro1.mart_gelir_vergisi_istisnasi=data[27]
                                bordro1.mart_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="nisan":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.nisan_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.nisan_brut=data[0]
                                bordro1.nisan_calisilan_gun=data[1]
                                bordro1.nisan_arge_gun=data[2]
                                bordro1.nisan_bordroyaesasbrut=data[3]
                                bordro1.nisan_sgk_matrahi=data[4]
                                bordro1.nisan_sgk_kesintisi=data[5]
                                bordro1.nisan_issizlik_kesintisi=data[6]
                                bordro1.nisan_vergi_matrahi=data[7]
                                bordro1.nisan_kumulatif_vergi=data[8]
                                bordro1.nisan_istisna_oncesi_gelir=data[9]
                                bordro1.nisan_kumulatif_asgari_ucret=data[10]
                                bordro1.nisan_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.nisan_damga_vergisi=data[12]
                                bordro1.nisan_gelir_vergisi=data[13]
                                bordro1.nisan_net_ucret=data[14]
                                bordro1.nisan_isveren_sgk_kesintisi=data[15]
                                bordro1.nisan_isveren_issizlik_kesintisi=data[16]
                                bordro1.nisan_toplam_sgk_kesintisi=data[17]
                                bordro1.nisan_sgk_istisnasi=data[18]
                                bordro1.nisan_odenecek_sgk=data[19]
                                bordro1.nisan_odenecek_gelir_vergisi=data[21]
                                bordro1.nisan_odenecek_damga_vergisi=data[22]
                                bordro1.nisan_istisna_oncesi_damga=data[23]
                                bordro1.nisan_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.nisan_toplam_maliyet=data[25]
                                bordro1.nisan_vergi_dilimi=data[26]
                                bordro1.nisan_gelir_vergisi_istisnasi=data[27]
                                bordro1.nisan_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="mayis":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.mayis_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.mayis_brut=data[0]
                                bordro1.mayis_calisilan_gun=data[1]
                                bordro1.mayis_arge_gun=data[2]
                                bordro1.mayis_bordroyaesasbrut=data[3]
                                bordro1.mayis_sgk_matrahi=data[4]
                                bordro1.mayis_sgk_kesintisi=data[5]
                                bordro1.mayis_issizlik_kesintisi=data[6]
                                bordro1.mayis_vergi_matrahi=data[7]
                                bordro1.mayis_kumulatif_vergi=data[8]
                                bordro1.mayis_istisna_oncesi_gelir=data[9]
                                bordro1.mayis_kumulatif_asgari_ucret=data[10]
                                bordro1.mayis_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.mayis_damga_vergisi=data[12]
                                bordro1.mayis_gelir_vergisi=data[13]
                                bordro1.mayis_net_ucret=data[14]
                                bordro1.mayis_isveren_sgk_kesintisi=data[15]
                                bordro1.mayis_isveren_issizlik_kesintisi=data[16]
                                bordro1.mayis_toplam_sgk_kesintisi=data[17]
                                bordro1.mayis_sgk_istisnasi=data[18]
                                bordro1.mayis_odenecek_sgk=data[19]
                                bordro1.mayis_odenecek_gelir_vergisi=data[21]
                                bordro1.mayis_odenecek_damga_vergisi=data[22]
                                bordro1.mayis_istisna_oncesi_damga=data[23]
                                bordro1.mayis_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.mayis_toplam_maliyet=data[25]
                                bordro1.mayis_vergi_dilimi=data[26]
                                bordro1.mayis_gelir_vergisi_istisnasi=data[27]
                                bordro1.mayis_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="haziran":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.haziran_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.haziran_brut=data[0]
                                bordro1.haziran_calisilan_gun=data[1]
                                bordro1.haziran_arge_gun=data[2]
                                bordro1.haziran_bordroyaesasbrut=data[3]
                                bordro1.haziran_sgk_matrahi=data[4]
                                bordro1.haziran_sgk_kesintisi=data[5]
                                bordro1.haziran_issizlik_kesintisi=data[6]
                                bordro1.haziran_vergi_matrahi=data[7]
                                bordro1.haziran_kumulatif_vergi=data[8]
                                bordro1.haziran_istisna_oncesi_gelir=data[9]
                                bordro1.haziran_kumulatif_asgari_ucret=data[10]
                                bordro1.haziran_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.haziran_damga_vergisi=data[12]
                                bordro1.haziran_gelir_vergisi=data[13]
                                bordro1.haziran_net_ucret=data[14]
                                bordro1.haziran_isveren_sgk_kesintisi=data[15]
                                bordro1.haziran_isveren_issizlik_kesintisi=data[16]
                                bordro1.haziran_toplam_sgk_kesintisi=data[17]
                                bordro1.haziran_sgk_istisnasi=data[18]
                                bordro1.haziran_odenecek_sgk=data[19]
                                bordro1.haziran_odenecek_gelir_vergisi=data[21]
                                bordro1.haziran_odenecek_damga_vergisi=data[22]
                                bordro1.haziran_istisna_oncesi_damga=data[23]
                                bordro1.haziran_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.haziran_toplam_maliyet=data[25]
                                bordro1.haziran_vergi_dilimi=data[26]
                                bordro1.haziran_gelir_vergisi_istisnasi=data[27]
                                bordro1.haziran_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="temmuz":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.temmuz_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.temmuz_brut=data[0]
                                bordro1.temmuz_calisilan_gun=data[1]
                                bordro1.temmuz_arge_gun=data[2]
                                bordro1.temmuz_bordroyaesasbrut=data[3]
                                bordro1.temmuz_sgk_matrahi=data[4]
                                bordro1.temmuz_sgk_kesintisi=data[5]
                                bordro1.temmuz_issizlik_kesintisi=data[6]
                                bordro1.temmuz_vergi_matrahi=data[7]
                                bordro1.temmuz_kumulatif_vergi=data[8]
                                bordro1.temmuz_istisna_oncesi_gelir=data[9]
                                bordro1.temmuz_kumulatif_asgari_ucret=data[10]
                                bordro1.temmuz_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.temmuz_damga_vergisi=data[12]
                                bordro1.temmuz_gelir_vergisi=data[13]
                                bordro1.temmuz_net_ucret=data[14]
                                bordro1.temmuz_isveren_sgk_kesintisi=data[15]
                                bordro1.temmuz_isveren_issizlik_kesintisi=data[16]
                                bordro1.temmuz_toplam_sgk_kesintisi=data[17]
                                bordro1.temmuz_sgk_istisnasi=data[18]
                                bordro1.temmuz_odenecek_sgk=data[19]
                                bordro1.temmuz_odenecek_gelir_vergisi=data[21]
                                bordro1.temmuz_odenecek_damga_vergisi=data[22]
                                bordro1.temmuz_istisna_oncesi_damga=data[23]
                                bordro1.temmuz_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.temmuz_toplam_maliyet=data[25]
                                bordro1.temmuz_vergi_dilimi=data[26]
                                bordro1.temmuz_gelir_vergisi_istisnasi=data[27]
                                bordro1.temmuz_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="agustos":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.agustos_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.agustos_brut=data[0]
                                bordro1.agustos_calisilan_gun=data[1]
                                bordro1.agustos_arge_gun=data[2]
                                bordro1.agustos_bordroyaesasbrut=data[3]
                                bordro1.agustos_sgk_matrahi=data[4]
                                bordro1.agustos_sgk_kesintisi=data[5]
                                bordro1.agustos_issizlik_kesintisi=data[6]
                                bordro1.agustos_vergi_matrahi=data[7]
                                bordro1.agustos_kumulatif_vergi=data[8]
                                bordro1.agustos_istisna_oncesi_gelir=data[9]
                                bordro1.agustos_kumulatif_asgari_ucret=data[10]
                                bordro1.agustos_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.agustos_damga_vergisi=data[12]
                                bordro1.agustos_gelir_vergisi=data[13]
                                bordro1.agustos_net_ucret=data[14]
                                bordro1.agustos_isveren_sgk_kesintisi=data[15]
                                bordro1.agustos_isveren_issizlik_kesintisi=data[16]
                                bordro1.agustos_toplam_sgk_kesintisi=data[17]
                                bordro1.agustos_sgk_istisnasi=data[18]
                                bordro1.agustos_odenecek_sgk=data[19]
                                bordro1.agustos_odenecek_gelir_vergisi=data[21]
                                bordro1.agustos_odenecek_damga_vergisi=data[22]
                                bordro1.agustos_istisna_oncesi_damga=data[23]
                                bordro1.agustos_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.agustos_toplam_maliyet=data[25]
                                bordro1.agustos_vergi_dilimi=data[26]
                                bordro1.agustos_gelir_vergisi_istisnasi=data[27]
                                bordro1.agustos_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="eylul":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.eylul_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.eylul_brut=data[0]
                                bordro1.eylul_calisilan_gun=data[1]
                                bordro1.eylul_arge_gun=data[2]
                                bordro1.eylul_bordroyaesasbrut=data[3]
                                bordro1.eylul_sgk_matrahi=data[4]
                                bordro1.eylul_sgk_kesintisi=data[5]
                                bordro1.eylul_issizlik_kesintisi=data[6]
                                bordro1.eylul_vergi_matrahi=data[7]
                                bordro1.eylul_kumulatif_vergi=data[8]
                                bordro1.eylul_istisna_oncesi_gelir=data[9]
                                bordro1.eylul_kumulatif_asgari_ucret=data[10]
                                bordro1.eylul_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.eylul_damga_vergisi=data[12]
                                bordro1.eylul_gelir_vergisi=data[13]
                                bordro1.eylul_net_ucret=data[14]
                                bordro1.eylul_isveren_sgk_kesintisi=data[15]
                                bordro1.eylul_isveren_issizlik_kesintisi=data[16]
                                bordro1.eylul_toplam_sgk_kesintisi=data[17]
                                bordro1.eylul_sgk_istisnasi=data[18]
                                bordro1.eylul_odenecek_sgk=data[19]
                                bordro1.eylul_odenecek_gelir_vergisi=data[21]
                                bordro1.eylul_odenecek_damga_vergisi=data[22]
                                bordro1.eylul_istisna_oncesi_damga=data[23]
                                bordro1.eylul_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.eylul_toplam_maliyet=data[25]
                                bordro1.eylul_vergi_dilimi=data[26]
                                bordro1.eylul_gelir_vergisi_istisnasi=data[27]
                                bordro1.eylul_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="ekim":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.ekim_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.ekim_brut=data[0]
                                bordro1.ekim_calisilan_gun=data[1]
                                bordro1.ekim_arge_gun=data[2]
                                bordro1.ekim_bordroyaesasbrut=data[3]
                                bordro1.ekim_sgk_matrahi=data[4]
                                bordro1.ekim_sgk_kesintisi=data[5]
                                bordro1.ekim_issizlik_kesintisi=data[6]
                                bordro1.ekim_vergi_matrahi=data[7]
                                bordro1.ekim_kumulatif_vergi=data[8]
                                bordro1.ekim_istisna_oncesi_gelir=data[9]
                                bordro1.ekim_kumulatif_asgari_ucret=data[10]
                                bordro1.ekim_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.ekim_damga_vergisi=data[12]
                                bordro1.ekim_gelir_vergisi=data[13]
                                bordro1.ekim_net_ucret=data[14]
                                bordro1.ekim_isveren_sgk_kesintisi=data[15]
                                bordro1.ekim_isveren_issizlik_kesintisi=data[16]
                                bordro1.ekim_toplam_sgk_kesintisi=data[17]
                                bordro1.ekim_sgk_istisnasi=data[18]
                                bordro1.ekim_odenecek_sgk=data[19]
                                bordro1.ekim_odenecek_gelir_vergisi=data[21]
                                bordro1.ekim_odenecek_damga_vergisi=data[22]
                                bordro1.ekim_istisna_oncesi_damga=data[23]
                                bordro1.ekim_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.ekim_toplam_maliyet=data[25]
                                bordro1.ekim_vergi_dilimi=data[26]
                                bordro1.ekim_gelir_vergisi_istisnasi=data[27]
                                bordro1.ekim_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="kasim":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.kasim_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.kasim_brut=data[0]
                                bordro1.kasim_calisilan_gun=data[1]
                                bordro1.kasim_arge_gun=data[2]
                                bordro1.kasim_bordroyaesasbrut=data[3]
                                bordro1.kasim_sgk_matrahi=data[4]
                                bordro1.kasim_sgk_kesintisi=data[5]
                                bordro1.kasim_issizlik_kesintisi=data[6]
                                bordro1.kasim_vergi_matrahi=data[7]
                                bordro1.kasim_kumulatif_vergi=data[8]
                                bordro1.kasim_istisna_oncesi_gelir=data[9]
                                bordro1.kasim_kumulatif_asgari_ucret=data[10]
                                bordro1.kasim_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.kasim_damga_vergisi=data[12]
                                bordro1.kasim_gelir_vergisi=data[13]
                                bordro1.kasim_net_ucret=data[14]
                                bordro1.kasim_isveren_sgk_kesintisi=data[15]
                                bordro1.kasim_isveren_issizlik_kesintisi=data[16]
                                bordro1.kasim_toplam_sgk_kesintisi=data[17]
                                bordro1.kasim_sgk_istisnasi=data[18]
                                bordro1.kasim_odenecek_sgk=data[19]
                                bordro1.kasim_odenecek_gelir_vergisi=data[21]
                                bordro1.kasim_odenecek_damga_vergisi=data[22]
                                bordro1.kasim_istisna_oncesi_damga=data[23]
                                bordro1.kasim_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.kasim_toplam_maliyet=data[25]
                                bordro1.kasim_vergi_dilimi=data[26]
                                bordro1.kasim_gelir_vergisi_istisnasi=data[27]
                                bordro1.kasim_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
                            elif ay=="aralik":
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(employees[i-1].id)+"").replace(",","."))
                                maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(employees[i-1].id)+"").replace(",","."))
                                data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                                bordro1.aralik_kanun_no=employees[i-1].calisan_tesvik
                                bordro1.aralik_brut=data[0]
                                bordro1.aralik_calisilan_gun=data[1]
                                bordro1.aralik_arge_gun=data[2]
                                bordro1.aralik_bordroyaesasbrut=data[3]
                                bordro1.aralik_sgk_matrahi=data[4]
                                bordro1.aralik_sgk_kesintisi=data[5]
                                bordro1.aralik_issizlik_kesintisi=data[6]
                                bordro1.aralik_vergi_matrahi=data[7]
                                bordro1.aralik_kumulatif_vergi=data[8]
                                bordro1.aralik_istisna_oncesi_gelir=data[9]
                                bordro1.aralik_kumulatif_asgari_ucret=data[10]
                                bordro1.aralik_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.aralik_damga_vergisi=data[12]
                                bordro1.aralik_gelir_vergisi=data[13]
                                bordro1.aralik_net_ucret=data[14]
                                bordro1.aralik_isveren_sgk_kesintisi=data[15]
                                bordro1.aralik_isveren_issizlik_kesintisi=data[16]
                                bordro1.aralik_toplam_sgk_kesintisi=data[17]
                                bordro1.aralik_sgk_istisnasi=data[18]
                                bordro1.aralik_odenecek_sgk=data[19]
                                bordro1.aralik_odenecek_gelir_vergisi=data[21]
                                bordro1.aralik_odenecek_damga_vergisi=data[22]
                                bordro1.aralik_istisna_oncesi_damga=data[23]
                                bordro1.aralik_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.aralik_toplam_maliyet=data[25]
                                bordro1.aralik_vergi_dilimi=data[26]
                                bordro1.aralik_gelir_vergisi_istisnasi=data[27]
                                bordro1.aralik_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()

                        else:
                            print("maas yok")


            if "cikis" in request.POST:
                for i in range(1,len(employees)+1):
                    if request.POST.get("inputc"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputc"+str(employees[i-1].id)+""))!=0:
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma_kodu=request.POST.get("inputc"+str(employees[i-1].id)+""))
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma=True)
                    if request.POST.get("inputb"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputb"+str(employees[i-1].id)+""))!=0:
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma_tarihi=request.POST.get("inputb"+str(employees[i-1].id)+""))
                    if request.POST.get("inputa"+str(employees[i-1].id)+"") is not None and len(request.POST.get("inputa"+str(employees[i-1].id)+""))!=0:
                        calisan.objects.filter(id=employees[i-1].id).update(calisan_isten_ayrilma_nedeni=request.POST.get("inputa"+str(employees[i-1].id)+""))
                    
                         
            if form.is_valid():
                for i in range(1,len(employees)+1):               
                    if "pdf"+str(employees[i-1].id) in request.POST:
                        if maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).exists():
                            maas1=maas.objects.get(calisan_id=employees[i-1],yil=date.today().year)
                            aylar=form.cleaned_data.get("aylar")
                            bordro1=bordro.objects.get(maas_id=maas1.id)
                            calisan1=calisan.objects.get(id=bordro1.calisan_id_id)
                            sirket1=sirket.objects.get(id=employees[i-1].calisan_sirket_id_id)
                            buffer=io.BytesIO()
                            pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

                            p=canvas.Canvas(buffer)
                            p.setFont('Vera', 5)
                            x=2.5
                            y=19
                            p.setPageSize( landscape(A4) )

                            response=FileResponse(content_type ='application/ms-excel')
                            response['Content-Disposition'] = 'attachment; filename="bordro.xls"'
                            wb=xlwt.Workbook(encoding='utf-8')
                            ws=wb.add_sheet('Bordro')
                            row_num=0
                            font_style=xlwt.XFStyle()
                            font_style.font.bold=True

                            p.line(1*cm, (y+1)*cm, 28.5*cm, (y+1)*cm)#üst çizgi
                            p.drawString(2*cm, (y+0.7)*cm, "Firma Adı")
                            p.drawString(5.2*cm, (y+0.7)*cm, sirket1.sirket_adi)
                            p.line(1*cm, (y+0.5)*cm, 28.5*cm, (y+0.5)*cm)#üstün altı
                            p.line(1*cm, (y+0)*cm, 28.5*cm, (y+0)*cm)#alt çizgi
                            p.drawString(2*cm, (y+0.2)*cm, "Sgk İşyeri Numarası")
                            p.line(1*cm, (y-(0.5))*cm, 28.5*cm, (y-(0.5))*cm)#sağ çizgi
                            p.drawString(2*cm, (y-0.3)*cm, "Adres")
                            p.drawString(5.2*cm, (y-0.3)*cm, sirket1.sirket_adres)
                            p.line(1*cm, (y-1)*cm, 28.5*cm, (y-1)*cm)#sağ çizgi
                            p.drawString(2*cm, (y-0.8)*cm, "Vergi Dairesi")
                            p.drawString(5.2*cm, (y-0.8)*cm, sirket1.sirket_vergi_dairesi.vd_adi)
                            p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#sağ çizgi
                            p.drawString(2*cm, (y-1.3)*cm, "Vergi Numarası")
                            p.drawString(5.2*cm, (y-1.3)*cm, sirket1.sirket_vergi_numarasi)
                            p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
                            p.drawString(2*cm, (y-1.8)*cm, "Mersis Numarası")
                            p.drawString(5.2*cm, (y-1.8)*cm, sirket1.sirket_mersis_no)
                            p.line(1*cm, (y-2)*cm, 1*cm, (y+1)*cm)#sol çizgi
                            p.line(5*cm, (y-2)*cm, 5*cm, (y+1)*cm)#sağ çizgi
                            p.line(28.5*cm, (y-2)*cm, 28.5*cm, (y+1)*cm)#sağ çizgi
                            ## üst taraf
                            y=y-2
                            p.line(1*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#üst çizgi
                            p.drawString(1.1*cm, (y-1)*cm, "Ad-Soyad")
                            p.drawString(1.1*cm, (y-1.3)*cm, "Tc Kimlik No")
                            
                            if len(""+calisan1.calisan_adi+" "+calisan1.calisan_soyadi+"") <= 19:
                             p.setFont('Vera', 4)
                             p.drawString(1.1*cm, (y-1.8)*cm, calisan1.calisan_adi + " " + calisan1.calisan_soyadi)
                            else:
                                p.setFont('Vera', 4)
                                p.drawString(1.1*cm, (y-1.7)*cm, calisan1.calisan_adi)
                                p.drawString(1.1*cm, (y-1.9)*cm, calisan1.calisan_soyadi)

                            p.setFont('Vera', 5)
                            p.drawString(1.1*cm, (y-2.3)*cm, calisan1.calisan_tc)
                            p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#üstün altı
                            p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
                            p.line(1*cm, (y-2.5)*cm, 28.5*cm, (y-2.5)*cm)#sol çizgi
                            p.line(1*cm, (y-2.5)*cm, 1*cm, (y-0.7)*cm)#sağ çizgi
                            p.line(28.5*cm, (y-2.5)*cm, 28.5*cm, (y-0.7)*cm)#sağ çizgi
                            p.line(2.8*cm, (y-2.5)*cm, 2.8*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(2.9*cm, (y-1)*cm, "Kanun No")
                            p.drawString(2.9*cm, (y-1.3)*cm, "Prim Günü")
                            if aylar[0] == 'ocak':
                                if bordro1.ocak_kanun_no=="pick1":
                                    p.drawString(2.9*cm, (y-1.8)*cm, "Standart")
                                else:
                                    p.drawString(2.9*cm, (y-1.8)*cm, bordro1.ocak_kanun_no)

                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi1))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ocak_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ocak_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ocak_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ocak_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ocak_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ocak_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ocak_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ocak_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ocak_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ocak_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ocak_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ocak_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ocak_damga_vergisi_istisnasi))
                            elif aylar[0] == "subat":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.subat_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi2))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.subat_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.subat_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.subat_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.subat_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.subat_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.subat_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.subat_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.subat_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.subat_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.subat_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.subat_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.subat_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.subat_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.subat_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.subat_damga_vergisi_istisnasi))
                            elif aylar[0] == "mart":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.mart_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi3))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.mart_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.mart_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.mart_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.mart_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.mart_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.mart_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.mart_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.mart_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.mart_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.mart_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.mart_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.mart_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.mart_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.mart_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.mart_damga_vergisi_istisnasi))
                            elif aylar[0] == "nisan":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.nisan_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi4))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.nisan_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.nisan_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.nisan_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.nisan_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.nisan_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.nisan_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.nisan_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.nisan_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.nisan_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.nisan_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.nisan_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.nisan_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.nisan_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.nisan_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.nisan_damga_vergisi_istisnasi))
                            elif aylar[0] == "mayis":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.mayis_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi5))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.mayis_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.mayis_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.mayis_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.mayis_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.mayis_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.mayis_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.mayis_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.mayis_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.mayis_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.mayis_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.mayis_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.mayis_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.mayis_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.mayis_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.mayis_damga_vergisi_istisnasi))
                            elif aylar[0] == "haziran":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.haziran_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi6))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.haziran_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.haziran_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.haziran_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.haziran_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.haziran_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.haziran_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.haziran_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.haziran_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.haziran_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.haziran_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.haziran_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.haziran_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.haziran_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.haziran_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.haziran_damga_vergisi_istisnasi))
                            elif aylar[0] == "temmuz":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.temmuz_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi7))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.temmuz_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.temmuz_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.temmuz_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.temmuz_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.temmuz_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.temmuz_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.temmuz_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.temmuz_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.temmuz_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.temmuz_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.temmuz_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.temmuz_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.temmuz_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.temmuz_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.temmuz_damga_vergisi_istisnasi))
                            elif aylar[0] == "agustos":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.agustos_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi8))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.agustos_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.agustos_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.agustos_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.agustos_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.agustos_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.agustos_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.agustos_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.agustos_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.agustos_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.agustos_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.agustos_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.agustos_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.agustos_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.agustos_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.agustos_damga_vergisi_istisnasi))
                            elif aylar[0] == "eylul":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.eylul_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi9))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.eylul_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.eylul_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.eylul_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.eylul_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.eylul_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.eylul_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.eylul_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.eylul_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.eylul_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.eylul_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.eylul_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.eylul_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.eylul_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.eylul_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.eylul_damga_vergisi_istisnasi))
                            elif aylar[0] == "ekim":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.ekim_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi10))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ekim_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ekim_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ekim_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ekim_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ekim_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ekim_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ekim_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ekim_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ekim_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ekim_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ekim_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ekim_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ekim_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ekim_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ekim_damga_vergisi_istisnasi))
                            elif aylar[0] == "kasim":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.kasim_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi11))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.kasim_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.kasim_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.kasim_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.kasim_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.kasim_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.kasim_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.kasim_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.kasim_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.kasim_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.kasim_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.kasim_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.kasim_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.kasim_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.kasim_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.kasim_damga_vergisi_istisnasi))
                            elif aylar[0] == "aralik":
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.aralik_kanun_no)
                                p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi12))
                                p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.aralik_brut))
                                p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.aralik_brut))
                                p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.aralik_sgk_kesintisi))
                                p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.aralik_issizlik_kesintisi))
                                p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.aralik_kumulatif_vergi))
                                p.drawString(14*cm, (y-1.8)*cm, str(bordro1.aralik_vergi_matrahi))
                                p.drawString(14*cm, (y-2.3)*cm, str(bordro1.aralik_istisna_oncesi_gelir))
                                p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.aralik_asgari_gelir_vergisi_istisnasi))
                                p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.aralik_gelir_vergisi))
                                p.drawString(18*cm, (y-1.8)*cm, str(bordro1.aralik_damga_vergisi))
                                p.drawString(18*cm, (y-2.3)*cm, str(bordro1.aralik_net_ucret))
                                p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.aralik_isveren_sgk_kesintisi))
                                p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.aralik_isveren_issizlik_kesintisi))
                                p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.aralik_gelir_vergisi_istisnasi))
                                p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.aralik_damga_vergisi_istisnasi))
                            p.line(4*cm, (y-2.5)*cm, 4*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(4.1*cm, (y-1)*cm, "Brüt Ücret")
                            p.drawString(4.1*cm, (y-1.3)*cm, "Sair Öd.")

                            p.line(5.8*cm, (y-2.5)*cm, 5.8*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(5.9*cm, (y-1)*cm, "Sair Öd.2")
                            p.drawString(5.9*cm, (y-1.3)*cm, "Sair Öd.3")
                            p.line(7.3*cm, (y-2.5)*cm, 7.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(7.4*cm, (y-1)*cm, "Fazla Mesai")
                            p.drawString(7.4*cm, (y-1.3)*cm, "Kesinti 1")
                            p.line(9*cm, (y-2.5)*cm, 9*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(9.1*cm, (y-1)*cm, "Kesinti 2")
                            p.drawString(9.1*cm, (y-1.3)*cm, "Kesinti 3")
                            p.line(10.3*cm, (y-2.5)*cm, 10.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(10.4*cm, (y-1)*cm, "Toplam Brüt")
                            p.drawString(10.4*cm, (y-1.3)*cm, "SGK İşçi Payı")

                            p.line(12.3*cm, (y-2.5)*cm, 12.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(12.4*cm, (y-1)*cm, "SGK İşçi İşz.")
                            p.drawString(12.4*cm, (y-1.3)*cm, "Küm. Vergi M.")

                            p.line(13.9*cm, (y-2.5)*cm, 13.9*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(14*cm, (y-1)*cm, "Vergi Matrahı")
                            p.drawString(14*cm, (y-1.3)*cm, "Gelir Vergisi")

                            p.line(15.3*cm, (y-2.5)*cm, 15.3*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(15.4*cm, (y-1)*cm, "Asgari Ü. Gelir V. İst.")
                            p.drawString(15.4*cm, (y-1.3)*cm, "Kalan Gelir Vergisi")

                            p.line(17.9*cm, (y-2.5)*cm, 17.9*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(18*cm, (y-1)*cm, "Damga Vergisi")
                            p.drawString(18*cm, (y-1.3)*cm, "Net Ücret")

                            p.line(21*cm, (y-2.5)*cm, 21*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(21.1*cm, (y-1.3)*cm, "SGK İsveren Primi")
                            p.drawString(21.1*cm, (y-1)*cm, "SGK İşveren İşsizlik Primi")

                            p.line(23.8*cm, (y-2.5)*cm, 23.8*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(23.9*cm, (y-1.3)*cm, "Gelir Vergisi İstisnası")
                            p.drawString(23.9*cm, (y-1)*cm, "Damga Vergisi İstisnası")

                            p.line(26.4*cm, (y-2.5)*cm, 26.4*cm, (y-0.7)*cm)#sağ çizgi
                            p.drawString(26.5*cm, (y-1.3)*cm, "Sgk Prim İstisnası")
                            p.drawString(26.5*cm, (y-1)*cm, "Sgk İşsizlik Prim İst.")
                            #orta kısım
                            y=y-7
                            p.line(1*cm, (y-0.7)*cm, 5.25*cm, (y-0.7)*cm)#üst çizgi
                            p.line(5.85*cm, (y-0.7)*cm, 10.1*cm, (y-0.7)*cm)#alt çizgi
                            p.line(10.7*cm, (y-0.7)*cm, 14.95*cm, (y-0.7)*cm)#alt çizgi
                            p.line(15.55*cm, (y-0.7)*cm, 19.8*cm, (y-0.7)*cm)#alt çizgi
                            p.line(20.4*cm, (y-0.7)*cm, 24.65*cm, (y-0.7)*cm)#alt çizgi
                            p.line(25.25*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#alt çizgi
                            p.line(1*cm, (y-0.7)*cm, 1*cm, (y-9)*cm)#üst çizgi
                            p.line(5.25*cm, (y-0.7)*cm, 5.25*cm, (y-9)*cm)#üst çizgi
                            p.line(5.85*cm, (y-0.7)*cm, 5.85*cm, (y-9)*cm)#üst çizgi
                            p.line(10.1*cm, (y-0.7)*cm, 10.1*cm, (y-9)*cm)#üst çizgi
                            p.line(10.7*cm, (y-0.7)*cm, 10.7*cm, (y-9)*cm)#üst çizgi
                            p.line(14.95*cm, (y-0.7)*cm, 14.95*cm, (y-9)*cm)#üst çizgi
                            p.line(15.55*cm, (y-0.7)*cm, 15.55*cm, (y-9)*cm)#üst çizgi
                            p.line(19.8*cm, (y-0.7)*cm, 19.8*cm, (y-9)*cm)#üst çizgi
                            p.line(20.4*cm, (y-0.7)*cm, 20.4*cm, (y-9)*cm)#üst çizgi
                            p.line(24.65*cm, (y-0.7)*cm, 24.65*cm, (y-9)*cm)#üst çizgi
                            p.line(25.25*cm, (y-0.7)*cm, 25.25*cm, (y-9)*cm)#üst çizgi
                            p.line(28.5*cm, (y-0.7)*cm, 28.5*cm, (y-9)*cm)#üst çizgi
                            p.line(1*cm, (y-9)*cm, 5.25*cm, (y-9)*cm)
                            p.drawString(2.6*cm, (y-1.1)*cm, "Brüt Toplam")
                            p.line(5.85*cm, (y-9)*cm, 10.1*cm, (y-9)*cm)
                            p.drawString(7.8*cm, (y-1.1)*cm, "SGK")
                            p.line(10.7*cm, (y-9)*cm, 14.95*cm, (y-9)*cm)
                            p.drawString(12.3*cm, (y-1.1)*cm, "Gelir Vergisi")
                            p.line(15.55*cm, (y-9)*cm, 19.8*cm, (y-9)*cm)
                            p.drawString(17.1*cm, (y-1.1)*cm, "Damga Vergisi")
                            p.line(20.4*cm, (y-9)*cm, 24.65*cm, (y-9)*cm)
                            p.drawString(22.1*cm, (y-1.1)*cm, "Net Ücret")
                            p.line(25.25*cm, (y-9)*cm, 28.5*cm, (y-9)*cm)
                            p.drawString(26.6*cm, (y-1.1)*cm, "Günler")
                            p.line(3*cm, (y-1.3)*cm, 3*cm, (y-9)*cm)#üst çizgi
                            p.line(8*cm, (y-1.3)*cm, 8*cm, (y-9)*cm)#üst çizgi
                            p.line(12.7*cm, (y-1.3)*cm, 12.7*cm, (y-9)*cm)#üst çizgi
                            p.line(17.6*cm, (y-1.3)*cm, 17.6*cm, (y-9)*cm)#üst çizgi
                            p.line(22.5*cm, (y-1.3)*cm, 22.5*cm, (y-9)*cm)#üst çizgi
                            p.line(26.8*cm, (y-1.3)*cm, 26.8*cm, (y-9)*cm)#üst çizgi
                            p.line(1*cm, (y-1.3)*cm, 5.25*cm, (y-1.3)*cm)
                            p.drawString(1.2*cm, (y-1.7)*cm, "Brüt Ücret")
                            p.line(5.85*cm, (y-1.3)*cm, 10.1*cm, (y-1.3)*cm)
                            p.drawString(6.1*cm, (y-1.7)*cm, "SGK İşveren Payı")
                            p.line(10.7*cm, (y-1.3)*cm, 14.95*cm, (y-1.3)*cm)
                            p.drawString(10.8*cm, (y-1.7)*cm, "Hesaplanan Gelir V.")
                            p.line(15.55*cm, (y-1.3)*cm, 19.8*cm, (y-1.3)*cm)
                            p.drawString(15.6*cm, (y-1.7)*cm, "Hesaplanan Damga V.")
                            p.line(20.4*cm, (y-1.3)*cm, 24.65*cm, (y-1.3)*cm)
                            p.drawString(20.5*cm, (y-1.7)*cm, "Asıl Ücret")
                            p.line(25.25*cm, (y-1.3)*cm, 28.5*cm, (y-1.3)*cm)
                            p.drawString(25.4*cm, (y-1.7)*cm, "Çalışma Günü")
                            p.line(1*cm, (y-2)*cm, 5.25*cm, (y-2)*cm)
                            p.drawString(1.2*cm, (y-2.5)*cm, "Sair Ödeme1")
                            p.line(5.85*cm, (y-2)*cm, 10.1*cm, (y-2)*cm)
                            p.drawString(6.1*cm, (y-2.5)*cm, "Sgk İşçi Payı")
                            p.line(10.7*cm, (y-2)*cm, 14.95*cm, (y-2)*cm)
                            p.drawString(10.8*cm, (y-2.5)*cm, "ASgari Ü. Gelir V. İst.")
                            p.line(15.55*cm, (y-2)*cm, 19.8*cm, (y-2)*cm)
                            p.drawString(15.6*cm, (y-2.5)*cm, "İst. Damga Vergisi")
                            p.line(20.4*cm, (y-2)*cm, 24.65*cm, (y-2)*cm)
                            p.drawString(20.5*cm, (y-2.5)*cm, "Fazla Mesai")
                            p.line(25.25*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)
                            p.drawString(25.4*cm, (y-2.5)*cm, "Haftasonu Günü")
                            p.line(1*cm, (y-2.7)*cm, 5.25*cm, (y-2.7)*cm)
                            p.drawString(1.2*cm, (y-3.2)*cm, "Sair Ödeme2")
                            p.line(5.85*cm, (y-2.7)*cm, 10.1*cm, (y-2.7)*cm)
                            p.drawString(6.1*cm, (y-3.2)*cm, "Sgk İşv. İşz. Payı")
                            p.line(10.7*cm, (y-2.7)*cm, 14.95*cm, (y-2.7)*cm)
                            p.drawString(10.8*cm, (y-3.2)*cm, "Terkin E. Gelir V.")
                            p.line(15.55*cm, (y-2.7)*cm, 19.8*cm, (y-2.7)*cm)
                            p.line(20.4*cm, (y-2.7)*cm, 24.65*cm, (y-2.7)*cm)
                            p.drawString(20.5*cm, (y-3.2)*cm, "Sair Ödeme 1")
                            p.line(25.25*cm, (y-2.7)*cm, 28.5*cm, (y-2.7)*cm)
                            p.drawString(25.5*cm, (y-3.2)*cm, "Genel Tatil")
                            p.line(1*cm, (y-3.4)*cm, 5.25*cm, (y-3.4)*cm)
                            p.drawString(1.2*cm, (y-3.9)*cm, "Sair Ödeme3")
                            p.line(5.85*cm, (y-3.4)*cm, 10.1*cm, (y-3.4)*cm)
                            p.drawString(6.1*cm, (y-3.9)*cm, "Sgk İşçi İşz. Payı")
                            p.line(10.7*cm, (y-3.4)*cm, 14.95*cm, (y-3.4)*cm)

                            p.line(20.4*cm, (y-3.4)*cm, 24.65*cm, (y-3.4)*cm)
                            p.drawString(20.5*cm, (y-3.9)*cm, "Sair Ödeme 2")
                            p.line(25.25*cm, (y-3.4)*cm, 28.5*cm, (y-3.4)*cm)
                            p.drawString(25.5*cm, (y-3.9)*cm, "Yıllık İzin")
                            p.line(1*cm, (y-4.1)*cm, 5.25*cm, (y-4.1)*cm)
                            p.drawString(1.2*cm, (y-4.6)*cm, "Fazla Mesai")
                            p.line(5.85*cm, (y-4.1)*cm, 10.1*cm, (y-4.1)*cm)
                            p.drawString(6.1*cm, (y-4.6)*cm, "Sgk Prim Desteği İst.")
                            p.line(20.4*cm, (y-4.1)*cm, 24.65*cm, (y-4.1)*cm)
                            p.drawString(20.5*cm, (y-4.6)*cm, "Sair Ödeme 3")
                            p.line(25.25*cm, (y-4.1)*cm, 28.5*cm, (y-4.1)*cm)
                            p.drawString(25.5*cm, (y-4.6)*cm, "Sıhhi İzin")
                            p.line(1*cm, (y-4.8)*cm, 5.25*cm, (y-4.8)*cm)
                            p.drawString(1.2*cm, (y-5.3)*cm, "Kesinti 1")
                            p.line(5.85*cm, (y-4.8)*cm, 10.1*cm, (y-4.8)*cm)
                            p.drawString(6.1*cm, (y-5.3)*cm, "Sgk İşs. Prim Des. İst.")
                            p.line(20.4*cm, (y-4.8)*cm, 24.65*cm, (y-4.8)*cm)
                            p.drawString(20.5*cm, (y-5.3)*cm, "Kesinti 1")
                            p.line(25.25*cm, (y-4.8)*cm, 28.5*cm, (y-4.8)*cm)
                            p.drawString(25.5*cm, (y-5.3)*cm, "Ucretsiz İzin")
                            p.line(1*cm, (y-5.5)*cm, 5.25*cm, (y-5.5)*cm)
                            p.drawString(1.2*cm, (y-6)*cm, "Kesinti 2")
                            p.line(5.85*cm, (y-5.5)*cm, 10.1*cm, (y-5.5)*cm)
                            p.line(20.4*cm, (y-5.5)*cm, 24.65*cm, (y-5.5)*cm)
                            p.drawString(20.5*cm, (y-6)*cm, "Kesinti 2")
                            p.line(25.25*cm, (y-5.5)*cm, 28.5*cm, (y-5.5)*cm)
                            p.drawString(25.5*cm, (y-6)*cm, "Ücretli İzin")
                            p.line(1*cm, (y-6.2)*cm, 5.25*cm, (y-6.2)*cm)
                            p.drawString(1.2*cm, (y-6.7)*cm, "Kesinti 3")
                            p.line(20.4*cm, (y-6.2)*cm, 24.65*cm, (y-6.2)*cm)
                            p.drawString(20.5*cm, (y-6.7)*cm, "Kesinti 3")
                            p.line(25.25*cm, (y-6.2)*cm, 28.5*cm, (y-6.2)*cm)
                            p.drawString(25.5*cm, (y-6.7)*cm, "Mazeret İzin")
                            p.line(1*cm, (y-6.9)*cm, 5.25*cm, (y-6.9)*cm)
                            p.line(20.4*cm, (y-6.9)*cm, 24.65*cm, (y-6.9)*cm)
                            p.line(25.25*cm, (y-6.9)*cm, 28.5*cm, (y-6.9)*cm)
                            p.drawString(25.5*cm, (y-7.4)*cm, "Prim Günü")

                            p.line(1*cm, (y-7.6)*cm, 5.25*cm, (y-7.6)*cm)

                            p.line(5.85*cm, (y-7.6)*cm, 10.1*cm, (y-7.6)*cm)

                            p.line(10.7*cm, (y-7.6)*cm, 14.95*cm, (y-7.6)*cm)

                            p.line(15.55*cm, (y-7.6)*cm, 19.8*cm, (y-7.6)*cm)

                            p.line(20.4*cm, (y-7.6)*cm, 24.65*cm, (y-7.6)*cm)

                            p.line(25.25*cm, (y-7.6)*cm, 28.5*cm, (y-7.6)*cm)
                            p.line(1*cm, (y-8.3)*cm, 5.25*cm, (y-8.3)*cm)
                            p.drawString(1.2*cm, (y-8.7)*cm, "Brüt Toplam")
                            p.line(5.85*cm, (y-8.3)*cm, 10.1*cm, (y-8.3)*cm)
                            p.drawString(10.7*cm, (y-8.7)*cm, "Ödenecek SGK Primi")

                            p.line(10.7*cm, (y-8.3)*cm, 14.95*cm, (y-8.3)*cm)
                            p.drawString(15.55*cm, (y-8.7)*cm, "Ödenecek Gelir V.")
                            p.line(15.55*cm, (y-8.3)*cm, 19.8*cm, (y-8.3)*cm)
                            p.drawString(20.5*cm, (y-8.7)*cm, "Ödenecek Damga V.")
                            p.line(20.4*cm, (y-8.3)*cm, 24.65*cm, (y-8.3)*cm)
                            p.drawString(25.5*cm, (y-8.7)*cm, "Net Ödenecek Ücret")
                            p.line(25.25*cm, (y-8.3)*cm, 28.5*cm, (y-8.3)*cm)

                            tur=form.cleaned_data.get('export')
                            print(tur)

                            if tur == "pdf":
                                p.showPage()
                                p.save()
                                buffer.seek(0)
                                return FileResponse(buffer, as_attachment=False, filename='bordro.pdf')
                            elif tur == "xls":
                                output = io.BytesIO()
                                wb.save(output)
                                output.seek(0)
                                return FileResponse(output, as_attachment=False, filename='bordro.xls')
                            else:
                                return HttpResponseNotFound("404")

            return redirect(reverse('user:passiveemployee', kwargs={'id':id}))


    context={
        'subes':sube1,
        'company':company,
        'uyelik':uyelik,
        'employees':employees1,
        'calisantab':calisantab,
        'sirketid':id,
        'deneme':deneme,
        'aylar':aylar,
        'bordro':deneme1,
        'month':month,
        'form':form,
        'maxuser':maxuser,
        'calisansayi':calisansayi,
        'uyelik':uyelik,
        'uyelik1':uyelik1,
        'sirketedit':False,
        'subeedit':True,

    }
    return render(request,'passiveemployee.html',context)
@login_required()
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def companyupdate(request,id):
    if (sirket.objects.filter(id=id)).exists():
        company=sirket.objects.get(id=id)
        if subs.objects.get(id=company.sirket_uyelik_id).subs_aktiflik==False:
            return handler404(request,exception=404)
    maas1=get_object_or_404(sirket,id=sirket.objects.get(id=id).id)
    form=SirketRegisterForm(request.POST or None,instance=maas1)
    if form.is_valid():
        maas1=form.save(commit=False)
        maas1.save()
        return redirect(reverse('user:subelist', kwargs={'id':id}))
    context={
        'form':form
    }
    return render(request,'companyupdate.html',context)

def updatesube(request,id):
    if (sirket.objects.filter(id=sube.objects.get(id=id).sube_sirket_id_id)).exists():
        company=sirket.objects.get(id=sube.objects.get(id=id).sube_sirket_id_id)
        if subs.objects.get(id=company.sirket_uyelik_id).subs_aktiflik==False:
            return handler404(request,exception=404)
    maas1=get_object_or_404(sube,id=sube.objects.get(id=id).id)
    if not (sgkisyeri.objects.filter(sube_id=maas1)).exists():
        sgkisyeri.objects.create(sube_id=maas1)
    if not (iskur.objects.filter(sube_id=maas1)).exists():
        iskur.objects.create(sube_id=maas1)
    sgk1=get_object_or_404(sgkisyeri,sube_id=maas1)
    iskur1=get_object_or_404(iskur,sube_id=maas1)
    form=SubeRegisterForm(request.POST or None,instance=maas1)
    form2=sgkisyeriregisterform(request.POST or None,instance=sgk1)
    form3=iskurregisterform(request.POST or None,instance=iskur1)

    if form.is_valid() and form2.is_valid() and form3.is_valid():
        maas1=form.save(commit=False)
        maas1.save()
        sgk1=form2.save(commit=False)
        sgk1.save()
        iskur1=form3.save(commit=False)
        iskur1.save()
        return redirect(reverse('user:employeelist', kwargs={'id':id}))
    context={
        'form':form,
        'form2':form2,
        'form3':form3
    }
    return render(request,'updatesube.html',context)
@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def calisanregister(request,id):
    if (sirket.objects.filter(id=sube.objects.get(id=id).sube_sirket_id_id)).exists():
        company=sirket.objects.get(id=sube.objects.get(id=id).sube_sirket_id_id)
        if subs.objects.get(id=company.sirket_uyelik_id).subs_aktiflik==False:
            return handler404(request,exception=404)
    form = RegisterForm(request.POST or None)
    calisan3=CalisanRegisterForm(request.POST or None,request.FILES or None)
    form1=calisanturform(request.POST or None)
    form2=engelliform(request.POST or None)
    if  calisan3.is_valid() and  form1.is_valid() and form2.is_valid():
        username=request.POST.get('username1')
        password = request.POST.get('password1')
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.is_active=True
        newUser.save()




        calisan2=calisan3.save(commit=False)
        if form1.cleaned_data.get('tur')=="pick0":
            newUser.groups.add(Group.objects.get(name='calisan'))
            calisan2.calisan_tur="pick0"
        elif form1.cleaned_data.get('yetki')=="pick2":
            newUser.groups.add(Group.objects.get(name='mali_musavir'))
            calisan2.calisan_tur="pick2"
        elif form1.cleaned_data.get('tur')=="pick1":
            newUser.groups.add(Group.objects.get(name='muhasebe'))
            calisan2.calisan_tur="pick1"
        sube1=sube.objects.get(id=id)
        calisan2.calisan_sirket_id=sirket.objects.get(id=sube1.sube_sirket_id.id)
        calisan2.calisan_sube_id=sube1
        calisan2.calisan_engelli=form2.cleaned_data.get('engelli')
        lastid=User.objects.get(username=username)
        calisan2.calisan_id=lastid
        if  not calisan2.calisan_photo :
            if calisan2.calisan_gender=="pick1":
                calisan2.calisan_photo="/calisan_photo/default.png"
            elif calisan2.calisan_gender=="pick2":
                calisan2.calisan_photo="/calisan_photo/defaultw.png"
            else:
                calisan2.calisan_photo="/calisan_photo/default.png"

        calisan2.save()
        calisan1=calisan.objects.get(calisan_id=lastid)
        temp=maas.objects.create(calisan_id=calisan1,yil=datetime.now().year)
        temp.save()
        maas1=maas.objects.get(calisan_id=calisan1,yil=datetime.now().year)
        bordro.objects.create(maas_id=maas1,calisan_id=calisan1).save()


        return redirect(reverse('user:subelist', kwargs={'id':id}))

    else:
         context = {
            'form': form,
            'calisan':calisan3,
            'form1':form1,
            'form2':form2,

            }
    return render(request, 'addemployee.html',context)

def checkusername(request):
    username=request.POST.get('username1')
    if len(username)<3:
        return HttpResponse('<p style="color:red">Kullanıcı adı en az 3 karakter olmalıdır</p>')
    elif User.objects.filter(username=username).exists():
        return HttpResponse('<p style="color:red">Bu kullanıcı adı kullanılamaz</p>')
    else:
        return HttpResponse('<p style="color:green">Bu kullanıcı adı kullanılabilir</p>')
@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def update_emp(request,id):

    maas1=get_object_or_404(calisan,id=calisan.objects.get(id=id).id)
    form=CalisanRegisterForm(request.POST or None, request.FILES or None,instance=maas1)
    user_group= User.groups.through.objects.get(user_id=maas1.calisan_id_id)


    if maas1.calisan_tur=='pick0':
        yetki="pick0"
    elif maas1.calisan_tur=='pick2':
        yetki="pick2"
    elif maas1.calisan_tur=='pick1':
        yetki="pick1"
    form1=calisanturform(request.POST or None,initial={'tur':yetki})
    form2=engelliform(request.POST or None,initial={'engelli':maas1.calisan_engelli})


    if form.is_valid() and form1.is_valid() and form2.is_valid():
        maas1=form.save(commit=False)
        if form1.cleaned_data.get('tur')=="pick0":
            maas1.calisan_tur="pick0"
            user_group.group=Group.objects.get(name='calisan')
            user_group.save()
        elif form1.cleaned_data.get('tur')=="pick2":
            maas1.calisan_tur="pick2"
            user_group.group=Group.objects.get(name='mali_musavir')
            user_group.save()
        elif form1.cleaned_data.get('tur')=="pick1":
            maas1.calisan_tur="pick1"
            user_group.group=Group.objects.get(name='muhasebe')
            user_group.save()
        maas1.calisan_engelli=form2.cleaned_data.get('engelli')
        maas1.save()


        return redirect(reverse('user:employeedetail', kwargs={'id':id}))
    else:
        print("form is not valid")
    context={
        'form':form,
        'form1':form1,
        'form2':form2,

    }
    return render(request,'empupdate.html',context)

@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists())
def addcompwithurl(request,slug):
    mali=mali_musavir.objects.get(mali_musavir_id=request.user)
    mali2=mali_sirket.objects.get(id=mali.mali_sirket_id.id)
    mali2.mali_sirket_bagli_sirketler.add(sirket.objects.get(sirket_davet_kodu=slug))
    mali2.save()
    sirket1=sirket.objects.get(sirket_davet_kodu=slug)
    sirket1.sirket_davet_kodu=uuid.uuid4()
    sirket1.save()
    return redirect(reverse('user:listcompany'))



@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='admin').exists())
def listcompany(request):
    companys=[]
    if request.user.groups.filter(name='admin').exists():
        companys=sirket.objects.all()
    elif request.user.groups.filter(name='mali_musavir').exists():
        mali1=mali_musavir.objects.get(mali_musavir_id=request.user)
        mali2=mali_sirket.objects.get(id=mali1.mali_sirket_id.id)
        for i in mali2.mali_sirket_bagli_sirketler.all():
            companys.append(sirket.objects.get(id=i.id))

    sirkettab=True
    context={
        'companys':companys,
        'sirkettab':sirkettab,
        'sirketedit':True,
        'subeedit':False,

    }
    return render(request,'listcompany.html',context)

@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def listemployee(request,id):

    aylar=employeelistaylar(request.POST or None)
    form=denemeform(request.POST or None)
    try:

        sube1=sube.objects.get(id=id)
        company=sirket.objects.get(id=sube1.sube_sirket_id.id)
        user=User.objects.get(id=request.user.id)
        user1=calisan.objects.get(calisan_id=user)
    except sirket.DoesNotExist:
        company=None
        sube1=None
    except calisan.DoesNotExist:
        user1=None


    if company is  None:
        return HttpResponseNotFound('<h1>Page not found</h1>',status=404)
    elif request.user.groups.filter(name='admin').exists():
        pass

    elif request.user.groups.filter(name='mali_musavir').exists():
        if company not in  mali_sirket.objects.get(id=mali_musavir.objects.get(mali_musavir_id=request.user).mali_sirket_id.id).mali_sirket_bagli_sirketler.all():
            return HttpResponseNotFound('<h1>Page not found</h1>')
    elif request.user.groups.filter(name='muhasebe').exists():
        if calisan.objects.get(calisan_id=request.user).calisan_sirket_id!=company:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    deneme=[]
    deneme1=[]
    if request.method == 'POST':
        employees=calisan.objects.filter(calisan_sirket_id=company,calisan_sube_id=sube1).order_by('calisan_soyadi')
        if employees is not None:
            for i in employees:
                if maas.objects.filter(calisan_id=i,yil=date.today().year).exists():
                    deneme.append(maas.objects.filter(calisan_id=i,yil=date.today().year))
                else:
                    deneme.append(maas.objects.none())
        if "infobutton" in request.POST:
            for i in range(1,len(employees)+1):
                if request.POST.get("input1"+str(i)+"") is not None and len(request.POST.get("input1"+str(i)+""))!=0:
                    employees[i-1].calisan_adi=request.POST.get("input1"+str(i)+"")
                if request.POST.get("input2"+str(i)+"") is not None and len(request.POST.get("input2"+str(i)+""))!=0:
                    employees[i-1].calisan_soyadi=request.POST.get("input2"+str(i)+"")
                if request.POST.get("input3"+str(i)+"") is not None and len(request.POST.get("input3"+str(i)+""))!=0:
                    employees[i-1].calisan_tc=request.POST.get("input3"+str(i)+"")
                if request.POST.get("input4"+str(i)+"") is not None and len(request.POST.get("input4"+str(i)+""))!=0:
                    employees[i-1].calisan_mail=request.POST.get("input4"+str(i)+"")
                if request.POST.get("input5"+str(i)+"") is not None and len(request.POST.get("input5"+str(i)+""))!=0:
                    employees[i-1].calisan_telefon=request.POST.get("input5"+str(i)+"")
                if request.POST.get("input6"+str(i)+"") is not None and len(request.POST.get("input6"+str(i)+""))!=0:
                    employees[i-1].calisan_adres=request.POST.get("input6"+str(i)+"")
                if request.POST.get("input7"+str(i)+"") is not None and len(request.POST.get("input7"+str(i)+""))!=0:
                    d=request.POST.get("input7"+str(i)+"")
                    employees[i-1].calisan_dogum_tarihi=d
                if request.POST.get("input8"+str(i)+"") is not None and len(request.POST.get("input8"+str(i)+""))!=0:
                    employees[i-1].calisan_ise_giris_tarihi=request.POST.get("input8"+str(i)+"")
                if request.POST.get("calisanengel"+str(i)+"") is not None and len(request.POST.get("calisanengel"+str(i)+""))!=0:
                    employees[i-1].calisan_engelli=request.POST.get("calisanengel"+str(i)+"")
                if request.POST.get("calisanemekli"+str(i)+"") is not None and len(request.POST.get("calisanemekli"+str(i)+""))!=0:
                    print(request.POST.get("calisanemekli"+str(i)+""))
                    employees[i-1].calisan_emekli=request.POST.get("calisanemekli"+str(i)+"")
                employees[i-1].save()
                
        if "maasbuton" in request.POST:

            for i in range(1,len(employees)+1):
                if request.POST.get("calisantesvik"+str(i)+"") is not None:
                    employees[i-1].calisan_tesvik=request.POST.get("calisantesvik"+str(i)+"")
                employees[i-1].save()

                if request.POST.get("maas"+str(i)+"") is not None and len(request.POST.get("maas"+str(i)+""))!=0:

                    if maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).exists():
                        maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(ucret=request.POST.get("maas"+str(i)+"").replace(",","."))
                        ay=request.POST.get("aylar")
                        bordro1=bordro.objects.get(maas_id=maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id)
                        maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(ucrettipi=request.POST.get("ucrettipi"+str(i)+""))
                        maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(para_birimi=request.POST.get("parabirimi"+str(i)+""))

                        
                        if ay=="ocak":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari1=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi1=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun1=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)

                            bordro1.ocak_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.ocak_brut=data[0]
                            bordro1.ocak_calisilan_gun=data[1]
                            bordro1.ocak_arge_gun=data[2]
                            bordro1.ocak_bordroyaesasbrut=data[3]
                            bordro1.ocak_sgk_matrahi=data[4]
                            bordro1.ocak_sgk_kesintisi=data[5]
                            bordro1.ocak_issizlik_kesintisi=data[6]
                            bordro1.ocak_vergi_matrahi=data[7]
                            bordro1.ocak_kumulatif_vergi=data[8]
                            bordro1.ocak_istisna_oncesi_gelir=data[9]
                            bordro1.ocak_kumulatif_asgari_ucret=data[10]
                            bordro1.ocak_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.ocak_damga_vergisi=data[12]
                            bordro1.ocak_gelir_vergisi=data[13]
                            bordro1.ocak_net_ucret=data[14]
                            bordro1.ocak_isveren_sgk_kesintisi=data[15]
                            bordro1.ocak_isveren_issizlik_kesintisi=data[16]
                            bordro1.ocak_toplam_sgk_kesintisi=data[17]
                            bordro1.ocak_sgk_istisnasi=data[18]
                            bordro1.ocak_odenecek_sgk=data[19]
                            bordro1.ocak_odenecek_gelir_vergisi=data[21]
                            bordro1.ocak_odenecek_damga_vergisi=data[22]
                            bordro1.ocak_istisna_oncesi_damga=data[23]
                            bordro1.ocak_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.ocak_toplam_maliyet=data[25]
                            bordro1.ocak_vergi_dilimi=data[26]
                            bordro1.ocak_gelir_vergisi_istisnasi=data[27]
                            bordro1.ocak_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="subat":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari2=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi2=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun2=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.subat_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.subat_brut=data[0]
                            bordro1.subat_calisilan_gun=data[1]
                            bordro1.subat_arge_gun=data[2]
                            bordro1.subat_bordroyaesasbrut=data[3]
                            bordro1.subat_sgk_matrahi=data[4]
                            bordro1.subat_sgk_kesintisi=data[5]
                            bordro1.subat_issizlik_kesintisi=data[6]
                            bordro1.subat_vergi_matrahi=data[7]
                            bordro1.subat_kumulatif_vergi=data[8]
                            bordro1.subat_istisna_oncesi_gelir=data[9]
                            bordro1.subat_kumulatif_asgari_ucret=data[10]
                            bordro1.subat_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.subat_damga_vergisi=data[12]
                            bordro1.subat_gelir_vergisi=data[13]
                            bordro1.subat_net_ucret=data[14]
                            bordro1.subat_isveren_sgk_kesintisi=data[15]
                            bordro1.subat_isveren_issizlik_kesintisi=data[16]
                            bordro1.subat_toplam_sgk_kesintisi=data[17]
                            bordro1.subat_sgk_istisnasi=data[18]
                            bordro1.subat_odenecek_sgk=data[19]
                            bordro1.subat_odenecek_gelir_vergisi=data[21]
                            bordro1.subat_odenecek_damga_vergisi=data[22]
                            bordro1.subat_istisna_oncesi_damga=data[23]
                            bordro1.subat_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.subat_toplam_maliyet=data[25]
                            bordro1.subat_vergi_dilimi=data[26]
                            bordro1.subat_gelir_vergisi_istisnasi=data[27]
                            bordro1.subat_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()

                        elif ay=="mart":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari3=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi3=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun3=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.mart_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.mart_brut=data[0]
                            bordro1.mart_calisilan_gun=data[1]
                            bordro1.mart_arge_gun=data[2]
                            bordro1.mart_bordroyaesasbrut=data[3]
                            bordro1.mart_sgk_matrahi=data[4]
                            bordro1.mart_sgk_kesintisi=data[5]
                            bordro1.mart_issizlik_kesintisi=data[6]
                            bordro1.mart_vergi_matrahi=data[7]
                            bordro1.mart_kumulatif_vergi=data[8]
                            bordro1.mart_istisna_oncesi_gelir=data[9]
                            bordro1.mart_kumulatif_asgari_ucret=data[10]
                            bordro1.mart_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.mart_damga_vergisi=data[12]
                            bordro1.mart_gelir_vergisi=data[13]
                            bordro1.mart_net_ucret=data[14]
                            bordro1.mart_isveren_sgk_kesintisi=data[15]
                            bordro1.mart_isveren_issizlik_kesintisi=data[16]
                            bordro1.mart_toplam_sgk_kesintisi=data[17]
                            bordro1.mart_sgk_istisnasi=data[18]
                            bordro1.mart_odenecek_sgk=data[19]
                            bordro1.mart_odenecek_gelir_vergisi=data[21]
                            bordro1.mart_odenecek_damga_vergisi=data[22]
                            bordro1.mart_istisna_oncesi_damga=data[23]
                            bordro1.mart_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.mart_toplam_maliyet=data[25]
                            bordro1.mart_vergi_dilimi=data[26]
                            bordro1.mart_gelir_vergisi_istisnasi=data[27]
                            bordro1.mart_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="nisan":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari4=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi4=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun4=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.nisan_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.nisan_brut=data[0]
                            bordro1.nisan_calisilan_gun=data[1]
                            bordro1.nisan_arge_gun=data[2]
                            bordro1.nisan_bordroyaesasbrut=data[3]
                            bordro1.nisan_sgk_matrahi=data[4]
                            bordro1.nisan_sgk_kesintisi=data[5]
                            bordro1.nisan_issizlik_kesintisi=data[6]
                            bordro1.nisan_vergi_matrahi=data[7]
                            bordro1.nisan_kumulatif_vergi=data[8]
                            bordro1.nisan_istisna_oncesi_gelir=data[9]
                            bordro1.nisan_kumulatif_asgari_ucret=data[10]
                            bordro1.nisan_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.nisan_damga_vergisi=data[12]
                            bordro1.nisan_gelir_vergisi=data[13]
                            bordro1.nisan_net_ucret=data[14]
                            bordro1.nisan_isveren_sgk_kesintisi=data[15]
                            bordro1.nisan_isveren_issizlik_kesintisi=data[16]
                            bordro1.nisan_toplam_sgk_kesintisi=data[17]
                            bordro1.nisan_sgk_istisnasi=data[18]
                            bordro1.nisan_odenecek_sgk=data[19]
                            bordro1.nisan_odenecek_gelir_vergisi=data[21]
                            bordro1.nisan_odenecek_damga_vergisi=data[22]
                            bordro1.nisan_istisna_oncesi_damga=data[23]
                            bordro1.nisan_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.nisan_toplam_maliyet=data[25]
                            bordro1.nisan_vergi_dilimi=data[26]
                            bordro1.nisan_gelir_vergisi_istisnasi=data[27]
                            bordro1.nisan_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="mayis":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari5=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi5=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun5=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.mayis_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.mayis_brut=data[0]
                            bordro1.mayis_calisilan_gun=data[1]
                            bordro1.mayis_arge_gun=data[2]
                            bordro1.mayis_bordroyaesasbrut=data[3]
                            bordro1.mayis_sgk_matrahi=data[4]
                            bordro1.mayis_sgk_kesintisi=data[5]
                            bordro1.mayis_issizlik_kesintisi=data[6]
                            bordro1.mayis_vergi_matrahi=data[7]
                            bordro1.mayis_kumulatif_vergi=data[8]
                            bordro1.mayis_istisna_oncesi_gelir=data[9]
                            bordro1.mayis_kumulatif_asgari_ucret=data[10]
                            bordro1.mayis_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.mayis_damga_vergisi=data[12]
                            bordro1.mayis_gelir_vergisi=data[13]
                            bordro1.mayis_net_ucret=data[14]
                            bordro1.mayis_isveren_sgk_kesintisi=data[15]
                            bordro1.mayis_isveren_issizlik_kesintisi=data[16]
                            bordro1.mayis_toplam_sgk_kesintisi=data[17]
                            bordro1.mayis_sgk_istisnasi=data[18]
                            bordro1.mayis_odenecek_sgk=data[19]
                            bordro1.mayis_odenecek_gelir_vergisi=data[21]
                            bordro1.mayis_odenecek_damga_vergisi=data[22]
                            bordro1.mayis_istisna_oncesi_damga=data[23]
                            bordro1.mayis_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.mayis_toplam_maliyet=data[25]
                            bordro1.mayis_vergi_dilimi=data[26]
                            bordro1.mayis_gelir_vergisi_istisnasi=data[27]
                            bordro1.mayis_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="haziran":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari6=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi6=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun6=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.haziran_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.haziran_brut=data[0]
                            bordro1.haziran_calisilan_gun=data[1]
                            bordro1.haziran_arge_gun=data[2]
                            bordro1.haziran_bordroyaesasbrut=data[3]
                            bordro1.haziran_sgk_matrahi=data[4]
                            bordro1.haziran_sgk_kesintisi=data[5]
                            bordro1.haziran_issizlik_kesintisi=data[6]
                            bordro1.haziran_vergi_matrahi=data[7]
                            bordro1.haziran_kumulatif_vergi=data[8]
                            bordro1.haziran_istisna_oncesi_gelir=data[9]
                            bordro1.haziran_kumulatif_asgari_ucret=data[10]
                            bordro1.haziran_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.haziran_damga_vergisi=data[12]
                            bordro1.haziran_gelir_vergisi=data[13]
                            bordro1.haziran_net_ucret=data[14]
                            bordro1.haziran_isveren_sgk_kesintisi=data[15]
                            bordro1.haziran_isveren_issizlik_kesintisi=data[16]
                            bordro1.haziran_toplam_sgk_kesintisi=data[17]
                            bordro1.haziran_sgk_istisnasi=data[18]
                            bordro1.haziran_odenecek_sgk=data[19]
                            bordro1.haziran_odenecek_gelir_vergisi=data[21]
                            bordro1.haziran_odenecek_damga_vergisi=data[22]
                            bordro1.haziran_istisna_oncesi_damga=data[23]
                            bordro1.haziran_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.haziran_toplam_maliyet=data[25]
                            bordro1.haziran_vergi_dilimi=data[26]
                            bordro1.haziran_gelir_vergisi_istisnasi=data[27]
                            bordro1.haziran_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="temmuz":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari7=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi7=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun7=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.temmuz_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.temmuz_brut=data[0]
                            bordro1.temmuz_calisilan_gun=data[1]
                            bordro1.temmuz_arge_gun=data[2]
                            bordro1.temmuz_bordroyaesasbrut=data[3]
                            bordro1.temmuz_sgk_matrahi=data[4]
                            bordro1.temmuz_sgk_kesintisi=data[5]
                            bordro1.temmuz_issizlik_kesintisi=data[6]
                            bordro1.temmuz_vergi_matrahi=data[7]
                            bordro1.temmuz_kumulatif_vergi=data[8]
                            bordro1.temmuz_istisna_oncesi_gelir=data[9]
                            bordro1.temmuz_kumulatif_asgari_ucret=data[10]
                            bordro1.temmuz_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.temmuz_damga_vergisi=data[12]
                            bordro1.temmuz_gelir_vergisi=data[13]
                            bordro1.temmuz_net_ucret=data[14]
                            bordro1.temmuz_isveren_sgk_kesintisi=data[15]
                            bordro1.temmuz_isveren_issizlik_kesintisi=data[16]
                            bordro1.temmuz_toplam_sgk_kesintisi=data[17]
                            bordro1.temmuz_sgk_istisnasi=data[18]
                            bordro1.temmuz_odenecek_sgk=data[19]
                            bordro1.temmuz_odenecek_gelir_vergisi=data[21]
                            bordro1.temmuz_odenecek_damga_vergisi=data[22]
                            bordro1.temmuz_istisna_oncesi_damga=data[23]
                            bordro1.temmuz_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.temmuz_toplam_maliyet=data[25]
                            bordro1.temmuz_vergi_dilimi=data[26]
                            bordro1.temmuz_gelir_vergisi_istisnasi=data[27]
                            bordro1.temmuz_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="agustos":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari8=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi8=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun8=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.agustos_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.agustos_brut=data[0]
                            bordro1.agustos_calisilan_gun=data[1]
                            bordro1.agustos_arge_gun=data[2]
                            bordro1.agustos_bordroyaesasbrut=data[3]
                            bordro1.agustos_sgk_matrahi=data[4]
                            bordro1.agustos_sgk_kesintisi=data[5]
                            bordro1.agustos_issizlik_kesintisi=data[6]
                            bordro1.agustos_vergi_matrahi=data[7]
                            bordro1.agustos_kumulatif_vergi=data[8]
                            bordro1.agustos_istisna_oncesi_gelir=data[9]
                            bordro1.agustos_kumulatif_asgari_ucret=data[10]
                            bordro1.agustos_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.agustos_damga_vergisi=data[12]
                            bordro1.agustos_gelir_vergisi=data[13]
                            bordro1.agustos_net_ucret=data[14]
                            bordro1.agustos_isveren_sgk_kesintisi=data[15]
                            bordro1.agustos_isveren_issizlik_kesintisi=data[16]
                            bordro1.agustos_toplam_sgk_kesintisi=data[17]
                            bordro1.agustos_sgk_istisnasi=data[18]
                            bordro1.agustos_odenecek_sgk=data[19]
                            bordro1.agustos_odenecek_gelir_vergisi=data[21]
                            bordro1.agustos_odenecek_damga_vergisi=data[22]
                            bordro1.agustos_istisna_oncesi_damga=data[23]
                            bordro1.agustos_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.agustos_toplam_maliyet=data[25]
                            bordro1.agustos_vergi_dilimi=data[26]
                            bordro1.agustos_gelir_vergisi_istisnasi=data[27]
                            bordro1.agustos_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="eylul":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari9=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi9=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun9=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.eylul_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.eylul_brut=data[0]
                            bordro1.eylul_calisilan_gun=data[1]
                            bordro1.eylul_arge_gun=data[2]
                            bordro1.eylul_bordroyaesasbrut=data[3]
                            bordro1.eylul_sgk_matrahi=data[4]
                            bordro1.eylul_sgk_kesintisi=data[5]
                            bordro1.eylul_issizlik_kesintisi=data[6]
                            bordro1.eylul_vergi_matrahi=data[7]
                            bordro1.eylul_kumulatif_vergi=data[8]
                            bordro1.eylul_istisna_oncesi_gelir=data[9]
                            bordro1.eylul_kumulatif_asgari_ucret=data[10]
                            bordro1.eylul_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.eylul_damga_vergisi=data[12]
                            bordro1.eylul_gelir_vergisi=data[13]
                            bordro1.eylul_net_ucret=data[14]
                            bordro1.eylul_isveren_sgk_kesintisi=data[15]
                            bordro1.eylul_isveren_issizlik_kesintisi=data[16]
                            bordro1.eylul_toplam_sgk_kesintisi=data[17]
                            bordro1.eylul_sgk_istisnasi=data[18]
                            bordro1.eylul_odenecek_sgk=data[19]
                            bordro1.eylul_odenecek_gelir_vergisi=data[21]
                            bordro1.eylul_odenecek_damga_vergisi=data[22]
                            bordro1.eylul_istisna_oncesi_damga=data[23]
                            bordro1.eylul_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.eylul_toplam_maliyet=data[25]
                            bordro1.eylul_vergi_dilimi=data[26]
                            bordro1.eylul_gelir_vergisi_istisnasi=data[27]
                            bordro1.eylul_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="ekim":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari10=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi10=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun10=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.ekim_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.ekim_brut=data[0]
                            bordro1.ekim_calisilan_gun=data[1]
                            bordro1.ekim_arge_gun=data[2]
                            bordro1.ekim_bordroyaesasbrut=data[3]
                            bordro1.ekim_sgk_matrahi=data[4]
                            bordro1.ekim_sgk_kesintisi=data[5]
                            bordro1.ekim_issizlik_kesintisi=data[6]
                            bordro1.ekim_vergi_matrahi=data[7]
                            bordro1.ekim_kumulatif_vergi=data[8]
                            bordro1.ekim_istisna_oncesi_gelir=data[9]
                            bordro1.ekim_kumulatif_asgari_ucret=data[10]
                            bordro1.ekim_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.ekim_damga_vergisi=data[12]
                            bordro1.ekim_gelir_vergisi=data[13]
                            bordro1.ekim_net_ucret=data[14]
                            bordro1.ekim_isveren_sgk_kesintisi=data[15]
                            bordro1.ekim_isveren_issizlik_kesintisi=data[16]
                            bordro1.ekim_toplam_sgk_kesintisi=data[17]
                            bordro1.ekim_sgk_istisnasi=data[18]
                            bordro1.ekim_odenecek_sgk=data[19]
                            bordro1.ekim_odenecek_gelir_vergisi=data[21]
                            bordro1.ekim_odenecek_damga_vergisi=data[22]
                            bordro1.ekim_istisna_oncesi_damga=data[23]
                            bordro1.ekim_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.ekim_toplam_maliyet=data[25]
                            bordro1.ekim_vergi_dilimi=data[26]
                            bordro1.ekim_gelir_vergisi_istisnasi=data[27]
                            bordro1.ekim_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="kasim":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari11=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi11=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun11=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.kasim_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.kasim_brut=data[0]
                            bordro1.kasim_calisilan_gun=data[1]
                            bordro1.kasim_arge_gun=data[2]
                            bordro1.kasim_bordroyaesasbrut=data[3]
                            bordro1.kasim_sgk_matrahi=data[4]
                            bordro1.kasim_sgk_kesintisi=data[5]
                            bordro1.kasim_issizlik_kesintisi=data[6]
                            bordro1.kasim_vergi_matrahi=data[7]
                            bordro1.kasim_kumulatif_vergi=data[8]
                            bordro1.kasim_istisna_oncesi_gelir=data[9]
                            bordro1.kasim_kumulatif_asgari_ucret=data[10]
                            bordro1.kasim_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.kasim_damga_vergisi=data[12]
                            bordro1.kasim_gelir_vergisi=data[13]
                            bordro1.kasim_net_ucret=data[14]
                            bordro1.kasim_isveren_sgk_kesintisi=data[15]
                            bordro1.kasim_isveren_issizlik_kesintisi=data[16]
                            bordro1.kasim_toplam_sgk_kesintisi=data[17]
                            bordro1.kasim_sgk_istisnasi=data[18]
                            bordro1.kasim_odenecek_sgk=data[19]
                            bordro1.kasim_odenecek_gelir_vergisi=data[21]
                            bordro1.kasim_odenecek_damga_vergisi=data[22]
                            bordro1.kasim_istisna_oncesi_damga=data[23]
                            bordro1.kasim_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.kasim_toplam_maliyet=data[25]
                            bordro1.kasim_vergi_dilimi=data[26]
                            bordro1.kasim_gelir_vergisi_istisnasi=data[27]
                            bordro1.kasim_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()
                        elif ay=="aralik":
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(maas_tutari12=request.POST.get("maas"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(gunsayisi12=request.POST.get("maas1"+str(i)+"").replace(",","."))
                            maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).update(argegun12=request.POST.get("maas2"+str(i)+"").replace(",","."))
                            data=hesaplama1(request.POST.get("aylar"),maas.objects.get(calisan_id=employees[i-1],yil=date.today().year).id,employees[i-1].id)
                            bordro1.aralik_kanun_no=employees[i-1].calisan_tesvik
                            bordro1.aralik_brut=data[0]
                            bordro1.aralik_calisilan_gun=data[1]
                            bordro1.aralik_arge_gun=data[2]
                            bordro1.aralik_bordroyaesasbrut=data[3]
                            bordro1.aralik_sgk_matrahi=data[4]
                            bordro1.aralik_sgk_kesintisi=data[5]
                            bordro1.aralik_issizlik_kesintisi=data[6]
                            bordro1.aralik_vergi_matrahi=data[7]
                            bordro1.aralik_kumulatif_vergi=data[8]
                            bordro1.aralik_istisna_oncesi_gelir=data[9]
                            bordro1.aralik_kumulatif_asgari_ucret=data[10]
                            bordro1.aralik_asgari_gelir_vergisi_istisnasi=data[11]
                            bordro1.aralik_damga_vergisi=data[12]
                            bordro1.aralik_gelir_vergisi=data[13]
                            bordro1.aralik_net_ucret=data[14]
                            bordro1.aralik_isveren_sgk_kesintisi=data[15]
                            bordro1.aralik_isveren_issizlik_kesintisi=data[16]
                            bordro1.aralik_toplam_sgk_kesintisi=data[17]
                            bordro1.aralik_sgk_istisnasi=data[18]
                            bordro1.aralik_odenecek_sgk=data[19]
                            bordro1.aralik_odenecek_gelir_vergisi=data[21]
                            bordro1.aralik_odenecek_damga_vergisi=data[22]
                            bordro1.aralik_istisna_oncesi_damga=data[23]
                            bordro1.aralik_asgari_damga_vergisi_istisnasi=data[24]
                            bordro1.aralik_toplam_maliyet=data[25]
                            bordro1.aralik_vergi_dilimi=data[26]
                            bordro1.aralik_gelir_vergisi_istisnasi=data[27]
                            bordro1.aralik_damga_vergisi_istisnasi=data[28]
                            bordro1.bordro_kumularifasgariucret=data[11]
                            bordro1.bordro_kumularivergi=data[8]
                            bordro1.save()

                    else:
                        print("maas yok")
        
        if form.is_valid():
            for i in range(1,len(employees)+1):               
                if "pdf"+str(i) in request.POST:
                    if maas.objects.filter(calisan_id=employees[i-1],yil=date.today().year).exists():
                        maas1=maas.objects.get(calisan_id=employees[i-1],yil=date.today().year)
                        veri=form.cleaned_data.get("deneme")
                        aylar=form.cleaned_data.get("aylar")
                        print(aylar)
                        bordro1=bordro.objects.get(maas_id=maas1.id)
                        calisan1=calisan.objects.get(id=bordro1.calisan_id_id)
                        sirket1=sirket.objects.get(id=employees[i-1].calisan_sirket_id_id)
                        buffer=io.BytesIO()
                        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

                        p=canvas.Canvas(buffer)
                        p.setFont('Vera', 5)
                        x=2.5
                        y=19
                        p.setPageSize( landscape(A4) )

                        response=FileResponse(content_type ='application/ms-excel')
                        response['Content-Disposition'] = 'attachment; filename="bordro.xls"'
                        wb=xlwt.Workbook(encoding='utf-8')
                        ws=wb.add_sheet('Bordro')
                        row_num=0
                        font_style=xlwt.XFStyle()
                        font_style.font.bold=True

                        p.line(1*cm, (y+1)*cm, 28.5*cm, (y+1)*cm)#üst çizgi
                        p.drawString(2*cm, (y+0.7)*cm, "Firma Adı")
                        p.drawString(5.2*cm, (y+0.7)*cm, sirket1.sirket_adi)
                        p.line(1*cm, (y+0.5)*cm, 28.5*cm, (y+0.5)*cm)#üstün altı
                        p.line(1*cm, (y+0)*cm, 28.5*cm, (y+0)*cm)#alt çizgi
                        p.drawString(2*cm, (y+0.2)*cm, "Sgk İşyeri Numarası")
                        p.line(1*cm, (y-(0.5))*cm, 28.5*cm, (y-(0.5))*cm)#sağ çizgi
                        p.drawString(2*cm, (y-0.3)*cm, "Adres")
                        p.drawString(5.2*cm, (y-0.3)*cm, sirket1.sirket_adres)
                        p.line(1*cm, (y-1)*cm, 28.5*cm, (y-1)*cm)#sağ çizgi
                        p.drawString(2*cm, (y-0.8)*cm, "Vergi Dairesi")
                        p.drawString(5.2*cm, (y-0.8)*cm, sirket1.sirket_vergi_dairesi.vd_adi)
                        p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#sağ çizgi
                        p.drawString(2*cm, (y-1.3)*cm, "Vergi Numarası")
                        p.drawString(5.2*cm, (y-1.3)*cm, sirket1.sirket_vergi_numarasi)
                        p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
                        p.drawString(2*cm, (y-1.8)*cm, "Mersis Numarası")
                        p.drawString(5.2*cm, (y-1.8)*cm, sirket1.sirket_mersis_no)
                        p.line(1*cm, (y-2)*cm, 1*cm, (y+1)*cm)#sol çizgi
                        p.line(5*cm, (y-2)*cm, 5*cm, (y+1)*cm)#sağ çizgi
                        p.line(28.5*cm, (y-2)*cm, 28.5*cm, (y+1)*cm)#sağ çizgi
                        ## üst taraf
                        y=y-2
                        p.line(1*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#üst çizgi
                        p.drawString(1.1*cm, (y-1)*cm, "Ad-Soyad")
                        p.drawString(1.1*cm, (y-1.3)*cm, "Tc Kimlik No")
                        p.drawString(1.1*cm, (y-1.8)*cm, calisan1.calisan_adi + " " + calisan1.calisan_soyadi)
                        p.drawString(1.1*cm, (y-2.3)*cm, calisan1.calisan_tc)
                        p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#üstün altı
                        p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
                        p.line(1*cm, (y-2.5)*cm, 28.5*cm, (y-2.5)*cm)#sol çizgi
                        p.line(1*cm, (y-2.5)*cm, 1*cm, (y-0.7)*cm)#sağ çizgi
                        p.line(28.5*cm, (y-2.5)*cm, 28.5*cm, (y-0.7)*cm)#sağ çizgi
                        p.line(2.8*cm, (y-2.5)*cm, 2.8*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(2.9*cm, (y-1)*cm, "Kanun No")
                        p.drawString(2.9*cm, (y-1.3)*cm, "Prim Günü")
                        if aylar[0] == 'ocak':
                            if bordro1.ocak_kanun_no=="pick1":
                                p.drawString(2.9*cm, (y-1.8)*cm, "Standart")
                            else:
                                p.drawString(2.9*cm, (y-1.8)*cm, bordro1.ocak_kanun_no)

                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi1))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ocak_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ocak_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ocak_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ocak_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ocak_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ocak_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ocak_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ocak_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ocak_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ocak_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ocak_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ocak_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ocak_damga_vergisi_istisnasi))
                        elif aylar[0] == "subat":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.subat_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi2))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.subat_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.subat_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.subat_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.subat_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.subat_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.subat_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.subat_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.subat_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.subat_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.subat_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.subat_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.subat_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.subat_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.subat_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.subat_damga_vergisi_istisnasi))
                        elif aylar[0] == "mart":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.mart_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi3))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.mart_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.mart_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.mart_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.mart_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.mart_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.mart_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.mart_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.mart_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.mart_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.mart_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.mart_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.mart_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.mart_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.mart_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.mart_damga_vergisi_istisnasi))
                        elif aylar[0] == "nisan":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.nisan_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi4))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.nisan_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.nisan_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.nisan_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.nisan_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.nisan_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.nisan_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.nisan_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.nisan_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.nisan_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.nisan_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.nisan_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.nisan_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.nisan_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.nisan_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.nisan_damga_vergisi_istisnasi))
                        elif aylar[0] == "mayis":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.mayis_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi5))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.mayis_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.mayis_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.mayis_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.mayis_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.mayis_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.mayis_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.mayis_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.mayis_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.mayis_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.mayis_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.mayis_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.mayis_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.mayis_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.mayis_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.mayis_damga_vergisi_istisnasi))
                        elif aylar[0] == "haziran":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.haziran_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi6))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.haziran_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.haziran_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.haziran_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.haziran_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.haziran_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.haziran_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.haziran_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.haziran_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.haziran_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.haziran_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.haziran_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.haziran_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.haziran_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.haziran_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.haziran_damga_vergisi_istisnasi))
                        elif aylar[0] == "temmuz":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.temmuz_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi7))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.temmuz_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.temmuz_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.temmuz_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.temmuz_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.temmuz_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.temmuz_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.temmuz_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.temmuz_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.temmuz_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.temmuz_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.temmuz_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.temmuz_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.temmuz_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.temmuz_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.temmuz_damga_vergisi_istisnasi))
                        elif aylar[0] == "agustos":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.agustos_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi8))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.agustos_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.agustos_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.agustos_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.agustos_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.agustos_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.agustos_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.agustos_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.agustos_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.agustos_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.agustos_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.agustos_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.agustos_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.agustos_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.agustos_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.agustos_damga_vergisi_istisnasi))
                        elif aylar[0] == "eylul":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.eylul_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi9))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.eylul_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.eylul_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.eylul_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.eylul_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.eylul_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.eylul_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.eylul_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.eylul_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.eylul_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.eylul_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.eylul_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.eylul_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.eylul_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.eylul_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.eylul_damga_vergisi_istisnasi))
                        elif aylar[0] == "ekim":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.ekim_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi10))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ekim_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ekim_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ekim_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ekim_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ekim_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ekim_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ekim_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ekim_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ekim_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ekim_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ekim_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ekim_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ekim_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ekim_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ekim_damga_vergisi_istisnasi))
                        elif aylar[0] == "kasim":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.kasim_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi11))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.kasim_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.kasim_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.kasim_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.kasim_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.kasim_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.kasim_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.kasim_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.kasim_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.kasim_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.kasim_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.kasim_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.kasim_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.kasim_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.kasim_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.kasim_damga_vergisi_istisnasi))
                        elif aylar[0] == "aralik":
                            p.drawString(2.9*cm, (y-1.8)*cm, bordro1.aralik_kanun_no)
                            p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi12))
                            p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.aralik_brut))
                            p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.aralik_brut))
                            p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.aralik_sgk_kesintisi))
                            p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.aralik_issizlik_kesintisi))
                            p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.aralik_kumulatif_vergi))
                            p.drawString(14*cm, (y-1.8)*cm, str(bordro1.aralik_vergi_matrahi))
                            p.drawString(14*cm, (y-2.3)*cm, str(bordro1.aralik_istisna_oncesi_gelir))
                            p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.aralik_asgari_gelir_vergisi_istisnasi))
                            p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.aralik_gelir_vergisi))
                            p.drawString(18*cm, (y-1.8)*cm, str(bordro1.aralik_damga_vergisi))
                            p.drawString(18*cm, (y-2.3)*cm, str(bordro1.aralik_net_ucret))
                            p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.aralik_isveren_sgk_kesintisi))
                            p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.aralik_isveren_issizlik_kesintisi))
                            p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.aralik_gelir_vergisi_istisnasi))
                            p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.aralik_damga_vergisi_istisnasi))
                        p.line(4*cm, (y-2.5)*cm, 4*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(4.1*cm, (y-1)*cm, "Brüt Ücret")
                        p.drawString(4.1*cm, (y-1.3)*cm, "Sair Öd.")

                        p.line(5.8*cm, (y-2.5)*cm, 5.8*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(5.9*cm, (y-1)*cm, "Sair Öd.2")
                        p.drawString(5.9*cm, (y-1.3)*cm, "Sair Öd.3")
                        p.line(7.3*cm, (y-2.5)*cm, 7.3*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(7.4*cm, (y-1)*cm, "Fazla Mesai")
                        p.drawString(7.4*cm, (y-1.3)*cm, "Kesinti 1")
                        p.line(9*cm, (y-2.5)*cm, 9*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(9.1*cm, (y-1)*cm, "Kesinti 2")
                        p.drawString(9.1*cm, (y-1.3)*cm, "Kesinti 3")
                        p.line(10.3*cm, (y-2.5)*cm, 10.3*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(10.4*cm, (y-1)*cm, "Toplam Brüt")
                        p.drawString(10.4*cm, (y-1.3)*cm, "SGK İşçi Payı")

                        p.line(12.3*cm, (y-2.5)*cm, 12.3*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(12.4*cm, (y-1)*cm, "SGK İşçi İşz.")
                        p.drawString(12.4*cm, (y-1.3)*cm, "Küm. Vergi M.")

                        p.line(13.9*cm, (y-2.5)*cm, 13.9*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(14*cm, (y-1)*cm, "Vergi Matrahı")
                        p.drawString(14*cm, (y-1.3)*cm, "Gelir Vergisi")

                        p.line(15.3*cm, (y-2.5)*cm, 15.3*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(15.4*cm, (y-1)*cm, "Asgari Ü. Gelir V. İst.")
                        p.drawString(15.4*cm, (y-1.3)*cm, "Kalan Gelir Vergisi")

                        p.line(17.9*cm, (y-2.5)*cm, 17.9*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(18*cm, (y-1)*cm, "Damga Vergisi")
                        p.drawString(18*cm, (y-1.3)*cm, "Net Ücret")

                        p.line(21*cm, (y-2.5)*cm, 21*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(21.1*cm, (y-1.3)*cm, "SGK İsveren Primi")
                        p.drawString(21.1*cm, (y-1)*cm, "SGK İşveren İşsizlik Primi")

                        p.line(23.8*cm, (y-2.5)*cm, 23.8*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(23.9*cm, (y-1.3)*cm, "Gelir Vergisi İstisnası")
                        p.drawString(23.9*cm, (y-1)*cm, "Damga Vergisi İstisnası")

                        p.line(26.4*cm, (y-2.5)*cm, 26.4*cm, (y-0.7)*cm)#sağ çizgi
                        p.drawString(26.5*cm, (y-1.3)*cm, "Sgk Prim İstisnası")
                        p.drawString(26.5*cm, (y-1)*cm, "Sgk İşsizlik Prim İst.")
                        #orta kısım
                        y=y-7
                        p.line(1*cm, (y-0.7)*cm, 5.25*cm, (y-0.7)*cm)#üst çizgi
                        p.line(5.85*cm, (y-0.7)*cm, 10.1*cm, (y-0.7)*cm)#alt çizgi
                        p.line(10.7*cm, (y-0.7)*cm, 14.95*cm, (y-0.7)*cm)#alt çizgi
                        p.line(15.55*cm, (y-0.7)*cm, 19.8*cm, (y-0.7)*cm)#alt çizgi
                        p.line(20.4*cm, (y-0.7)*cm, 24.65*cm, (y-0.7)*cm)#alt çizgi
                        p.line(25.25*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#alt çizgi
                        p.line(1*cm, (y-0.7)*cm, 1*cm, (y-9)*cm)#üst çizgi
                        p.line(5.25*cm, (y-0.7)*cm, 5.25*cm, (y-9)*cm)#üst çizgi
                        p.line(5.85*cm, (y-0.7)*cm, 5.85*cm, (y-9)*cm)#üst çizgi
                        p.line(10.1*cm, (y-0.7)*cm, 10.1*cm, (y-9)*cm)#üst çizgi
                        p.line(10.7*cm, (y-0.7)*cm, 10.7*cm, (y-9)*cm)#üst çizgi
                        p.line(14.95*cm, (y-0.7)*cm, 14.95*cm, (y-9)*cm)#üst çizgi
                        p.line(15.55*cm, (y-0.7)*cm, 15.55*cm, (y-9)*cm)#üst çizgi
                        p.line(19.8*cm, (y-0.7)*cm, 19.8*cm, (y-9)*cm)#üst çizgi
                        p.line(20.4*cm, (y-0.7)*cm, 20.4*cm, (y-9)*cm)#üst çizgi
                        p.line(24.65*cm, (y-0.7)*cm, 24.65*cm, (y-9)*cm)#üst çizgi
                        p.line(25.25*cm, (y-0.7)*cm, 25.25*cm, (y-9)*cm)#üst çizgi
                        p.line(28.5*cm, (y-0.7)*cm, 28.5*cm, (y-9)*cm)#üst çizgi
                        p.line(1*cm, (y-9)*cm, 5.25*cm, (y-9)*cm)
                        p.drawString(2.6*cm, (y-1.1)*cm, "Brüt Toplam")
                        p.line(5.85*cm, (y-9)*cm, 10.1*cm, (y-9)*cm)
                        p.drawString(7.8*cm, (y-1.1)*cm, "SGK")
                        p.line(10.7*cm, (y-9)*cm, 14.95*cm, (y-9)*cm)
                        p.drawString(12.3*cm, (y-1.1)*cm, "Gelir Vergisi")
                        p.line(15.55*cm, (y-9)*cm, 19.8*cm, (y-9)*cm)
                        p.drawString(17.1*cm, (y-1.1)*cm, "Damga Vergisi")
                        p.line(20.4*cm, (y-9)*cm, 24.65*cm, (y-9)*cm)
                        p.drawString(22.1*cm, (y-1.1)*cm, "Net Ücret")
                        p.line(25.25*cm, (y-9)*cm, 28.5*cm, (y-9)*cm)
                        p.drawString(26.6*cm, (y-1.1)*cm, "Günler")
                        p.line(3*cm, (y-1.3)*cm, 3*cm, (y-9)*cm)#üst çizgi
                        p.line(8*cm, (y-1.3)*cm, 8*cm, (y-9)*cm)#üst çizgi
                        p.line(12.7*cm, (y-1.3)*cm, 12.7*cm, (y-9)*cm)#üst çizgi
                        p.line(17.6*cm, (y-1.3)*cm, 17.6*cm, (y-9)*cm)#üst çizgi
                        p.line(22.5*cm, (y-1.3)*cm, 22.5*cm, (y-9)*cm)#üst çizgi
                        p.line(26.8*cm, (y-1.3)*cm, 26.8*cm, (y-9)*cm)#üst çizgi
                        p.line(1*cm, (y-1.3)*cm, 5.25*cm, (y-1.3)*cm)
                        p.drawString(1.2*cm, (y-1.7)*cm, "Brüt Ücret")
                        p.line(5.85*cm, (y-1.3)*cm, 10.1*cm, (y-1.3)*cm)
                        p.drawString(6.1*cm, (y-1.7)*cm, "SGK İşveren Payı")
                        p.line(10.7*cm, (y-1.3)*cm, 14.95*cm, (y-1.3)*cm)
                        p.drawString(10.8*cm, (y-1.7)*cm, "Hesaplanan Gelir V.")
                        p.line(15.55*cm, (y-1.3)*cm, 19.8*cm, (y-1.3)*cm)
                        p.drawString(15.6*cm, (y-1.7)*cm, "Hesaplanan Damga V.")
                        p.line(20.4*cm, (y-1.3)*cm, 24.65*cm, (y-1.3)*cm)
                        p.drawString(20.5*cm, (y-1.7)*cm, "Asıl Ücret")
                        p.line(25.25*cm, (y-1.3)*cm, 28.5*cm, (y-1.3)*cm)
                        p.drawString(25.4*cm, (y-1.7)*cm, "Çalışma Günü")
                        p.line(1*cm, (y-2)*cm, 5.25*cm, (y-2)*cm)
                        p.drawString(1.2*cm, (y-2.5)*cm, "Sair Ödeme1")
                        p.line(5.85*cm, (y-2)*cm, 10.1*cm, (y-2)*cm)
                        p.drawString(6.1*cm, (y-2.5)*cm, "Sgk İşçi Payı")
                        p.line(10.7*cm, (y-2)*cm, 14.95*cm, (y-2)*cm)
                        p.drawString(10.8*cm, (y-2.5)*cm, "ASgari Ü. Gelir V. İst.")
                        p.line(15.55*cm, (y-2)*cm, 19.8*cm, (y-2)*cm)
                        p.drawString(15.6*cm, (y-2.5)*cm, "İst. Damga Vergisi")
                        p.line(20.4*cm, (y-2)*cm, 24.65*cm, (y-2)*cm)
                        p.drawString(20.5*cm, (y-2.5)*cm, "Fazla Mesai")
                        p.line(25.25*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)
                        p.drawString(25.4*cm, (y-2.5)*cm, "Haftasonu Günü")
                        p.line(1*cm, (y-2.7)*cm, 5.25*cm, (y-2.7)*cm)
                        p.drawString(1.2*cm, (y-3.2)*cm, "Sair Ödeme2")
                        p.line(5.85*cm, (y-2.7)*cm, 10.1*cm, (y-2.7)*cm)
                        p.drawString(6.1*cm, (y-3.2)*cm, "Sgk İşv. İşz. Payı")
                        p.line(10.7*cm, (y-2.7)*cm, 14.95*cm, (y-2.7)*cm)
                        p.drawString(10.8*cm, (y-3.2)*cm, "Terkin E. Gelir V.")
                        p.line(15.55*cm, (y-2.7)*cm, 19.8*cm, (y-2.7)*cm)
                        p.line(20.4*cm, (y-2.7)*cm, 24.65*cm, (y-2.7)*cm)
                        p.drawString(20.5*cm, (y-3.2)*cm, "Sair Ödeme 1")
                        p.line(25.25*cm, (y-2.7)*cm, 28.5*cm, (y-2.7)*cm)
                        p.drawString(25.5*cm, (y-3.2)*cm, "Genel Tatil")
                        p.line(1*cm, (y-3.4)*cm, 5.25*cm, (y-3.4)*cm)
                        p.drawString(1.2*cm, (y-3.9)*cm, "Sair Ödeme3")
                        p.line(5.85*cm, (y-3.4)*cm, 10.1*cm, (y-3.4)*cm)
                        p.drawString(6.1*cm, (y-3.9)*cm, "Sgk İşçi İşz. Payı")
                        p.line(10.7*cm, (y-3.4)*cm, 14.95*cm, (y-3.4)*cm)

                        p.line(20.4*cm, (y-3.4)*cm, 24.65*cm, (y-3.4)*cm)
                        p.drawString(20.5*cm, (y-3.9)*cm, "Sair Ödeme 2")
                        p.line(25.25*cm, (y-3.4)*cm, 28.5*cm, (y-3.4)*cm)
                        p.drawString(25.5*cm, (y-3.9)*cm, "Yıllık İzin")
                        p.line(1*cm, (y-4.1)*cm, 5.25*cm, (y-4.1)*cm)
                        p.drawString(1.2*cm, (y-4.6)*cm, "Fazla Mesai")
                        p.line(5.85*cm, (y-4.1)*cm, 10.1*cm, (y-4.1)*cm)
                        p.drawString(6.1*cm, (y-4.6)*cm, "Sgk Prim Desteği İst.")
                        p.line(20.4*cm, (y-4.1)*cm, 24.65*cm, (y-4.1)*cm)
                        p.drawString(20.5*cm, (y-4.6)*cm, "Sair Ödeme 3")
                        p.line(25.25*cm, (y-4.1)*cm, 28.5*cm, (y-4.1)*cm)
                        p.drawString(25.5*cm, (y-4.6)*cm, "Sıhhi İzin")
                        p.line(1*cm, (y-4.8)*cm, 5.25*cm, (y-4.8)*cm)
                        p.drawString(1.2*cm, (y-5.3)*cm, "Kesinti 1")
                        p.line(5.85*cm, (y-4.8)*cm, 10.1*cm, (y-4.8)*cm)
                        p.drawString(6.1*cm, (y-5.3)*cm, "Sgk İşs. Prim Des. İst.")
                        p.line(20.4*cm, (y-4.8)*cm, 24.65*cm, (y-4.8)*cm)
                        p.drawString(20.5*cm, (y-5.3)*cm, "Kesinti 1")
                        p.line(25.25*cm, (y-4.8)*cm, 28.5*cm, (y-4.8)*cm)
                        p.drawString(25.5*cm, (y-5.3)*cm, "Ucretsiz İzin")
                        p.line(1*cm, (y-5.5)*cm, 5.25*cm, (y-5.5)*cm)
                        p.drawString(1.2*cm, (y-6)*cm, "Kesinti 2")
                        p.line(5.85*cm, (y-5.5)*cm, 10.1*cm, (y-5.5)*cm)
                        p.line(20.4*cm, (y-5.5)*cm, 24.65*cm, (y-5.5)*cm)
                        p.drawString(20.5*cm, (y-6)*cm, "Kesinti 2")
                        p.line(25.25*cm, (y-5.5)*cm, 28.5*cm, (y-5.5)*cm)
                        p.drawString(25.5*cm, (y-6)*cm, "Ücretli İzin")
                        p.line(1*cm, (y-6.2)*cm, 5.25*cm, (y-6.2)*cm)
                        p.drawString(1.2*cm, (y-6.7)*cm, "Kesinti 3")
                        p.line(20.4*cm, (y-6.2)*cm, 24.65*cm, (y-6.2)*cm)
                        p.drawString(20.5*cm, (y-6.7)*cm, "Kesinti 3")
                        p.line(25.25*cm, (y-6.2)*cm, 28.5*cm, (y-6.2)*cm)
                        p.drawString(25.5*cm, (y-6.7)*cm, "Mazeret İzin")
                        p.line(1*cm, (y-6.9)*cm, 5.25*cm, (y-6.9)*cm)
                        p.line(20.4*cm, (y-6.9)*cm, 24.65*cm, (y-6.9)*cm)
                        p.line(25.25*cm, (y-6.9)*cm, 28.5*cm, (y-6.9)*cm)
                        p.drawString(25.5*cm, (y-7.4)*cm, "Prim Günü")

                        p.line(1*cm, (y-7.6)*cm, 5.25*cm, (y-7.6)*cm)

                        p.line(5.85*cm, (y-7.6)*cm, 10.1*cm, (y-7.6)*cm)

                        p.line(10.7*cm, (y-7.6)*cm, 14.95*cm, (y-7.6)*cm)

                        p.line(15.55*cm, (y-7.6)*cm, 19.8*cm, (y-7.6)*cm)

                        p.line(20.4*cm, (y-7.6)*cm, 24.65*cm, (y-7.6)*cm)

                        p.line(25.25*cm, (y-7.6)*cm, 28.5*cm, (y-7.6)*cm)
                        p.line(1*cm, (y-8.3)*cm, 5.25*cm, (y-8.3)*cm)
                        p.drawString(1.2*cm, (y-8.7)*cm, "Brüt Toplam")
                        p.line(5.85*cm, (y-8.3)*cm, 10.1*cm, (y-8.3)*cm)
                        p.drawString(10.7*cm, (y-8.7)*cm, "Ödenecek SGK Primi")

                        p.line(10.7*cm, (y-8.3)*cm, 14.95*cm, (y-8.3)*cm)
                        p.drawString(15.55*cm, (y-8.7)*cm, "Ödenecek Gelir V.")
                        p.line(15.55*cm, (y-8.3)*cm, 19.8*cm, (y-8.3)*cm)
                        p.drawString(20.5*cm, (y-8.7)*cm, "Ödenecek Damga V.")
                        p.line(20.4*cm, (y-8.3)*cm, 24.65*cm, (y-8.3)*cm)
                        p.drawString(25.5*cm, (y-8.7)*cm, "Net Ödenecek Ücret")
                        p.line(25.25*cm, (y-8.3)*cm, 28.5*cm, (y-8.3)*cm)

                        tur=form.cleaned_data.get('export')

                        if tur == "pdf":
                            p.showPage()
                            p.save()
                            buffer.seek(0)
                            return FileResponse(buffer, as_attachment=False, filename='bordro.pdf')
                        elif tur == "xls":
                            output = io.BytesIO()
                            wb.save(output)
                            output.seek(0)
                            return FileResponse(output, as_attachment=False, filename='bordro.xls')
                        else:
                            return HttpResponseNotFound("404")

        return redirect(reverse('user:employeelist', kwargs={'id':id}))



    if( request.user.groups.filter(name='mali_musavir').exists() or request.user.groups.filter(name='admin').exists() or request.user.groups.filter(name='muhasebe').exists()  ):
        employees=calisan.objects.filter(calisan_sirket_id=company,calisan_sube_id=sube1).order_by('calisan_soyadi')


        if employees is not None:
            for i in employees:
                if maas.objects.filter(calisan_id=i,yil=date.today().year).exists():
                    deneme.append(maas.objects.filter(calisan_id=i,yil=date.today().year))

        if deneme is not None:
            for i in deneme:
                if bordro.objects.filter(maas_id=i[0].id,).exists():
                    deneme1.append(bordro.objects.filter(maas_id=i[0].id))

        calisantab=False
        month=datetime.now().month
        maxuser=subs.objects.filter(id=company.sirket_uyelik.id)
        maxuser=maxuser[0].subs_maksimum_calisan
        calisansayi=(employees.count())

        uyelik=True
        uyelik1=True
        if subs.objects.filter(id=company.sirket_uyelik_id).exists():
            subs1=subs.objects.get(id=company.sirket_uyelik_id)
        if subs1.subs_baslangic_tarihi + timedelta(subs1.subs_gun_sayisi)<datetime.now().date():
             subs1.subs_aktiflik=False
             subs1.save()
        if subs.objects.get(id=company.sirket_uyelik_id).subs_aktiflik==False:
            uyelik=False
        if subs.objects.get(id=company.sirket_uyelik_id).subs_maksimum_calisan<=calisansayi:
            uyelik1=False




        context={
            'employees':employees,
            'calisantab':calisantab,
            'sirketid':company.id,
            'sube':sube1.id,
            'deneme':deneme,
            'aylar':aylar,
            'bordro':deneme1,
            'month':month,
            'form':form,
            'maxuser':maxuser,
            'calisansayi':calisansayi,
            'uyelik':uyelik,
            'uyelik1':uyelik1,
        }
        return render(request,'listemployee.html',context)

    elif(user1 is not None):

        if( user1.calisan_sirket_id.id==company.id and user1.calisan_sube_id.id==sube1.id):
            calisantab=False

            employees=calisan.objects.filter(calisan_sirket_id=id)

            context={
                'employees':employees,
                'calisantab':calisantab,
                'sirketid':id,
                'deneme':deneme,
                'form':form,
                
            }
            return render(request,'listemployee.html',context)
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponseNotFound("Yetkisiz Erişim")


@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def detailcompany(request,id):
    try:
        company=sirket.objects.get(id=id)

    except company.DoesNotExist:
        company=None

    if company is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')


    if request.user.groups.filter(name='mali_musavir').exists():

        if company.sirket_mali_musavir_id!=request.user:

            return HttpResponseNotFound('<h1>Page not found</h1>')
    elif request.user.groups.filter(name='muhasebe').exists():
        if calisan.objects.get(calisan_id=request.user).calisan_sirket_id!=company:
            return HttpResponseNotFound('<h1>Page not found</h1>')


    return listemployee(request,id)
@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists() or u.groups.filter(name='calisan').exists())

def detailemployee(request,id):

    if request.user.groups.filter(name='mali_musavir').exists():

        if not mali_sirket.objects.get(id=mali_musavir.objects.get(mali_musavir_id=request.user).mali_sirket_id_id).mali_sirket_bagli_sirketler.filter(id=calisan.objects.get(id=id).calisan_sirket_id_id).exists():
            return HttpResponseNotFound('<h1>Page not found</h1>')

    elif request.user.groups.filter(name='muhasebe').exists():

        if calisan.objects.get(calisan_id=request.user.id).calisan_sirket_id != calisan.objects.get(id=id).calisan_sirket_id:
            return HttpResponseNotFound("Yetkisiz Erişim")
    elif request.user.groups.filter(name='calisan').exists():
        if request.user.id != calisan.objects.get(id=id).calisan_id_id:
            return HttpResponseNotFound("Yetkisiz Erişim")
    employee=calisan.objects.get(id=id)
    user2=User.objects.get(id=employee.calisan_id_id)
    maass=maas.objects.filter(calisan_id=employee)

    aylar1={
        'Ocak':'1',
        'Şubat':'2',
        'Mart':'3',
        'Nisan':'4',
        'Mayıs':'5',
        'Haziran':'6',
        'Temmuz':'7',
        'Ağustos':'8',
        'Eylül':'9',
        'Ekim':'10',
        'Kasım':'11',
        'Aralık':'12',

    }






    context={
        'employee':employee,
        'maass':maass,
        'aylar':monthform(),
        'aylar1':aylar1,
        'mainpage':False,


    }

    return render(request,'employeedetail.html',context)
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter,landscape
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from django.http import FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import xlwt
from io import StringIO

def createpdf(request,id):

    form=denemeform(request.POST or None)
    if form.is_valid():
        veri=form.cleaned_data.get("deneme")
        aylar=form.cleaned_data.get("aylar")
        bordro1=bordro.objects.get(maas_id=id)
        maas1=maas.objects.get(id=id)
        calisan1=calisan.objects.get(id=bordro1.calisan_id_id)
        sirket1=sirket.objects.get(id=calisan1.calisan_sirket_id_id)
        buffer=io.BytesIO()
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

        p=canvas.Canvas(buffer)
        p.setFont('Vera', 5)
        x=2.5
        y=19
        p.setPageSize( landscape(A4) )

        response=FileResponse(content_type ='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="bordro.xls"'
        wb=xlwt.Workbook(encoding='utf-8')
        ws=wb.add_sheet('Bordro')
        row_num=0
        font_style=xlwt.XFStyle()
        font_style.font.bold=True
        # colums=[]
        # if "pick0" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"Brüt Ücret")
        #     colums.append("Brüt Ücret")
        #     x=x+2
        # if "pick1" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"Çalışılan Gün")
        #     colums.append("Çalışılan Gün")
        #     x=x+2
        # if "pick2" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"Bordro E. Brüt")
        #     colums.append("Bordro E. Brüt")
        #     x=x+3
        # if "pick3" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"SGK Kesintisi")
        #     colums.append("SGK Kesintisi")
        #     x=x+2
        # if "pick4" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"İşsizlik Kesintisi")
        #     colums.append("İşsizlik Kesintisi")
        #     x=x+3
        # if "pick5" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"Damga Vergisi")
        #     colums.append("Damga Vergisi")
        #     x=x+2.5
        # if "pick6" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"Gelir Vergisi")
        #     colums.append("Gelir Vergisi")
        #     x=x+2
        # if "pick7" in veri:
        #     p.drawString(x*cm,(y+1)*cm,"Net Ücret")
        #     colums.append("Net Ücret")
        #     x=x+2
        # for col_num in range(len(colums)):
        #     ws.write(row_num,col_num+1,colums[col_num],font_style)
        # for i in aylar:
        #     x=0.5
        #     row_num=row_num+1
        #     k=0

        #     if i == "maas_tutari1":#ocak
        #         p.drawString(x*cm, y*cm, str("Ocak"))
        #         ws.write(row_num,k,"Ocak")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.ocak_brut
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(brut))
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.ocak_calisilan_gun
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.ocak_bordroyaesasbrut
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.ocak_sgk_kesintisi
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.ocak_issizlik_kesintisi
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.ocak_damga_vergisi
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(damga))
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.ocak_gelir_vergisi
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             x=x+2
        #         if "pick7" in veri:

        #             net=bordro1.ocak_net_ucret
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             p.drawString(x*cm, y*cm, str(net))
        #             x=x+2

        #         y=y-1

        #     elif i=="maas_tutari2":
        #         p.drawString(x*cm, y*cm, str("Şubat"))
        #         ws.write(row_num,k,"Şubat")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.subat_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.subat_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2

        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.subat_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3

        #         if "pick3" in veri:
        #             sgkprimi=bordro1.subat_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.subat_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.subat_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.subat_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.subat_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari3":
        #         p.drawString(x*cm, y*cm, str("Mart"))
        #         ws.write(row_num,k,"Mart")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.mart_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2

        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.mart_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.mart_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.mart_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.mart_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.mart_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.mart_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.mart_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1
        #     elif i=="maas_tutari4":
        #         p.drawString(x*cm, y*cm, str("Nisan"))
        #         ws.write(row_num,k,"Nisan")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.nisan_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2

        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.nisan_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.nisan_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.nisan_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.nisan_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.nisan_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.nisan_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.nisan_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1
        #     elif i=="maas_tutari5":
        #         p.drawString(x*cm, y*cm, str("Mayıs"))
        #         ws.write(row_num,k,"Mayıs")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.mayis_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.mayis_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.mayis_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.mayis_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.mayis_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.mayis_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.mayis_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.mayis_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1
        #     elif i=="maas_tutari6":
        #         p.drawString(x*cm, y*cm, str("Haziran"))
        #         ws.write(row_num,k,"Haziran")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.haziran_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.haziran_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.haziran_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.haziran_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.haziran_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.haziran_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.haziran_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.haziran_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari7":
        #         p.drawString(x*cm, y*cm, str("Temmuz"))
        #         ws.write(row_num,k,"Temmuz")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.temmuz_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2

        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.temmuz_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.temmuz_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.temmuz_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.temmuz_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.temmuz_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.temmuz_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.temmuz_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari8":
        #         p.drawString(x*cm, y*cm, str("Ağustos"))
        #         ws.write(row_num,k,"Ağustos")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.agustos_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.agustos_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.agustos_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.agustos_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.agustos_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.agustos_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.agustos_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.agustos_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari9":
        #         p.drawString(x*cm, y*cm, str("Eylül"))
        #         ws.write(row_num,k,"Eylül")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.eylul_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2

        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.eylul_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.eylul_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.eylul_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.eylul_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.eylul_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.eylul_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.eylul_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari10":
        #         p.drawString(x*cm, y*cm, str("Ekim"))
        #         ws.write(row_num,k,"Ekim")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.ekim_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.ekim_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.ekim_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.ekim_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.ekim_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.ekim_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.ekim_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.ekim_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari11":
        #         p.drawString(x*cm, y*cm, str("Kasım"))
        #         ws.write(row_num,k,"Kasım")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.kasim_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.kasim_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.kasim_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.kasim_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.kasim_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.kasim_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.kasim_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.kasim_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1

        #     elif i=="maas_tutari12":
        #         p.drawString(x*cm, y*cm, str("Aralık"))
        #         ws.write(row_num,k,"Aralık")
        #         k=k+1
        #         x=x+2
        #         if "pick0" in veri:
        #             brut=bordro1.aralik_brut
        #             p.drawString(x*cm, y*cm, str(brut))
        #             ws.write(row_num,k,brut)
        #             k=k+1
        #             x=x+2
        #         if "pick1" in veri:
        #             calisilan_gun=bordro1.aralik_calisilan_gun
        #             p.drawString(x*cm, y*cm, str(calisilan_gun))
        #             ws.write(row_num,k,calisilan_gun)
        #             k=k+1
        #             x=x+2
        #         if "pick2" in veri:
        #             bordroyaesas=bordro1.aralik_bordroyaesasbrut
        #             p.drawString(x*cm, y*cm, str(bordroyaesas))
        #             ws.write(row_num,k,bordroyaesas)
        #             k=k+1
        #             x=x+3
        #         if "pick3" in veri:
        #             sgkprimi=bordro1.aralik_sgk_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkprimi))
        #             ws.write(row_num,k,sgkprimi)
        #             k=k+1
        #             x=x+2
        #         if "pick4" in veri:
        #             sgkissizlik=bordro1.aralik_issizlik_kesintisi
        #             p.drawString(x*cm, y*cm, str(sgkissizlik))
        #             ws.write(row_num,k,sgkissizlik)
        #             k=k+1
        #             x=x+3
        #         if "pick5" in veri:
        #             damga=bordro1.aralik_damga_vergisi
        #             p.drawString(x*cm, y*cm, str(damga))
        #             ws.write(row_num,k,damga)
        #             k=k+1
        #             x=x+2.5
        #         if "pick6" in veri:
        #             gelirvergisi=bordro1.aralik_gelir_vergisi
        #             p.drawString(x*cm, y*cm, str(gelirvergisi))
        #             ws.write(row_num,k,gelirvergisi)
        #             k=k+1
        #             x=x+2
        #         if "pick7" in veri:
        #             net=bordro1.aralik_net_ucret
        #             p.drawString(x*cm, y*cm, str(net))
        #             ws.write(row_num,k,net)
        #             k=k+1
        #             x=x+2
        #         y=y-1
        p.line(1*cm, (y+1)*cm, 28.5*cm, (y+1)*cm)#üst çizgi
        p.drawString(2*cm, (y+0.7)*cm, "Firma Adı")
        p.drawString(5.2*cm, (y+0.7)*cm, sirket1.sirket_adi)
        p.line(1*cm, (y+0.5)*cm, 28.5*cm, (y+0.5)*cm)#üstün altı
        p.line(1*cm, (y+0)*cm, 28.5*cm, (y+0)*cm)#alt çizgi
        p.drawString(2*cm, (y+0.2)*cm, "Sgk İşyeri Numarası")
        p.line(1*cm, (y-(0.5))*cm, 28.5*cm, (y-(0.5))*cm)#sağ çizgi
        p.drawString(2*cm, (y-0.3)*cm, "Adres")
        p.drawString(5.2*cm, (y-0.3)*cm, sirket1.sirket_adres)
        p.line(1*cm, (y-1)*cm, 28.5*cm, (y-1)*cm)#sağ çizgi
        p.drawString(2*cm, (y-0.8)*cm, "Vergi Dairesi")
        p.drawString(5.2*cm, (y-0.8)*cm, sirket1.sirket_vergi_dairesi.vd_adi)
        p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#sağ çizgi
        p.drawString(2*cm, (y-1.3)*cm, "Vergi Numarası")
        p.drawString(5.2*cm, (y-1.3)*cm, sirket1.sirket_vergi_numarasi)
        p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
        p.drawString(2*cm, (y-1.8)*cm, "Mersis Numarası")
        p.drawString(5.2*cm, (y-1.8)*cm, sirket1.sirket_mersis_no)
        p.line(1*cm, (y-2)*cm, 1*cm, (y+1)*cm)#sol çizgi
        p.line(5*cm, (y-2)*cm, 5*cm, (y+1)*cm)#sağ çizgi
        p.line(28.5*cm, (y-2)*cm, 28.5*cm, (y+1)*cm)#sağ çizgi
        ## üst taraf
        y=y-2
        p.line(1*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#üst çizgi
        p.drawString(1.1*cm, (y-1)*cm, "Ad-Soyad")
        p.drawString(1.1*cm, (y-1.3)*cm, "Tc Kimlik No")
        p.drawString(1.1*cm, (y-1.8)*cm, calisan1.calisan_adi + " " + calisan1.calisan_soyadi)
        p.drawString(1.1*cm, (y-2.3)*cm, calisan1.calisan_tc)
        p.line(1*cm, (y-1.5)*cm, 28.5*cm, (y-1.5)*cm)#üstün altı
        p.line(1*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)#alt çizgi
        p.line(1*cm, (y-2.5)*cm, 28.5*cm, (y-2.5)*cm)#sol çizgi
        p.line(1*cm, (y-2.5)*cm, 1*cm, (y-0.7)*cm)#sağ çizgi
        p.line(28.5*cm, (y-2.5)*cm, 28.5*cm, (y-0.7)*cm)#sağ çizgi
        p.line(2.8*cm, (y-2.5)*cm, 2.8*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(2.9*cm, (y-1)*cm, "Kanun No")
        p.drawString(2.9*cm, (y-1.3)*cm, "Prim Günü")
        p.drawString(2.9*cm, (y-1.8)*cm, calisan1.calisan_tesvik)
        p.drawString(2.9*cm, (y-2.3)*cm, str(maas1.gunsayisi1))
        p.line(4*cm, (y-2.5)*cm, 4*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(4.1*cm, (y-1)*cm, "Brüt Ücret")
        p.drawString(4.1*cm, (y-1.3)*cm, "Sair Öd.")
        p.drawString(4.1*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
        p.line(5.8*cm, (y-2.5)*cm, 5.8*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(5.9*cm, (y-1)*cm, "Sair Öd.2")
        p.drawString(5.9*cm, (y-1.3)*cm, "Sair Öd.3")
        p.line(7.3*cm, (y-2.5)*cm, 7.3*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(7.4*cm, (y-1)*cm, "Fazla Mesai")
        p.drawString(7.4*cm, (y-1.3)*cm, "Kesinti 1")
        p.line(9*cm, (y-2.5)*cm, 9*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(9.1*cm, (y-1)*cm, "Kesinti 2")
        p.drawString(9.1*cm, (y-1.3)*cm, "Kesinti 3")
        p.line(10.3*cm, (y-2.5)*cm, 10.3*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(10.4*cm, (y-1)*cm, "Toplam Brüt")
        p.drawString(10.4*cm, (y-1.3)*cm, "SGK İşçi Payı")
        p.drawString(10.4*cm, (y-1.8)*cm, str(bordro1.ocak_brut))
        p.drawString(10.4*cm, (y-2.3)*cm, str(bordro1.ocak_sgk_kesintisi))
        p.line(12.3*cm, (y-2.5)*cm, 12.3*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(12.4*cm, (y-1)*cm, "SGK İşçi İşz.")
        p.drawString(12.4*cm, (y-1.3)*cm, "Küm. Vergi M.")
        p.drawString(12.4*cm, (y-1.8)*cm, str(bordro1.ocak_issizlik_kesintisi))
        p.drawString(12.4*cm, (y-2.3)*cm, str(bordro1.ocak_kumulatif_vergi))
        p.line(13.9*cm, (y-2.5)*cm, 13.9*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(14*cm, (y-1)*cm, "Vergi Matrahı")
        p.drawString(14*cm, (y-1.3)*cm, "Gelir Vergisi")
        p.drawString(14*cm, (y-1.8)*cm, str(bordro1.ocak_vergi_matrahi))
        p.drawString(14*cm, (y-2.3)*cm, str(bordro1.ocak_istisna_oncesi_gelir))
        p.line(15.3*cm, (y-2.5)*cm, 15.3*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(15.4*cm, (y-1)*cm, "Asgari Ü. Gelir V. İst.")
        p.drawString(15.4*cm, (y-1.3)*cm, "Kalan Gelir Vergisi")
        p.drawString(15.4*cm, (y-1.8)*cm, str(bordro1.ocak_asgari_gelir_vergisi_istisnasi))
        p.drawString(15.4*cm, (y-2.3)*cm, str(bordro1.ocak_gelir_vergisi))
        p.line(17.9*cm, (y-2.5)*cm, 17.9*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(18*cm, (y-1)*cm, "Damga Vergisi")
        p.drawString(18*cm, (y-1.3)*cm, "Net Ücret")
        p.drawString(18*cm, (y-1.8)*cm, str(bordro1.ocak_damga_vergisi))
        p.drawString(18*cm, (y-2.3)*cm, str(bordro1.ocak_net_ucret))
        p.line(21*cm, (y-2.5)*cm, 21*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(21.1*cm, (y-1.3)*cm, "SGK İsveren Primi")
        p.drawString(21.1*cm, (y-1)*cm, "SGK İşveren İşsizlik Primi")
        p.drawString(21.1*cm, (y-1.8)*cm, str(bordro1.ocak_isveren_sgk_kesintisi))
        p.drawString(21.1*cm, (y-2.3)*cm, str(bordro1.ocak_isveren_issizlik_kesintisi))
        p.line(23.8*cm, (y-2.5)*cm, 23.8*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(23.9*cm, (y-1.3)*cm, "Gelir Vergisi İstisnası")
        p.drawString(23.9*cm, (y-1)*cm, "Damga Vergisi İstisnası")
        p.drawString(23.9*cm, (y-1.8)*cm, str(bordro1.ocak_gelir_vergisi_istisnasi))
        p.drawString(23.9*cm, (y-2.3)*cm, str(bordro1.ocak_damga_vergisi_istisnasi))
        p.line(26.4*cm, (y-2.5)*cm, 26.4*cm, (y-0.7)*cm)#sağ çizgi
        p.drawString(26.5*cm, (y-1.3)*cm, "Sgk Prim İstisnası")
        p.drawString(26.5*cm, (y-1)*cm, "Sgk İşsizlik Prim İst.")
        #orta kısım
        y=y-7
        p.line(1*cm, (y-0.7)*cm, 5.25*cm, (y-0.7)*cm)#üst çizgi
        p.line(5.85*cm, (y-0.7)*cm, 10.1*cm, (y-0.7)*cm)#alt çizgi
        p.line(10.7*cm, (y-0.7)*cm, 14.95*cm, (y-0.7)*cm)#alt çizgi
        p.line(15.55*cm, (y-0.7)*cm, 19.8*cm, (y-0.7)*cm)#alt çizgi
        p.line(20.4*cm, (y-0.7)*cm, 24.65*cm, (y-0.7)*cm)#alt çizgi
        p.line(25.25*cm, (y-0.7)*cm, 28.5*cm, (y-0.7)*cm)#alt çizgi
        p.line(1*cm, (y-0.7)*cm, 1*cm, (y-9)*cm)#üst çizgi
        p.line(5.25*cm, (y-0.7)*cm, 5.25*cm, (y-9)*cm)#üst çizgi
        p.line(5.85*cm, (y-0.7)*cm, 5.85*cm, (y-9)*cm)#üst çizgi
        p.line(10.1*cm, (y-0.7)*cm, 10.1*cm, (y-9)*cm)#üst çizgi
        p.line(10.7*cm, (y-0.7)*cm, 10.7*cm, (y-9)*cm)#üst çizgi
        p.line(14.95*cm, (y-0.7)*cm, 14.95*cm, (y-9)*cm)#üst çizgi
        p.line(15.55*cm, (y-0.7)*cm, 15.55*cm, (y-9)*cm)#üst çizgi
        p.line(19.8*cm, (y-0.7)*cm, 19.8*cm, (y-9)*cm)#üst çizgi
        p.line(20.4*cm, (y-0.7)*cm, 20.4*cm, (y-9)*cm)#üst çizgi
        p.line(24.65*cm, (y-0.7)*cm, 24.65*cm, (y-9)*cm)#üst çizgi
        p.line(25.25*cm, (y-0.7)*cm, 25.25*cm, (y-9)*cm)#üst çizgi
        p.line(28.5*cm, (y-0.7)*cm, 28.5*cm, (y-9)*cm)#üst çizgi
        p.line(1*cm, (y-9)*cm, 5.25*cm, (y-9)*cm)
        p.drawString(2.6*cm, (y-1.1)*cm, "Brüt Toplam")
        p.line(5.85*cm, (y-9)*cm, 10.1*cm, (y-9)*cm)
        p.drawString(7.8*cm, (y-1.1)*cm, "SGK")
        p.line(10.7*cm, (y-9)*cm, 14.95*cm, (y-9)*cm)
        p.drawString(12.3*cm, (y-1.1)*cm, "Gelir Vergisi")
        p.line(15.55*cm, (y-9)*cm, 19.8*cm, (y-9)*cm)
        p.drawString(17.1*cm, (y-1.1)*cm, "Damga Vergisi")
        p.line(20.4*cm, (y-9)*cm, 24.65*cm, (y-9)*cm)
        p.drawString(22.1*cm, (y-1.1)*cm, "Net Ücret")
        p.line(25.25*cm, (y-9)*cm, 28.5*cm, (y-9)*cm)
        p.drawString(26.6*cm, (y-1.1)*cm, "Günler")
        p.line(3*cm, (y-1.3)*cm, 3*cm, (y-9)*cm)#üst çizgi
        p.line(8*cm, (y-1.3)*cm, 8*cm, (y-9)*cm)#üst çizgi
        p.line(12.7*cm, (y-1.3)*cm, 12.7*cm, (y-9)*cm)#üst çizgi
        p.line(17.6*cm, (y-1.3)*cm, 17.6*cm, (y-9)*cm)#üst çizgi
        p.line(22.5*cm, (y-1.3)*cm, 22.5*cm, (y-9)*cm)#üst çizgi
        p.line(26.8*cm, (y-1.3)*cm, 26.8*cm, (y-9)*cm)#üst çizgi
        p.line(1*cm, (y-1.3)*cm, 5.25*cm, (y-1.3)*cm)
        p.drawString(1.2*cm, (y-1.7)*cm, "Brüt Ücret")
        p.line(5.85*cm, (y-1.3)*cm, 10.1*cm, (y-1.3)*cm)
        p.drawString(6.1*cm, (y-1.7)*cm, "SGK İşveren Payı")
        p.line(10.7*cm, (y-1.3)*cm, 14.95*cm, (y-1.3)*cm)
        p.drawString(10.8*cm, (y-1.7)*cm, "Hesaplanan Gelir V.")
        p.line(15.55*cm, (y-1.3)*cm, 19.8*cm, (y-1.3)*cm)
        p.drawString(15.6*cm, (y-1.7)*cm, "Hesaplanan Damga V.")
        p.line(20.4*cm, (y-1.3)*cm, 24.65*cm, (y-1.3)*cm)
        p.drawString(20.5*cm, (y-1.7)*cm, "Asıl Ücret")
        p.line(25.25*cm, (y-1.3)*cm, 28.5*cm, (y-1.3)*cm)
        p.drawString(25.5*cm, (y-1.7)*cm, "Çalışma Günü")
        p.line(1*cm, (y-2)*cm, 5.25*cm, (y-2)*cm)
        p.drawString(1.2*cm, (y-2.7)*cm, "Sair Ödeme1")
        p.line(5.85*cm, (y-2)*cm, 10.1*cm, (y-2)*cm)
        p.drawString(6.1*cm, (y-2.7)*cm, "Sgk İşçi Payı")
        p.line(10.7*cm, (y-2)*cm, 14.95*cm, (y-2)*cm)
        p.drawString(10.8*cm, (y-2.7)*cm, "ASgari Ü. Gelir V. İst.")
        p.line(15.55*cm, (y-2)*cm, 19.8*cm, (y-2)*cm)
        p.drawString(15.6*cm, (y-2.7)*cm, "İst. Damga Vergisi")
        p.line(20.4*cm, (y-2)*cm, 24.65*cm, (y-2)*cm)
        p.drawString(20.5*cm, (y-2.7)*cm, "Fazla Mesai")
        p.line(25.25*cm, (y-2)*cm, 28.5*cm, (y-2)*cm)
        p.drawString(25.5*cm, (y-2.7)*cm, "Haftasonu Günü")
        p.line(1*cm, (y-2.7)*cm, 5.25*cm, (y-2.7)*cm)
        p.drawString(1.2*cm, (y-3.4)*cm, "Sair Ödeme2")
        p.line(5.85*cm, (y-2.7)*cm, 10.1*cm, (y-2.7)*cm)
        p.drawString(6.1*cm, (y-3.4)*cm, "Sgk İşv. İşz. Payı")
        p.line(10.7*cm, (y-2.7)*cm, 14.95*cm, (y-2.7)*cm)
        p.drawString(10.8*cm, (y-3.4)*cm, "Terkin E. Gelir V.")
        p.line(15.55*cm, (y-2.7)*cm, 19.8*cm, (y-2.7)*cm)
        p.line(20.4*cm, (y-2.7)*cm, 24.65*cm, (y-2.7)*cm)
        p.drawString(20.5*cm, (y-3.4)*cm, "Sair Ödeme 1")
        p.line(25.25*cm, (y-2.7)*cm, 28.5*cm, (y-2.7)*cm)
        p.drawString(25.5*cm, (y-3.4)*cm, "Genel Tatil")
        p.line(1*cm, (y-3.4)*cm, 5.25*cm, (y-3.4)*cm)
        p.drawString(1.2*cm, (y-4.1)*cm, "Sair Ödeme3")
        p.line(5.85*cm, (y-3.4)*cm, 10.1*cm, (y-3.4)*cm)
        p.drawString(6.1*cm, (y-4.1)*cm, "Sgk İşçi İşz. Payı")
        p.line(10.7*cm, (y-3.4)*cm, 14.95*cm, (y-3.4)*cm)
        p.line(20.4*cm, (y-3.4)*cm, 24.65*cm, (y-3.4)*cm)
        p.drawString(20.5*cm, (y-4.1)*cm, "Sair Ödeme 2")
        p.line(25.25*cm, (y-3.4)*cm, 28.5*cm, (y-3.4)*cm)
        p.drawString(25.5*cm, (y-4.1)*cm, "Yıllık İzin")
        p.line(1*cm, (y-4.1)*cm, 5.25*cm, (y-4.1)*cm)
        p.drawString(1.2*cm, (y-4.8)*cm, "Fazla Mesai")
        p.line(5.85*cm, (y-4.1)*cm, 10.1*cm, (y-4.1)*cm)
        p.drawString(6.1*cm, (y-4.8)*cm, "Sgk Prim Desteği İst.")
        p.line(20.4*cm, (y-4.1)*cm, 24.65*cm, (y-4.1)*cm)
        p.drawString(20.5*cm, (y-4.8)*cm, "Sair Ödeme 3")
        p.line(25.25*cm, (y-4.1)*cm, 28.5*cm, (y-4.1)*cm)
        p.drawString(25.5*cm, (y-4.8)*cm, "Sıhhi İzin")
        p.line(1*cm, (y-4.8)*cm, 5.25*cm, (y-4.8)*cm)
        p.drawString(1.2*cm, (y-5.5)*cm, "Kesinti 1")
        p.line(5.85*cm, (y-4.8)*cm, 10.1*cm, (y-4.8)*cm)
        p.drawString(6.1*cm, (y-5.5)*cm, "Sgk İşs. Prim Des. İst.")
        p.line(20.4*cm, (y-4.8)*cm, 24.65*cm, (y-4.8)*cm)
        p.drawString(20.5*cm, (y-5.5)*cm, "Kesinti 1")
        p.line(25.25*cm, (y-4.8)*cm, 28.5*cm, (y-4.8)*cm)
        p.drawString(25.5*cm, (y-5.5)*cm, "Ucretsiz İzin")
        p.line(1*cm, (y-5.5)*cm, 5.25*cm, (y-5.5)*cm)
        p.drawString(1.2*cm, (y-6.2)*cm, "Kesinti 2")
        p.line(5.85*cm, (y-5.5)*cm, 10.1*cm, (y-5.5)*cm)
        p.line(20.4*cm, (y-5.5)*cm, 24.65*cm, (y-5.5)*cm)
        p.drawString(20.5*cm, (y-6.2)*cm, "Kesinti 2")
        p.line(25.25*cm, (y-5.5)*cm, 28.5*cm, (y-5.5)*cm)
        p.drawString(25.5*cm, (y-6.2)*cm, "Ücretli İzin")
        p.line(1*cm, (y-6.2)*cm, 5.25*cm, (y-6.2)*cm)
        p.drawString(1.2*cm, (y-6.9)*cm, "Kesinti 3")
        p.line(20.4*cm, (y-6.2)*cm, 24.65*cm, (y-6.2)*cm)
        p.drawString(20.5*cm, (y-6.9)*cm, "Kesinti 3")
        p.line(25.25*cm, (y-6.2)*cm, 28.5*cm, (y-6.2)*cm)
        p.drawString(25.5*cm, (y-6.9)*cm, "Mazeret İzin")
        p.line(1*cm, (y-6.9)*cm, 5.25*cm, (y-6.9)*cm)
        p.line(20.4*cm, (y-6.9)*cm, 24.65*cm, (y-6.9)*cm)
        p.line(25.25*cm, (y-6.9)*cm, 28.5*cm, (y-6.9)*cm)
        p.drawString(25.5*cm, (y-7.6)*cm, "Prim Günü")

        p.line(1*cm, (y-7.6)*cm, 5.25*cm, (y-7.6)*cm)

        p.line(5.85*cm, (y-7.6)*cm, 10.1*cm, (y-7.6)*cm)

        p.line(10.7*cm, (y-7.6)*cm, 14.95*cm, (y-7.6)*cm)

        p.line(15.55*cm, (y-7.6)*cm, 19.8*cm, (y-7.6)*cm)

        p.line(20.4*cm, (y-7.6)*cm, 24.65*cm, (y-7.6)*cm)

        p.line(25.25*cm, (y-7.6)*cm, 28.5*cm, (y-7.6)*cm)
        p.line(1*cm, (y-8.3)*cm, 5.25*cm, (y-8.3)*cm)
        p.drawString(1.2*cm, (y-9)*cm, "Brüt Toplam")
        p.line(5.85*cm, (y-8.3)*cm, 10.1*cm, (y-8.3)*cm)
        p.drawString(10.7*cm, (y-9)*cm, "Ödenecek SGK Primi")

        p.line(10.7*cm, (y-8.3)*cm, 14.95*cm, (y-8.3)*cm)
        p.drawString(15.55*cm, (y-9)*cm, "Ödenecek Gelir V.")
        p.line(15.55*cm, (y-8.3)*cm, 19.8*cm, (y-8.3)*cm)
        p.drawString(20.5*cm, (y-9)*cm, "Ödenecek Damga V.")
        p.line(20.4*cm, (y-8.3)*cm, 24.65*cm, (y-8.3)*cm)
        p.drawString(25.5*cm, (y-9)*cm, "Net Ödenecek Ücret")
        p.line(25.25*cm, (y-8.3)*cm, 28.5*cm, (y-8.3)*cm)

        tur=form.cleaned_data.get('export')

        if tur == "pdf":
            p.showPage()
            p.save()
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=False, filename='bordro.pdf')
        elif tur == "xls":
            output = io.BytesIO()
            wb.save(output)
            output.seek(0)
            return FileResponse(output, as_attachment=False, filename='bordro.xls')
        else:
            return HttpResponseNotFound("404")




    context={

        'form':form,

    }
    return render(request,'createpdf.html',context)

def handler404(request, exception):
    return render(request, 'custom404.html', status=404)
@login_required(login_url='user:login')
def maasdetail(request,id,year):
    if request.user.groups.filter(name='admin').exists():
        pass
    elif request.user.groups.filter(name='mali_musavir').exists():
        if not mali_sirket.objects.get(id=mali_musavir.objects.get(mali_musavir_id=request.user).mali_sirket_id_id).mali_sirket_bagli_sirketler.filter(id=calisan.objects.get(id=id).calisan_sirket_id_id).exists():
            return HttpResponseNotFound('<h1>Page not found</h1>')
    elif request.user.groups.filter(name='calisan').exists():
        if request.user.id != calisan.objects.get(id=id).calisan_id_id:
            return HttpResponseNotFound("Yetkisiz Erişim")

    employee=calisan.objects.filter(id=id)
    tesvik=employee[0].calisan_tesvik
    engelli=employee[0].calisan_engelli
    indirim=employee[0].calisan_indirim





    return hesapla(request,id,year,tesvik,engelli,indirim)
from datetime import date
def searchemp(request,id):
    print(id)
    calisantab=False
    queryset_list= calisan.objects.filter(calisan_sube_id=id).order_by('calisan_soyadi')
    comp=sirket.objects.get(id=sube.objects.get(id=id).sube_sirket_id.id)

    if 'q' in request.GET:
        q=request.GET.get('q')
        if q:
            queryset_list=queryset_list.filter(
                Q(calisan_adi__icontains=q)|
                Q(calisan_soyadi__icontains=q)|
                Q(calisan_tc__icontains=q)
            ).distinct()
            calisantab=True




    context={
            'employees':queryset_list,
            'calisantab':calisantab,
            'sirketid':comp.id,
            'sube':id
        }
    return render(request,'listemployee.html',context)
def searchcomp(request):

    if request.user.groups.filter(name='admin').exists():
        queryset_list= sirket.objects.all()
    elif request.user.groups.filter(name='mali_musavir').exists():
        queryset_list= sirket.objects.filter(sirket_mali_musavir_id=request.user)


    if 'q' in request.GET:
        q=request.GET.get('q')
        if q:
            queryset_list=queryset_list.filter(
                Q(sirket_adi__icontains=q)
            ).distinct()
    sirkettab=True
    context={
        'companys':queryset_list,
        'sirkettab':sirkettab,

    }
    return render(request,'listcompany.html',context)


def list_malisirket_detail(request):

    mali=mali_sirket.objects.get(id=mali_musavir.objects.get(mali_musavir_id=request.user.id).mali_sirket_id.id)
    calisan=mali_musavir.objects.filter(mali_sirket_id=mali)
    print(calisan)
    context={
        'calisan':calisan,
    }
    return render(request,'listmalimusavir.html',context)

def addmalimusavir(request):

    form=RegisterForm(request.POST or None)
    form1=MaliMusavirRegisterForm(request.POST or None, request.FILES or None)
    if form.is_valid() and form1.is_valid():
        username=form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.is_active=True
        newUser.save()
        lastid=User.objects.get(username=newUser.username)
        malimusavir=form1.save(commit=False)
        malimusavir.mali_musavir_id=lastid
        malimusavir.mali_sirket_id=mali_sirket.objects.get(id=mali_musavir.objects.get(mali_musavir_id=request.user.id).mali_sirket_id.id)

        if  not malimusavir.mali_musavir_photo :
            if malimusavir.mali_musavir_gender=="pick1":
                malimusavir.mali_musavir_photo="/calisan_photo/default.png"
            elif malimusavir.mali_musavir_gender=="pick2":
                malimusavir.mali_musavir_photo="/calisan_photo/defaultw.png"
            else:
                malimusavir.mali_musavir_photo="/calisan_photo/default.png"
        malimusavir.save()
        return redirect(reverse('user:malisirketdetail'))
    context={
        'form':form,
        'form1':form1,
    }
    return render(request,'addmalimusavir.html',context)

@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def addmaas(request,id):
    calisan1=calisan.objects.get(id=id)
    user1=User.objects.get(id=calisan1.calisan_id_id)
    current_year = date.today().year

    form=MaasRegisterForm(request.POST or None)
    record=maas.objects.filter(calisan_id=calisan1.id ,yil=current_year)


    if form.is_valid():
        if record:
            messages.info(request,"Bu yıl için zaten maaş kaydı yapılmıştır")
            return redirect(reverse('user:employeedetail', kwargs={'id':id}))

        else:
            form=form.save(commit=False)
            form.calisan_id=calisan1
            form.yil=current_year
            form.save()
            maas1=maas.objects.get(calisan_id=calisan1.id ,yil=current_year)
            bordro.objects.create(maas_id=maas1,calisan_id=calisan1)

            return redirect(reverse('user:employeedetail', kwargs={'id':id}))
    context={
        'form':form
    }
    return render(request,'addmaas.html',context)

from django import forms
@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def update_maas(request,id,maasid):

    maas1=get_object_or_404(maas,id=maasid)
    form=MaasRegisterForm(request.POST or None,instance=maas1)


    if form.is_valid():
        maas1=form.save(commit=False)
        maas1.save()
        maas1=maas.objects.get(id=maasid)
        bordro1=bordro.objects.get(maas_id=maas1)
        calisan1=calisan.objects.get(id=id)
        # bordro1=getlist1(request,id,maas1.yil,calisan1.calisan_tesvik,calisan1.calisan_engelli,calisan1.calisan_indirim)

        for i in range(12):
            if i==0:
                                data=hesaplama1("ocak",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.ocak_brut=data[0]
                                bordro1.ocak_calisilan_gun=data[1]
                                bordro1.ocak_arge_gun=data[2]
                                bordro1.ocak_bordroyaesasbrut=data[3]
                                bordro1.ocak_sgk_matrahi=data[4]
                                bordro1.ocak_sgk_kesintisi=data[5]
                                bordro1.ocak_issizlik_kesintisi=data[6]
                                bordro1.ocak_vergi_matrahi=data[7]
                                bordro1.ocak_kumulatif_vergi=data[8]
                                bordro1.ocak_istisna_oncesi_gelir=data[9]
                                # bordro1.ocak_asgari_vergi=data[10]
                                bordro1.ocak_kumulatif_asgari_ucret=data[10]
                                bordro1.ocak_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.ocak_damga_vergisi=data[12]
                                bordro1.ocak_gelir_vergisi=data[13]
                                bordro1.ocak_net_ucret=data[14]
                                bordro1.ocak_isveren_sgk_kesintisi=data[15]
                                bordro1.ocak_isveren_issizlik_kesintisi=data[16]
                                bordro1.ocak_toplam_sgk_kesintisi=data[17]
                                bordro1.ocak_sgk_istisnasi=data[18]
                                bordro1.ocak_odenecek_sgk=data[19]
                                bordro1.ocak_odenecek_gelir_vergisi=data[21]
                                bordro1.ocak_odenecek_damga_vergisi=data[22]
                                bordro1.ocak_istisna_oncesi_damga=data[23]
                                bordro1.ocak_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.ocak_toplam_maliyet=data[25]
                                bordro1.ocak_vergi_dilimi=data[26]
                                bordro1.ocak_gelir_vergisi_istisnasi=data[27]
                                bordro1.ocak_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==1:
                                data=hesaplama1("subat",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.subat_brut=data[0]
                                bordro1.subat_calisilan_gun=data[1]
                                bordro1.subat_arge_gun=data[2]
                                bordro1.subat_bordroyaesasbrut=data[3]
                                bordro1.subat_sgk_matrahi=data[4]
                                bordro1.subat_sgk_kesintisi=data[5]
                                bordro1.subat_issizlik_kesintisi=data[6]
                                bordro1.subat_vergi_matrahi=data[7]
                                bordro1.subat_kumulatif_vergi=data[8]
                                bordro1.subat_istisna_oncesi_gelir=data[9]
                                # bordrosubatak_asgari_vergi=data[10]
                                bordro1.subat_kumulatif_asgari_ucret=data[10]
                                bordro1.subat_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.subat_damga_vergisi=data[12]
                                bordro1.subat_gelir_vergisi=data[13]
                                bordro1.subat_net_ucret=data[14]
                                bordro1.subat_isveren_sgk_kesintisi=data[15]
                                bordro1.subat_isveren_issizlik_kesintisi=data[16]
                                bordro1.subat_toplam_sgk_kesintisi=data[17]
                                bordro1.subat_sgk_istisnasi=data[18]
                                bordro1.subat_odenecek_sgk=data[19]
                                bordro1.subat_odenecek_gelir_vergisi=data[21]
                                bordro1.subat_odenecek_damga_vergisi=data[22]
                                bordro1.subat_istisna_oncesi_damga=data[23]
                                bordro1.subat_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.subat_toplam_maliyet=data[25]
                                bordro1.subat_vergi_dilimi=data[26]
                                bordro1.subat_gelir_vergisi_istisnasi=data[27]
                                bordro1.subat_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==2:
                                data=hesaplama1("mart",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.mart_brut=data[0]
                                bordro1.mart_calisilan_gun=data[1]
                                bordro1.mart_arge_gun=data[2]
                                bordro1.mart_bordroyaesasbrut=data[3]
                                bordro1.mart_sgk_matrahi=data[4]
                                bordro1.mart_sgk_kesintisi=data[5]
                                bordro1.mart_issizlik_kesintisi=data[6]
                                bordro1.mart_vergi_matrahi=data[7]
                                bordro1.mart_kumulatif_vergi=data[8]
                                bordro1.mart_istisna_oncesi_gelir=data[9]
                                # bordromartak_asgari_vergi=data[10]
                                bordro1.mart_kumulatif_asgari_ucret=data[10]
                                bordro1.mart_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.mart_damga_vergisi=data[12]
                                bordro1.mart_gelir_vergisi=data[13]
                                bordro1.mart_net_ucret=data[14]
                                bordro1.mart_isveren_sgk_kesintisi=data[15]
                                bordro1.mart_isveren_issizlik_kesintisi=data[16]
                                bordro1.mart_toplam_sgk_kesintisi=data[17]
                                bordro1.mart_sgk_istisnasi=data[18]
                                bordro1.mart_odenecek_sgk=data[19]
                                bordro1.mart_odenecek_gelir_vergisi=data[21]
                                bordro1.mart_odenecek_damga_vergisi=data[22]
                                bordro1.mart_istisna_oncesi_damga=data[23]
                                bordro1.mart_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.mart_toplam_maliyet=data[25]
                                bordro1.mart_vergi_dilimi=data[26]
                                bordro1.mart_gelir_vergisi_istisnasi=data[27]
                                bordro1.mart_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==3:
                                data=hesaplama1("nisan",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.nisan_brut=data[0]
                                bordro1.nisan_calisilan_gun=data[1]
                                bordro1.nisan_arge_gun=data[2]
                                bordro1.nisan_bordroyaesasbrut=data[3]
                                bordro1.nisan_sgk_matrahi=data[4]
                                bordro1.nisan_sgk_kesintisi=data[5]
                                bordro1.nisan_issizlik_kesintisi=data[6]
                                bordro1.nisan_vergi_matrahi=data[7]
                                bordro1.nisan_kumulatif_vergi=data[8]
                                bordro1.nisan_istisna_oncesi_gelir=data[9]
                                # bordronisanak_asgari_vergi=data[10]
                                bordro1.nisan_kumulatif_asgari_ucret=data[10]
                                bordro1.nisan_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.nisan_damga_vergisi=data[12]
                                bordro1.nisan_gelir_vergisi=data[13]
                                bordro1.nisan_net_ucret=data[14]
                                bordro1.nisan_isveren_sgk_kesintisi=data[15]
                                bordro1.nisan_isveren_issizlik_kesintisi=data[16]
                                bordro1.nisan_toplam_sgk_kesintisi=data[17]
                                bordro1.nisan_sgk_istisnasi=data[18]
                                bordro1.nisan_odenecek_sgk=data[19]
                                bordro1.nisan_odenecek_gelir_vergisi=data[21]
                                bordro1.nisan_odenecek_damga_vergisi=data[22]
                                bordro1.nisan_istisna_oncesi_damga=data[23]
                                bordro1.nisan_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.nisan_toplam_maliyet=data[25]
                                bordro1.nisan_vergi_dilimi=data[26]
                                bordro1.nisan_gelir_vergisi_istisnasi=data[27]
                                bordro1.nisan_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==4:
                                data=hesaplama1("mayis",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.mayis_brut=data[0]
                                bordro1.mayis_calisilan_gun=data[1]
                                bordro1.mayis_arge_gun=data[2]
                                bordro1.mayis_bordroyaesasbrut=data[3]
                                bordro1.mayis_sgk_matrahi=data[4]
                                bordro1.mayis_sgk_kesintisi=data[5]
                                bordro1.mayis_issizlik_kesintisi=data[6]
                                bordro1.mayis_vergi_matrahi=data[7]
                                bordro1.mayis_kumulatif_vergi=data[8]
                                bordro1.mayis_istisna_oncesi_gelir=data[9]
                                # bordromayisak_asgari_vergi=data[10]
                                bordro1.mayis_kumulatif_asgari_ucret=data[10]
                                bordro1.mayis_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.mayis_damga_vergisi=data[12]
                                bordro1.mayis_gelir_vergisi=data[13]
                                bordro1.mayis_net_ucret=data[14]
                                bordro1.mayis_isveren_sgk_kesintisi=data[15]
                                bordro1.mayis_isveren_issizlik_kesintisi=data[16]
                                bordro1.mayis_toplam_sgk_kesintisi=data[17]
                                bordro1.mayis_sgk_istisnasi=data[18]
                                bordro1.mayis_odenecek_sgk=data[19]
                                bordro1.mayis_odenecek_gelir_vergisi=data[21]
                                bordro1.mayis_odenecek_damga_vergisi=data[22]
                                bordro1.mayis_istisna_oncesi_damga=data[23]
                                bordro1.mayis_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.mayis_toplam_maliyet=data[25]
                                bordro1.mayis_vergi_dilimi=data[26]
                                bordro1.mayis_gelir_vergisi_istisnasi=data[27]
                                bordro1.mayis_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==5:
                                data=hesaplama1("haziran",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.haziran_brut=data[0]
                                bordro1.haziran_calisilan_gun=data[1]
                                bordro1.haziran_arge_gun=data[2]
                                bordro1.haziran_bordroyaesasbrut=data[3]
                                bordro1.haziran_sgk_matrahi=data[4]
                                bordro1.haziran_sgk_kesintisi=data[5]
                                bordro1.haziran_issizlik_kesintisi=data[6]
                                bordro1.haziran_vergi_matrahi=data[7]
                                bordro1.haziran_kumulatif_vergi=data[8]
                                bordro1.haziran_istisna_oncesi_gelir=data[9]
                                # bordrohaziranak_asgari_vergi=data[10]
                                bordro1.haziran_kumulatif_asgari_ucret=data[10]
                                bordro1.haziran_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.haziran_damga_vergisi=data[12]
                                bordro1.haziran_gelir_vergisi=data[13]
                                bordro1.haziran_net_ucret=data[14]
                                bordro1.haziran_isveren_sgk_kesintisi=data[15]
                                bordro1.haziran_isveren_issizlik_kesintisi=data[16]
                                bordro1.haziran_toplam_sgk_kesintisi=data[17]
                                bordro1.haziran_sgk_istisnasi=data[18]
                                bordro1.haziran_odenecek_sgk=data[19]
                                bordro1.haziran_odenecek_gelir_vergisi=data[21]
                                bordro1.haziran_odenecek_damga_vergisi=data[22]
                                bordro1.haziran_istisna_oncesi_damga=data[23]
                                bordro1.haziran_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.haziran_toplam_maliyet=data[25]
                                bordro1.haziran_vergi_dilimi=data[26]
                                bordro1.haziran_gelir_vergisi_istisnasi=data[27]
                                bordro1.haziran_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==6:
                                data=hesaplama1("temmuz",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.temmuz_brut=data[0]
                                bordro1.temmuz_calisilan_gun=data[1]
                                bordro1.temmuz_arge_gun=data[2]
                                bordro1.temmuz_bordroyaesasbrut=data[3]
                                bordro1.temmuz_sgk_matrahi=data[4]
                                bordro1.temmuz_sgk_kesintisi=data[5]
                                bordro1.temmuz_issizlik_kesintisi=data[6]
                                bordro1.temmuz_vergi_matrahi=data[7]
                                bordro1.temmuz_kumulatif_vergi=data[8]
                                bordro1.temmuz_istisna_oncesi_gelir=data[9]
                                # bordrotemmuzak_asgari_vergi=data[10]
                                bordro1.temmuz_kumulatif_asgari_ucret=data[10]
                                bordro1.temmuz_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.temmuz_damga_vergisi=data[12]
                                bordro1.temmuz_gelir_vergisi=data[13]
                                bordro1.temmuz_net_ucret=data[14]
                                bordro1.temmuz_isveren_sgk_kesintisi=data[15]
                                bordro1.temmuz_isveren_issizlik_kesintisi=data[16]
                                bordro1.temmuz_toplam_sgk_kesintisi=data[17]
                                bordro1.temmuz_sgk_istisnasi=data[18]
                                bordro1.temmuz_odenecek_sgk=data[19]
                                bordro1.temmuz_odenecek_gelir_vergisi=data[21]
                                bordro1.temmuz_odenecek_damga_vergisi=data[22]
                                bordro1.temmuz_istisna_oncesi_damga=data[23]
                                bordro1.temmuz_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.temmuz_toplam_maliyet=data[25]
                                bordro1.temmuz_vergi_dilimi=data[26]
                                bordro1.temmuz_gelir_vergisi_istisnasi=data[27]
                                bordro1.temmuz_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==7:
                                data=hesaplama1("agustos",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.agustos_brut=data[0]
                                bordro1.agustos_calisilan_gun=data[1]
                                bordro1.agustos_arge_gun=data[2]
                                bordro1.agustos_bordroyaesasbrut=data[3]
                                bordro1.agustos_sgk_matrahi=data[4]
                                bordro1.agustos_sgk_kesintisi=data[5]
                                bordro1.agustos_issizlik_kesintisi=data[6]
                                bordro1.agustos_vergi_matrahi=data[7]
                                bordro1.agustos_kumulatif_vergi=data[8]
                                bordro1.agustos_istisna_oncesi_gelir=data[9]
                                # bordroagustosak_asgari_vergi=data[10]
                                bordro1.agustos_kumulatif_asgari_ucret=data[10]
                                bordro1.agustos_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.agustos_damga_vergisi=data[12]
                                bordro1.agustos_gelir_vergisi=data[13]
                                bordro1.agustos_net_ucret=data[14]
                                bordro1.agustos_isveren_sgk_kesintisi=data[15]
                                bordro1.agustos_isveren_issizlik_kesintisi=data[16]
                                bordro1.agustos_toplam_sgk_kesintisi=data[17]
                                bordro1.agustos_sgk_istisnasi=data[18]
                                bordro1.agustos_odenecek_sgk=data[19]
                                bordro1.agustos_odenecek_gelir_vergisi=data[21]
                                bordro1.agustos_odenecek_damga_vergisi=data[22]
                                bordro1.agustos_istisna_oncesi_damga=data[23]
                                bordro1.agustos_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.agustos_toplam_maliyet=data[25]
                                bordro1.agustos_vergi_dilimi=data[26]
                                bordro1.agustos_gelir_vergisi_istisnasi=data[27]
                                bordro1.agustos_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==8:          
                                data=hesaplama1("eylul",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.eylul_brut=data[0]
                                bordro1.eylul_calisilan_gun=data[1]
                                bordro1.eylul_arge_gun=data[2]
                                bordro1.eylul_bordroyaesasbrut=data[3]
                                bordro1.eylul_sgk_matrahi=data[4]
                                bordro1.eylul_sgk_kesintisi=data[5]
                                bordro1.eylul_issizlik_kesintisi=data[6]
                                bordro1.eylul_vergi_matrahi=data[7]
                                bordro1.eylul_kumulatif_vergi=data[8]
                                bordro1.eylul_istisna_oncesi_gelir=data[9]
                                # bordroeylulak_asgari_vergi=data[10]
                                bordro1.eylul_kumulatif_asgari_ucret=data[10]
                                bordro1.eylul_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.eylul_damga_vergisi=data[12]
                                bordro1.eylul_gelir_vergisi=data[13]
                                bordro1.eylul_net_ucret=data[14]
                                bordro1.eylul_isveren_sgk_kesintisi=data[15]
                                bordro1.eylul_isveren_issizlik_kesintisi=data[16]
                                bordro1.eylul_toplam_sgk_kesintisi=data[17]
                                bordro1.eylul_sgk_istisnasi=data[18]
                                bordro1.eylul_odenecek_sgk=data[19]
                                bordro1.eylul_odenecek_gelir_vergisi=data[21]
                                bordro1.eylul_odenecek_damga_vergisi=data[22]
                                bordro1.eylul_istisna_oncesi_damga=data[23]
                                bordro1.eylul_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.eylul_toplam_maliyet=data[25]
                                bordro1.eylul_vergi_dilimi=data[26]
                                bordro1.eylul_gelir_vergisi_istisnasi=data[27]
                                bordro1.eylul_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==9:
                                data=hesaplama1("ekim",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.ekim_brut=data[0]
                                bordro1.ekim_calisilan_gun=data[1]
                                bordro1.ekim_arge_gun=data[2]
                                bordro1.ekim_bordroyaesasbrut=data[3]
                                bordro1.ekim_sgk_matrahi=data[4]
                                bordro1.ekim_sgk_kesintisi=data[5]
                                bordro1.ekim_issizlik_kesintisi=data[6]
                                bordro1.ekim_vergi_matrahi=data[7]
                                bordro1.ekim_kumulatif_vergi=data[8]
                                bordro1.ekim_istisna_oncesi_gelir=data[9]
                                # bordroekimak_asgari_vergi=data[10]
                                bordro1.ekim_kumulatif_asgari_ucret=data[10]
                                bordro1.ekim_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.ekim_damga_vergisi=data[12]
                                bordro1.ekim_gelir_vergisi=data[13]
                                bordro1.ekim_net_ucret=data[14]
                                bordro1.ekim_isveren_sgk_kesintisi=data[15]
                                bordro1.ekim_isveren_issizlik_kesintisi=data[16]
                                bordro1.ekim_toplam_sgk_kesintisi=data[17]
                                bordro1.ekim_sgk_istisnasi=data[18]
                                bordro1.ekim_odenecek_sgk=data[19]
                                bordro1.ekim_odenecek_gelir_vergisi=data[21]
                                bordro1.ekim_odenecek_damga_vergisi=data[22]
                                bordro1.ekim_istisna_oncesi_damga=data[23]
                                bordro1.ekim_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.ekim_toplam_maliyet=data[25]
                                bordro1.ekim_vergi_dilimi=data[26]
                                bordro1.ekim_gelir_vergisi_istisnasi=data[27]
                                bordro1.ekim_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==10:
                                data=hesaplama1("kasim",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.kasim_brut=data[0]
                                bordro1.kasim_calisilan_gun=data[1]
                                bordro1.kasim_arge_gun=data[2]
                                bordro1.kasim_bordroyaesasbrut=data[3]
                                bordro1.kasim_sgk_matrahi=data[4]
                                bordro1.kasim_sgk_kesintisi=data[5]
                                bordro1.kasim_issizlik_kesintisi=data[6]
                                bordro1.kasim_vergi_matrahi=data[7]
                                bordro1.kasim_kumulatif_vergi=data[8]
                                bordro1.kasim_istisna_oncesi_gelir=data[9]
                                # bordrokasimak_asgari_vergi=data[10]
                                bordro1.kasim_kumulatif_asgari_ucret=data[10]
                                bordro1.kasim_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.kasim_damga_vergisi=data[12]
                                bordro1.kasim_gelir_vergisi=data[13]
                                bordro1.kasim_net_ucret=data[14]
                                bordro1.kasim_isveren_sgk_kesintisi=data[15]
                                bordro1.kasim_isveren_issizlik_kesintisi=data[16]
                                bordro1.kasim_toplam_sgk_kesintisi=data[17]
                                bordro1.kasim_sgk_istisnasi=data[18]
                                bordro1.kasim_odenecek_sgk=data[19]
                                bordro1.kasim_odenecek_gelir_vergisi=data[21]
                                bordro1.kasim_odenecek_damga_vergisi=data[22]
                                bordro1.kasim_istisna_oncesi_damga=data[23]
                                bordro1.kasim_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.kasim_toplam_maliyet=data[25]
                                bordro1.kasim_vergi_dilimi=data[26]
                                bordro1.kasim_gelir_vergisi_istisnasi=data[27]
                                bordro1.kasim_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()
            elif i==11:
                                data=hesaplama1("aralik",maas.objects.get(calisan_id=calisan1,yil=date.today().year).id,calisan1.id)
                                bordro1.aralik_brut=data[0]
                                bordro1.aralik_calisilan_gun=data[1]
                                bordro1.aralik_arge_gun=data[2]
                                bordro1.aralik_bordroyaesasbrut=data[3]
                                bordro1.aralik_sgk_matrahi=data[4]
                                bordro1.aralik_sgk_kesintisi=data[5]
                                bordro1.aralik_issizlik_kesintisi=data[6]
                                bordro1.aralik_vergi_matrahi=data[7]
                                bordro1.aralik_kumulatif_vergi=data[8]
                                bordro1.aralik_istisna_oncesi_gelir=data[9]
                                # bordroaralikak_asgari_vergi=data[10]
                                bordro1.aralik_kumulatif_asgari_ucret=data[10]
                                bordro1.aralik_asgari_gelir_vergisi_istisnasi=data[11]
                                bordro1.aralik_damga_vergisi=data[12]
                                bordro1.aralik_gelir_vergisi=data[13]
                                bordro1.aralik_net_ucret=data[14]
                                bordro1.aralik_isveren_sgk_kesintisi=data[15]
                                bordro1.aralik_isveren_issizlik_kesintisi=data[16]
                                bordro1.aralik_toplam_sgk_kesintisi=data[17]
                                bordro1.aralik_sgk_istisnasi=data[18]
                                bordro1.aralik_odenecek_sgk=data[19]
                                bordro1.aralik_odenecek_gelir_vergisi=data[21]
                                bordro1.aralik_odenecek_damga_vergisi=data[22]
                                bordro1.aralik_istisna_oncesi_damga=data[23]
                                bordro1.aralik_asgari_damga_vergisi_istisnasi=data[24]
                                bordro1.aralik_toplam_maliyet=data[25]
                                bordro1.aralik_vergi_dilimi=data[26]
                                bordro1.aralik_gelir_vergisi_istisnasi=data[27]
                                bordro1.aralik_damga_vergisi_istisnasi=data[28]
                                bordro1.bordro_kumularifasgariucret=data[11]
                                bordro1.bordro_kumularivergi=data[8]
                                bordro1.save()

        # for i in range(12):
        #     if i==0:
        #             bordroekle.ocak_brut=bordro1[i][19]
        #             bordroekle.ocak_calisilan_gun=bordro1[i][2]
        #             bordroekle.ocak_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.ocak_sgk_matrahi=bordro1[i][3]
        #             bordroekle.ocak_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.ocak_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.ocak_vergi_dilimi=bordro1[i][25]
        #             bordroekle.ocak_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.ocak_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.ocak_vergi_matrahi=bordro1[i][6]
        #             bordroekle.ocak_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.ocak_asgari_vergi=bordro1[i][9]
        #             bordroekle.ocak_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.ocak_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.ocak_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.ocak_damga_vergisi=bordro1[i][12]
        #             bordroekle.ocak_gelir_vergisi=bordro1[i][13]
        #             bordroekle.ocak_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.ocak_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.ocak_net_ucret=bordro1[i][14]
        #             bordroekle.ocak_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.ocak_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.ocak_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.ocak_toplam_maliyet=bordro1[i][18]
        #             bordroekle.ocak_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.ocak_odenecek_sgk=bordro1[i][21]
        #             bordroekle.ocak_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.ocak_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==1:
        #             bordroekle.subat_brut=bordro1[i][19]
        #             bordroekle.subat_calisilan_gun=bordro1[i][2]
        #             bordroekle.subat_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.subat_sgk_matrahi=bordro1[i][3]
        #             bordroekle.subat_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.subat_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.subat_vergi_dilimi=bordro1[i][25]
        #             bordroekle.subat_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.subat_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.subat_vergi_matrahi=bordro1[i][6]
        #             bordroekle.subat_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.subat_asgari_vergi=bordro1[i][9]
        #             bordroekle.subat_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.subat_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.subat_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.subat_damga_vergisi=bordro1[i][12]
        #             bordroekle.subat_gelir_vergisi=bordro1[i][13]
        #             bordroekle.subat_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.subat_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.subat_net_ucret=bordro1[i][14]
        #             bordroekle.subat_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.subat_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.subat_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.subat_toplam_maliyet=bordro1[i][18]
        #             bordroekle.subat_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.subat_odenecek_sgk=bordro1[i][21]
        #             bordroekle.subat_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.subat_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==2:
        #             bordroekle.mart_brut=bordro1[i][19]
        #             bordroekle.mart_calisilan_gun=bordro1[i][2]
        #             bordroekle.mart_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.mart_sgk_matrahi=bordro1[i][3]
        #             bordroekle.mart_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.mart_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.mart_vergi_dilimi=bordro1[i][25]
        #             bordroekle.mart_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.mart_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.mart_vergi_matrahi=bordro1[i][6]
        #             bordroekle.mart_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.mart_asgari_vergi=bordro1[i][9]
        #             bordroekle.mart_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.mart_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.mart_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.mart_damga_vergisi=bordro1[i][12]
        #             bordroekle.mart_gelir_vergisi=bordro1[i][13]
        #             bordroekle.mart_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.mart_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.mart_net_ucret=bordro1[i][14]
        #             bordroekle.mart_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.mart_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.mart_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.mart_toplam_maliyet=bordro1[i][18]
        #             bordroekle.mart_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.mart_odenecek_sgk=bordro1[i][21]
        #             bordroekle.mart_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.mart_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==3:
        #             bordroekle.nisan_brut=bordro1[i][19]
        #             bordroekle.nisan_calisilan_gun=bordro1[i][2]
        #             bordroekle.nisan_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.nisan_sgk_matrahi=bordro1[i][3]
        #             bordroekle.nisan_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.nisan_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.nisan_vergi_dilimi=bordro1[i][25]
        #             bordroekle.nisan_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.nisan_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.nisan_vergi_matrahi=bordro1[i][6]
        #             bordroekle.nisan_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.nisan_asgari_vergi=bordro1[i][9]
        #             bordroekle.nisan_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.nisan_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.nisan_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.nisan_damga_vergisi=bordro1[i][12]
        #             bordroekle.nisan_gelir_vergisi=bordro1[i][13]
        #             bordroekle.nisan_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.nisan_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.nisan_net_ucret=bordro1[i][14]
        #             bordroekle.nisan_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.nisan_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.nisan_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.nisan_toplam_maliyet=bordro1[i][18]
        #             bordroekle.nisan_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.nisan_odenecek_sgk=bordro1[i][21]
        #             bordroekle.nisan_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.nisan_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==4:
        #             bordroekle.mayis_brut=bordro1[i][19]
        #             bordroekle.mayis_calisilan_gun=bordro1[i][2]
        #             bordroekle.mayis_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.mayis_sgk_matrahi=bordro1[i][3]
        #             bordroekle.mayis_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.mayis_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.mayis_vergi_dilimi=bordro1[i][25]
        #             bordroekle.mayis_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.mayis_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.mayis_vergi_matrahi=bordro1[i][6]
        #             bordroekle.mayis_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.mayis_asgari_vergi=bordro1[i][9]
        #             bordroekle.mayis_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.mayis_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.mayis_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.mayis_damga_vergisi=bordro1[i][12]
        #             bordroekle.mayis_gelir_vergisi=bordro1[i][13]
        #             bordroekle.mayis_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.mayis_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.mayis_net_ucret=bordro1[i][14]
        #             bordroekle.mayis_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.mayis_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.mayis_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.mayis_toplam_maliyet=bordro1[i][18]
        #             bordroekle.mayis_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.mayis_odenecek_sgk=bordro1[i][21]
        #             bordroekle.mayis_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.mayis_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==5:
        #             bordroekle.haziran_brut=bordro1[i][19]
        #             bordroekle.haziran_calisilan_gun=bordro1[i][2]
        #             bordroekle.haziran_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.haziran_sgk_matrahi=bordro1[i][3]
        #             bordroekle.haziran_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.haziran_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.haziran_vergi_dilimi=bordro1[i][25]
        #             bordroekle.haziran_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.haziran_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.haziran_vergi_matrahi=bordro1[i][6]
        #             bordroekle.haziran_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.haziran_asgari_vergi=bordro1[i][9]
        #             bordroekle.haziran_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.haziran_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.haziran_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.haziran_damga_vergisi=bordro1[i][12]
        #             bordroekle.haziran_gelir_vergisi=bordro1[i][13]
        #             bordroekle.haziran_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.haziran_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.haziran_net_ucret=bordro1[i][14]
        #             bordroekle.haziran_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.haziran_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.haziran_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.haziran_toplam_maliyet=bordro1[i][18]
        #             bordroekle.haziran_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.haziran_odenecek_sgk=bordro1[i][21]
        #             bordroekle.haziran_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.haziran_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==6:
        #             bordroekle.temmuz_brut=bordro1[i][19]
        #             bordroekle.temmuz_calisilan_gun=bordro1[i][2]
        #             bordroekle.temmuz_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.temmuz_sgk_matrahi=bordro1[i][3]
        #             bordroekle.temmuz_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.temmuz_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.temmuz_vergi_dilimi=bordro1[i][25]
        #             bordroekle.temmuz_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.temmuz_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.temmuz_vergi_matrahi=bordro1[i][6]
        #             bordroekle.temmuz_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.temmuz_asgari_vergi=bordro1[i][9]
        #             bordroekle.temmuz_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.temmuz_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.temmuz_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.temmuz_damga_vergisi=bordro1[i][12]
        #             bordroekle.temmuz_gelir_vergisi=bordro1[i][13]
        #             bordroekle.temmuz_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.temmuz_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.temmuz_net_ucret=bordro1[i][14]
        #             bordroekle.temmuz_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.temmuz_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.temmuz_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.temmuz_toplam_maliyet=bordro1[i][18]
        #             bordroekle.temmuz_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.temmuz_odenecek_sgk=bordro1[i][21]
        #             bordroekle.temmuz_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.temmuz_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==7:
        #             bordroekle.agustos_brut=bordro1[i][19]
        #             bordroekle.agustos_calisilan_gun=bordro1[i][2]
        #             bordroekle.agustos_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.agustos_sgk_matrahi=bordro1[i][3]
        #             bordroekle.agustos_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.agustos_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.agustos_vergi_dilimi=bordro1[i][25]
        #             bordroekle.agustos_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.agustos_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.agustos_vergi_matrahi=bordro1[i][6]
        #             bordroekle.agustos_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.agustos_asgari_vergi=bordro1[i][9]
        #             bordroekle.agustos_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.agustos_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.agustos_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.agustos_damga_vergisi=bordro1[i][12]
        #             bordroekle.agustos_gelir_vergisi=bordro1[i][13]
        #             bordroekle.agustos_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.agustos_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.agustos_net_ucret=bordro1[i][14]
        #             bordroekle.agustos_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.agustos_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.agustos_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.agustos_toplam_maliyet=bordro1[i][18]
        #             bordroekle.agustos_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.agustos_odenecek_sgk=bordro1[i][21]
        #             bordroekle.agustos_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.agustos_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==8:
        #             bordroekle.eylul_brut=bordro1[i][19]
        #             bordroekle.eylul_calisilan_gun=bordro1[i][2]
        #             bordroekle.eylul_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.eylul_sgk_matrahi=bordro1[i][3]
        #             bordroekle.eylul_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.eylul_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.eylul_vergi_dilimi=bordro1[i][25]
        #             bordroekle.eylul_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.eylul_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.eylul_vergi_matrahi=bordro1[i][6]
        #             bordroekle.eylul_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.eylul_asgari_vergi=bordro1[i][9]
        #             bordroekle.eylul_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.eylul_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.eylul_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.eylul_damga_vergisi=bordro1[i][12]
        #             bordroekle.eylul_gelir_vergisi=bordro1[i][13]
        #             bordroekle.eylul_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.eylul_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.eylul_net_ucret=bordro1[i][14]
        #             bordroekle.eylul_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.eylul_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.eylul_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.eylul_toplam_maliyet=bordro1[i][18]
        #             bordroekle.eylul_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.eylul_odenecek_sgk=bordro1[i][21]
        #             bordroekle.eylul_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.eylul_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==9:
        #             bordroekle.ekim_brut=bordro1[i][19]
        #             bordroekle.ekim_calisilan_gun=bordro1[i][2]
        #             bordroekle.ekim_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.ekim_sgk_matrahi=bordro1[i][3]
        #             bordroekle.ekim_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.ekim_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.ekim_vergi_dilimi=bordro1[i][25]
        #             bordroekle.ekim_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.ekim_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.ekim_vergi_matrahi=bordro1[i][6]
        #             bordroekle.ekim_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.ekim_asgari_vergi=bordro1[i][9]
        #             bordroekle.ekim_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.ekim_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.ekim_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.ekim_damga_vergisi=bordro1[i][12]
        #             bordroekle.ekim_gelir_vergisi=bordro1[i][13]
        #             bordroekle.ekim_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.ekim_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.ekim_net_ucret=bordro1[i][14]
        #             bordroekle.ekim_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.ekim_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.ekim_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.ekim_toplam_maliyet=bordro1[i][18]
        #             bordroekle.ekim_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.ekim_odenecek_sgk=bordro1[i][21]
        #             bordroekle.ekim_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.ekim_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==10:
        #             bordroekle.kasim_brut=bordro1[i][19]
        #             bordroekle.kasim_calisilan_gun=bordro1[i][2]
        #             bordroekle.kasim_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.kasim_sgk_matrahi=bordro1[i][3]
        #             bordroekle.kasim_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.kasim_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.kasim_vergi_dilimi=bordro1[i][25]
        #             bordroekle.kasim_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.kasim_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.kasim_vergi_matrahi=bordro1[i][6]
        #             bordroekle.kasim_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.kasim_asgari_vergi=bordro1[i][9]
        #             bordroekle.kasim_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.kasim_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.kasim_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.kasim_damga_vergisi=bordro1[i][12]
        #             bordroekle.kasim_gelir_vergisi=bordro1[i][13]
        #             bordroekle.kasim_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.kasim_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.kasim_net_ucret=bordro1[i][14]
        #             bordroekle.kasim_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.kasim_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.kasim_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.kasim_toplam_maliyet=bordro1[i][18]
        #             bordroekle.kasim_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.kasim_odenecek_sgk=bordro1[i][21]
        #             bordroekle.kasim_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.kasim_odenecek_damga_vergisi=bordro1[i][23]
        #     elif i==11:
        #             bordroekle.aralik_brut=bordro1[i][19]
        #             bordroekle.aralik_calisilan_gun=bordro1[i][2]
        #             bordroekle.aralik_bordroyaesasbrut=bordro1[i][1]
        #             bordroekle.aralik_sgk_matrahi=bordro1[i][3]
        #             bordroekle.aralik_sgk_kesintisi=bordro1[i][4]
        #             bordroekle.aralik_issizlik_kesintisi=bordro1[i][5]
        #             bordroekle.aralik_vergi_dilimi=bordro1[i][25]
        #             bordroekle.aralik_istisna_oncesi_gelir=bordro1[i][8]
        #             bordroekle.aralik_istisna_oncesi_damga_vergisi=bordro1[i][26]
        #             bordroekle.aralik_vergi_matrahi=bordro1[i][6]
        #             bordroekle.aralik_kumulatif_vergi=bordro1[i][7]
        #             bordroekle.aralik_asgari_vergi=bordro1[i][9]
        #             bordroekle.aralik_kumulatif_asgari_vergi=bordro1[i][10]
        #             bordroekle.aralik_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
        #             bordroekle.aralik_asgari_damga_vergisi_istisnasi=bordro1[i][27]
        #             bordroekle.aralik_damga_vergisi=bordro1[i][12]
        #             bordroekle.aralik_gelir_vergisi=bordro1[i][13]
        #             bordroekle.aralik_gelir_vergisi_istisnasi=bordro1[i][28]
        #             bordroekle.aralik_damga_vergisi_istisnasi=bordro1[i][29]
        #             bordroekle.aralik_net_ucret=bordro1[i][14]
        #             bordroekle.aralik_isveren_sgk_kesintisi=bordro1[i][15]
        #             bordroekle.aralik_isveren_issizlik_kesintisi=bordro1[i][16]
        #             bordroekle.aralik_toplam_sgk_kesintisi=bordro1[i][17]
        #             bordroekle.aralik_toplam_maliyet=bordro1[i][18]
        #             bordroekle.aralik_sgk_istisnasi=bordro1[i][20]
        #             bordroekle.aralik_odenecek_sgk=bordro1[i][21]
        #             bordroekle.aralik_odenecek_gelir_vergisi=bordro1[i][22]
        #             bordroekle.aralik_odenecek_damga_vergisi=bordro1[i][23]


        #     bordroekle.save()

        return redirect(reverse('user:employeedetail', kwargs={'id':id}))
    else:
        print("form is not vali1d")
    context={
        'form':form
    }
    return render(request,'updatemaas.html',context)
@login_required(login_url='user:login')
@user_passes_test(lambda u: u.groups.filter(name='mali_musavir').exists() or u.groups.filter(name='muhasebe').exists() or u.groups.filter(name='admin').exists())
def updatebymonth(request,id,maasid,month):
    maas1=get_object_or_404(maas,id=maasid)
    form=MaasRegisterForm(request.POST or None,instance=maas1)





    if form.is_valid():
            maas1=form.save(commit=False)
            maas1.save()
            maas2=maas.objects.get(id=maasid)
            bordroekle=bordro.objects.get(maas_id=maas2)
            calisan1=calisan.objects.get(id=id)


            bordro1=getlist1(request,id,maas2.yil,calisan1.calisan_tesvik,calisan1.calisan_engelli,calisan1.calisan_indirim)

            for i in range(12):
                if i==0:
                        bordroekle.ocak_brut=bordro1[i][19]
                        bordroekle.ocak_calisilan_gun=bordro1[i][2]
                        bordroekle.ocak_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.ocak_sgk_matrahi=bordro1[i][3]
                        bordroekle.ocak_sgk_kesintisi=bordro1[i][4]
                        bordroekle.ocak_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.ocak_vergi_dilimi=bordro1[i][25]
                        bordroekle.ocak_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.ocak_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.ocak_vergi_matrahi=bordro1[i][6]
                        bordroekle.ocak_kumulatif_vergi=bordro1[i][7]
                        bordroekle.ocak_asgari_vergi=bordro1[i][9]
                        bordroekle.ocak_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.ocak_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.ocak_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.ocak_damga_vergisi=bordro1[i][12]
                        bordroekle.ocak_gelir_vergisi=bordro1[i][13]
                        bordroekle.ocak_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.ocak_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.ocak_net_ucret=bordro1[i][14]
                        bordroekle.ocak_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.ocak_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.ocak_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.ocak_toplam_maliyet=bordro1[i][18]
                        bordroekle.ocak_sgk_istisnasi=bordro1[i][20]
                        bordroekle.ocak_odenecek_sgk=bordro1[i][21]
                        bordroekle.ocak_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.ocak_odenecek_damga_vergisi=bordro1[i][23]
                elif i==1:
                        bordroekle.subat_brut=bordro1[i][19]
                        bordroekle.subat_calisilan_gun=bordro1[i][2]
                        bordroekle.subat_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.subat_sgk_matrahi=bordro1[i][3]
                        bordroekle.subat_sgk_kesintisi=bordro1[i][4]
                        bordroekle.subat_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.subat_vergi_dilimi=bordro1[i][25]
                        bordroekle.subat_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.subat_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.subat_vergi_matrahi=bordro1[i][6]
                        bordroekle.subat_kumulatif_vergi=bordro1[i][7]
                        bordroekle.subat_asgari_vergi=bordro1[i][9]
                        bordroekle.subat_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.subat_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.subat_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.subat_damga_vergisi=bordro1[i][12]
                        bordroekle.subat_gelir_vergisi=bordro1[i][13]
                        bordroekle.subat_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.subat_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.subat_net_ucret=bordro1[i][14]
                        bordroekle.subat_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.subat_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.subat_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.subat_toplam_maliyet=bordro1[i][18]
                        bordroekle.subat_sgk_istisnasi=bordro1[i][20]
                        bordroekle.subat_odenecek_sgk=bordro1[i][21]
                        bordroekle.subat_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.subat_odenecek_damga_vergisi=bordro1[i][23]
                elif i==2:
                        bordroekle.mart_brut=bordro1[i][19]
                        bordroekle.mart_calisilan_gun=bordro1[i][2]
                        bordroekle.mart_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.mart_sgk_matrahi=bordro1[i][3]
                        bordroekle.mart_sgk_kesintisi=bordro1[i][4]
                        bordroekle.mart_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.mart_vergi_dilimi=bordro1[i][25]
                        bordroekle.mart_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.mart_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.mart_vergi_matrahi=bordro1[i][6]
                        bordroekle.mart_kumulatif_vergi=bordro1[i][7]
                        bordroekle.mart_asgari_vergi=bordro1[i][9]
                        bordroekle.mart_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.mart_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.mart_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.mart_damga_vergisi=bordro1[i][12]
                        bordroekle.mart_gelir_vergisi=bordro1[i][13]
                        bordroekle.mart_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.mart_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.mart_net_ucret=bordro1[i][14]
                        bordroekle.mart_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.mart_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.mart_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.mart_toplam_maliyet=bordro1[i][18]
                        bordroekle.mart_sgk_istisnasi=bordro1[i][20]
                        bordroekle.mart_odenecek_sgk=bordro1[i][21]
                        bordroekle.mart_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.mart_odenecek_damga_vergisi=bordro1[i][23]
                elif i==3:
                        bordroekle.nisan_brut=bordro1[i][19]
                        bordroekle.nisan_calisilan_gun=bordro1[i][2]
                        bordroekle.nisan_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.nisan_sgk_matrahi=bordro1[i][3]
                        bordroekle.nisan_sgk_kesintisi=bordro1[i][4]
                        bordroekle.nisan_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.nisan_vergi_dilimi=bordro1[i][25]
                        bordroekle.nisan_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.nisan_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.nisan_vergi_matrahi=bordro1[i][6]
                        bordroekle.nisan_kumulatif_vergi=bordro1[i][7]
                        bordroekle.nisan_asgari_vergi=bordro1[i][9]
                        bordroekle.nisan_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.nisan_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.nisan_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.nisan_damga_vergisi=bordro1[i][12]
                        bordroekle.nisan_gelir_vergisi=bordro1[i][13]
                        bordroekle.nisan_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.nisan_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.nisan_net_ucret=bordro1[i][14]
                        bordroekle.nisan_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.nisan_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.nisan_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.nisan_toplam_maliyet=bordro1[i][18]
                        bordroekle.nisan_sgk_istisnasi=bordro1[i][20]
                        bordroekle.nisan_odenecek_sgk=bordro1[i][21]
                        bordroekle.nisan_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.nisan_odenecek_damga_vergisi=bordro1[i][23]
                elif i==4:
                        bordroekle.mayis_brut=bordro1[i][19]
                        bordroekle.mayis_calisilan_gun=bordro1[i][2]
                        bordroekle.mayis_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.mayis_sgk_matrahi=bordro1[i][3]
                        bordroekle.mayis_sgk_kesintisi=bordro1[i][4]
                        bordroekle.mayis_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.mayis_vergi_dilimi=bordro1[i][25]
                        bordroekle.mayis_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.mayis_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.mayis_vergi_matrahi=bordro1[i][6]
                        bordroekle.mayis_kumulatif_vergi=bordro1[i][7]
                        bordroekle.mayis_asgari_vergi=bordro1[i][9]
                        bordroekle.mayis_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.mayis_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.mayis_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.mayis_damga_vergisi=bordro1[i][12]
                        bordroekle.mayis_gelir_vergisi=bordro1[i][13]
                        bordroekle.mayis_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.mayis_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.mayis_net_ucret=bordro1[i][14]
                        bordroekle.mayis_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.mayis_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.mayis_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.mayis_toplam_maliyet=bordro1[i][18]
                        bordroekle.mayis_sgk_istisnasi=bordro1[i][20]
                        bordroekle.mayis_odenecek_sgk=bordro1[i][21]
                        bordroekle.mayis_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.mayis_odenecek_damga_vergisi=bordro1[i][23]
                elif i==5:
                        bordroekle.haziran_brut=bordro1[i][19]
                        bordroekle.haziran_calisilan_gun=bordro1[i][2]
                        bordroekle.haziran_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.haziran_sgk_matrahi=bordro1[i][3]
                        bordroekle.haziran_sgk_kesintisi=bordro1[i][4]
                        bordroekle.haziran_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.haziran_vergi_dilimi=bordro1[i][25]
                        bordroekle.haziran_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.haziran_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.haziran_vergi_matrahi=bordro1[i][6]
                        bordroekle.haziran_kumulatif_vergi=bordro1[i][7]
                        bordroekle.haziran_asgari_vergi=bordro1[i][9]
                        bordroekle.haziran_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.haziran_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.haziran_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.haziran_damga_vergisi=bordro1[i][12]
                        bordroekle.haziran_gelir_vergisi=bordro1[i][13]
                        bordroekle.haziran_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.haziran_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.haziran_net_ucret=bordro1[i][14]
                        bordroekle.haziran_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.haziran_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.haziran_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.haziran_toplam_maliyet=bordro1[i][18]
                        bordroekle.haziran_sgk_istisnasi=bordro1[i][20]
                        bordroekle.haziran_odenecek_sgk=bordro1[i][21]
                        bordroekle.haziran_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.haziran_odenecek_damga_vergisi=bordro1[i][23]
                elif i==6:
                        bordroekle.temmuz_brut=bordro1[i][19]
                        bordroekle.temmuz_calisilan_gun=bordro1[i][2]
                        bordroekle.temmuz_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.temmuz_sgk_matrahi=bordro1[i][3]
                        bordroekle.temmuz_sgk_kesintisi=bordro1[i][4]
                        bordroekle.temmuz_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.temmuz_vergi_dilimi=bordro1[i][25]
                        bordroekle.temmuz_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.temmuz_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.temmuz_vergi_matrahi=bordro1[i][6]
                        bordroekle.temmuz_kumulatif_vergi=bordro1[i][7]
                        bordroekle.temmuz_asgari_vergi=bordro1[i][9]
                        bordroekle.temmuz_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.temmuz_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.temmuz_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.temmuz_damga_vergisi=bordro1[i][12]
                        bordroekle.temmuz_gelir_vergisi=bordro1[i][13]
                        bordroekle.temmuz_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.temmuz_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.temmuz_net_ucret=bordro1[i][14]
                        bordroekle.temmuz_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.temmuz_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.temmuz_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.temmuz_toplam_maliyet=bordro1[i][18]
                        bordroekle.temmuz_sgk_istisnasi=bordro1[i][20]
                        bordroekle.temmuz_odenecek_sgk=bordro1[i][21]
                        bordroekle.temmuz_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.temmuz_odenecek_damga_vergisi=bordro1[i][23]
                elif i==7:
                        bordroekle.agustos_brut=bordro1[i][19]
                        bordroekle.agustos_calisilan_gun=bordro1[i][2]
                        bordroekle.agustos_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.agustos_sgk_matrahi=bordro1[i][3]
                        bordroekle.agustos_sgk_kesintisi=bordro1[i][4]
                        bordroekle.agustos_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.agustos_vergi_dilimi=bordro1[i][25]
                        bordroekle.agustos_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.agustos_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.agustos_vergi_matrahi=bordro1[i][6]
                        bordroekle.agustos_kumulatif_vergi=bordro1[i][7]
                        bordroekle.agustos_asgari_vergi=bordro1[i][9]
                        bordroekle.agustos_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.agustos_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.agustos_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.agustos_damga_vergisi=bordro1[i][12]
                        bordroekle.agustos_gelir_vergisi=bordro1[i][13]
                        bordroekle.agustos_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.agustos_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.agustos_net_ucret=bordro1[i][14]
                        bordroekle.agustos_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.agustos_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.agustos_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.agustos_toplam_maliyet=bordro1[i][18]
                        bordroekle.agustos_sgk_istisnasi=bordro1[i][20]
                        bordroekle.agustos_odenecek_sgk=bordro1[i][21]
                        bordroekle.agustos_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.agustos_odenecek_damga_vergisi=bordro1[i][23]
                elif i==8:
                        bordroekle.eylul_brut=bordro1[i][19]
                        bordroekle.eylul_calisilan_gun=bordro1[i][2]
                        bordroekle.eylul_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.eylul_sgk_matrahi=bordro1[i][3]
                        bordroekle.eylul_sgk_kesintisi=bordro1[i][4]
                        bordroekle.eylul_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.eylul_vergi_dilimi=bordro1[i][25]
                        bordroekle.eylul_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.eylul_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.eylul_vergi_matrahi=bordro1[i][6]
                        bordroekle.eylul_kumulatif_vergi=bordro1[i][7]
                        bordroekle.eylul_asgari_vergi=bordro1[i][9]
                        bordroekle.eylul_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.eylul_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.eylul_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.eylul_damga_vergisi=bordro1[i][12]
                        bordroekle.eylul_gelir_vergisi=bordro1[i][13]
                        bordroekle.eylul_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.eylul_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.eylul_net_ucret=bordro1[i][14]
                        bordroekle.eylul_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.eylul_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.eylul_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.eylul_toplam_maliyet=bordro1[i][18]
                        bordroekle.eylul_sgk_istisnasi=bordro1[i][20]
                        bordroekle.eylul_odenecek_sgk=bordro1[i][21]
                        bordroekle.eylul_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.eylul_odenecek_damga_vergisi=bordro1[i][23]
                elif i==9:
                        bordroekle.ekim_brut=bordro1[i][19]
                        bordroekle.ekim_calisilan_gun=bordro1[i][2]
                        bordroekle.ekim_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.ekim_sgk_matrahi=bordro1[i][3]
                        bordroekle.ekim_sgk_kesintisi=bordro1[i][4]
                        bordroekle.ekim_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.ekim_vergi_dilimi=bordro1[i][25]
                        bordroekle.ekim_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.ekim_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.ekim_vergi_matrahi=bordro1[i][6]
                        bordroekle.ekim_kumulatif_vergi=bordro1[i][7]
                        bordroekle.ekim_asgari_vergi=bordro1[i][9]
                        bordroekle.ekim_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.ekim_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.ekim_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.ekim_damga_vergisi=bordro1[i][12]
                        bordroekle.ekim_gelir_vergisi=bordro1[i][13]
                        bordroekle.ekim_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.ekim_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.ekim_net_ucret=bordro1[i][14]
                        bordroekle.ekim_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.ekim_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.ekim_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.ekim_toplam_maliyet=bordro1[i][18]
                        bordroekle.ekim_sgk_istisnasi=bordro1[i][20]
                        bordroekle.ekim_odenecek_sgk=bordro1[i][21]
                        bordroekle.ekim_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.ekim_odenecek_damga_vergisi=bordro1[i][23]
                elif i==10:
                        bordroekle.kasim_brut=bordro1[i][19]
                        bordroekle.kasim_calisilan_gun=bordro1[i][2]
                        bordroekle.kasim_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.kasim_sgk_matrahi=bordro1[i][3]
                        bordroekle.kasim_sgk_kesintisi=bordro1[i][4]
                        bordroekle.kasim_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.kasim_vergi_dilimi=bordro1[i][25]
                        bordroekle.kasim_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.kasim_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.kasim_vergi_matrahi=bordro1[i][6]
                        bordroekle.kasim_kumulatif_vergi=bordro1[i][7]
                        bordroekle.kasim_asgari_vergi=bordro1[i][9]
                        bordroekle.kasim_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.kasim_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.kasim_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.kasim_damga_vergisi=bordro1[i][12]
                        bordroekle.kasim_gelir_vergisi=bordro1[i][13]
                        bordroekle.kasim_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.kasim_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.kasim_net_ucret=bordro1[i][14]
                        bordroekle.kasim_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.kasim_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.kasim_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.kasim_toplam_maliyet=bordro1[i][18]
                        bordroekle.kasim_sgk_istisnasi=bordro1[i][20]
                        bordroekle.kasim_odenecek_sgk=bordro1[i][21]
                        bordroekle.kasim_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.kasim_odenecek_damga_vergisi=bordro1[i][23]
                elif i==11:
                        bordroekle.aralik_brut=bordro1[i][19]
                        bordroekle.aralik_calisilan_gun=bordro1[i][2]
                        bordroekle.aralik_bordroyaesasbrut=bordro1[i][1]
                        bordroekle.aralik_sgk_matrahi=bordro1[i][3]
                        bordroekle.aralik_sgk_kesintisi=bordro1[i][4]
                        bordroekle.aralik_issizlik_kesintisi=bordro1[i][5]
                        bordroekle.aralik_vergi_dilimi=bordro1[i][25]
                        bordroekle.aralik_istisna_oncesi_gelir=bordro1[i][8]
                        bordroekle.aralik_istisna_oncesi_damga_vergisi=bordro1[i][26]
                        bordroekle.aralik_vergi_matrahi=bordro1[i][6]
                        bordroekle.aralik_kumulatif_vergi=bordro1[i][7]
                        bordroekle.aralik_asgari_vergi=bordro1[i][9]
                        bordroekle.aralik_kumulatif_asgari_vergi=bordro1[i][10]
                        bordroekle.aralik_asgari_gelir_vergisi_istisnasi=bordro1[i][11]
                        bordroekle.aralik_asgari_damga_vergisi_istisnasi=bordro1[i][27]
                        bordroekle.aralik_damga_vergisi=bordro1[i][12]
                        bordroekle.aralik_gelir_vergisi=bordro1[i][13]
                        bordroekle.aralik_gelir_vergisi_istisnasi=bordro1[i][28]
                        bordroekle.aralik_damga_vergisi_istisnasi=bordro1[i][29]
                        bordroekle.aralik_net_ucret=bordro1[i][14]
                        bordroekle.aralik_isveren_sgk_kesintisi=bordro1[i][15]
                        bordroekle.aralik_isveren_issizlik_kesintisi=bordro1[i][16]
                        bordroekle.aralik_toplam_sgk_kesintisi=bordro1[i][17]
                        bordroekle.aralik_toplam_maliyet=bordro1[i][18]
                        bordroekle.aralik_sgk_istisnasi=bordro1[i][20]
                        bordroekle.aralik_odenecek_sgk=bordro1[i][21]
                        bordroekle.aralik_odenecek_gelir_vergisi=bordro1[i][22]
                        bordroekle.aralik_odenecek_damga_vergisi=bordro1[i][23]


            bordroekle.save()
            return redirect(reverse('user:employeedetail', kwargs={'id':id}))
    else:
            print(form.errors)
            print("form is not valid")



    if month=='Ocak':
        maastutar1=True
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Şubat':
        maastutar2=True
        maastutar1=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False


    elif month=='Mart':
        maastutar3=True
        maastutar1=False
        maastutar2=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Nisan':
        maastutar4=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Mayıs':
        maastutar5=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Haziran':
        maastutar6=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Temmuz':
        maastutar7=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Ağustos':
        maastutar8=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Eylül':
        maastutar9=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar10=False
        maastutar11=False
        maastutar12=False

    elif month=='Ekim':
        maastutar10=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar11=False
        maastutar12=False

    elif month=='Kasım':
        maastutar11=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar12=False


    elif month=='Aralık':
        maastutar12=True
        maastutar1=False
        maastutar2=False
        maastutar3=False
        maastutar4=False
        maastutar5=False
        maastutar6=False
        maastutar7=False
        maastutar8=False
        maastutar9=False
        maastutar10=False
        maastutar11=False
    context={
        'form':form,
        'maastutar1':maastutar1,
        'maastutar2':maastutar2,
        'maastutar3':maastutar3,
        'maastutar4':maastutar4,
        'maastutar5':maastutar5,
        'maastutar6':maastutar6,
        'maastutar7':maastutar7,
        'maastutar8':maastutar8,
        'maastutar9':maastutar9,
        'maastutar10':maastutar10,
        'maastutar11':maastutar11,
        'maastutar12':maastutar12,
    }


    return render(request,'updatebymonth.html',context)


from .my_caphtcha import CaptchaForm
def loginUser(request):

    form=LoginForm(request.POST or None)
    context={
        'form':form,
        'captcha':CaptchaForm()

    }
    if request.method=='POST':
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Kullanıcı Adı veya Parola Hatalı')
            return render(request,'user/login.html',context)

        login(request,user)
        return redirect('user:homepage')
    return render(request, 'user/login.html',context)

def logoutUser(request):
    logout(request)
    return  loginUser(request)


