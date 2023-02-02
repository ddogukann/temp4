
from copyreg import pickle
from turtle import clear, left
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import hesaplama
import calendar
from .forms import monthsanddays
from django.contrib import messages
from app.tekayhesaplama import hesaplama1,get_nettenbrute

# Create your views here.
from datetime import datetime,timedelta

brutucret1=[]
gunsayisi1=[]
nettenbrut1=[]
argegun=[]
indirimm=[]
htmlrange=[1,2,3,4,5,6,7,8,9,10,11,12]
hesaplamaturu=""
egitimdurumu=[]
calisanturu=[""]
engelli=[""]
hesaplamayil=[]
emeklicalisan=[]
gosterilenbrut=[]
otuzbesvergidilimi=[]
yirmiyedivergidilimi=[]
yirmivergidilimi=[]
onbesvergidilimi=[]
ocakhaziranasgari=5004
temmuzagustosasgari=6471
birinciderece=[]
ikinciderece=[]
ucuncuderece=[]
sgkkesintiorani1=[]
emeklisgkorani=[]
issizlikkesintiorani=[]
gelirvergioran1=[]
gelirvergioran2=[]
gelirvergioran3=[]
gelirvergioran4=[]
egitim1geliroran=[]
egitim2geliroran=[]
egitim3geliroran=[]
issizlikisverenoran=[]
damgavergiorani=[]
indirimorani5510=[]
sgkkesintiorani=[]
isverenissizlikoran=[]
issizlikisverenoran=[]
aylikasgari=[]
asgaritavanorani=[]
asgarimatrahorani=[]
parabirimi=[]
dolar=0
euro=0


# @login_required(login_url="user:login")
def index(request):
    context={}


    
    
    if request.method == 'POST':
        context= monthsanddays(request.POST)
        
        if context.is_valid():
       
            dolar=float(getdolar()[0][1])

            euro=float(geteuro()[0][1])
            brutucret1.clear()
            gosterilenbrut.clear()
            gunsayisi1.clear()
            indirimm.clear()
            nettenbrut1.clear()
            calisanturu.clear()
            egitimdurumu.clear()
            argegun.clear()
            engelli.clear()
            emeklicalisan.clear()
            hesaplamayil.clear()
            parabirimi.clear()
            parabirimi.append(context.cleaned_data.get("parabirimi"))
            hesaplamaturu=context.cleaned_data['hesaplamaturu']
            calisanturu.append(context.cleaned_data['calisanturu'])
            egitimdurumu.append(context.cleaned_data['egitimdurumu'])
            engelli.append(context.cleaned_data['engelliderecesi'])
            emeklicalisan.append(context.cleaned_data['emeklicalisan'])
            hesaplamayil.append(context.cleaned_data['hesaplamayili'])
            data=hesaplama.objects.get(hesaplama_yili=hesaplamayil[0])
            otuzbesvergidilimi.append(data.otuzbesvergidilimi)
            yirmiyedivergidilimi.append(data.yirmiyedivergidilimi)
            yirmivergidilimi.append(data.yirmivergidilimi)
            onbesvergidilimi.append(data.onbesvergidilimi)
            ocakhaziranasgari=5004
            temmuzagustosasgari=6471
            birinciderece.append(data.birinciderece)
            ikinciderece.append(data.ikinciderece)
            ucuncuderece.append(data.ucuncuderece)
            sgkkesintiorani1.append(data.sgkkesintiorani1)
            emeklisgkorani.append(data.emeklisgkorani)
            issizlikkesintiorani.append(data.issizlikkesintiorani)
            gelirvergioran1.append(data.gelirvergioran1)
            gelirvergioran2.append(data.gelirvergioran2)
            gelirvergioran3.append(data.gelirvergioran3)
            gelirvergioran4.append(data.gelirvergioran4)
            egitim1geliroran.append(data.egitim1geliroran)
            egitim2geliroran.append(data.egitim2geliroran)
            egitim3geliroran.append(data.egitim3geliroran)
            issizlikisverenoran.append(data.issizlikisverenoran)
            damgavergiorani.append(data.damgavergiorani)
            indirimorani5510.append(data.indirimorani5510)
            sgkkesintiorani.append(data.sgkkesintiorani)
            isverenissizlikoran.append(data.isverenissizlikoran)
            issizlikisverenoran.append(data.issizlikisverenoran)
            asgaritavanorani.append(data.asgaritavanorani)
            asgarimatrahorani.append(data.asgarimatrahorani)

            aylikasgari.clear()
            aylikasgari.append(float(data.ocakasgari))
            aylikasgari.append(float(data.subatasgari))
            aylikasgari.append(float(data.martasgari))
            aylikasgari.append(float(data.nisanasgari))
            aylikasgari.append(float(data.mayisasgari))
            aylikasgari.append(float(data.haziranasgari))
            aylikasgari.append(float(data.temmuzasgari))
            aylikasgari.append(float(data.agustosasgari))
            aylikasgari.append(float(data.eylulasgari))
            aylikasgari.append(float(data.ekimasgari))
            aylikasgari.append(float(data.kasimasgari))
            aylikasgari.append(float(data.aralikasgari))

            
            
            if hesaplamaturu=="pick1":
                if parabirimi[0]=="pick0":
                    if float(aylikasgari[0])> float(context.cleaned_data['month1'].replace(",",".")) and float(context.cleaned_data['month1'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[0])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month1'].replace(",","."))
                    if float(aylikasgari[1])> float(context.cleaned_data['month2'].replace(",",".")) and float(context.cleaned_data['month2'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[1])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month2'].replace(",","."))
                    if float(aylikasgari[2])> float(context.cleaned_data['month3'].replace(",",".")) and float(context.cleaned_data['month3'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[2])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month3'].replace(",","."))
                    if float(aylikasgari[3])> float(context.cleaned_data['month4'].replace(",",".")) and float(context.cleaned_data['month4'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[3])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:    
                        brutucret1.append(context.cleaned_data['month4'].replace(",","."))
                    if float(aylikasgari[4])> float(context.cleaned_data['month5'].replace(",",".")) and float(context.cleaned_data['month5'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[4])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month5'].replace(",","."))
                    if float(aylikasgari[5])> float(context.cleaned_data['month6'].replace(",",".")) and float(context.cleaned_data['month6'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[5])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month6'].replace(",","."))
                    if float(aylikasgari[6])> float(context.cleaned_data['month7'].replace(",",".")) and float(context.cleaned_data['month7'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[6])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month7'].replace(",","."))
                    if float(aylikasgari[7])> float(context.cleaned_data['month8'].replace(",",".")) and float(context.cleaned_data['month8'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[7])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month8'].replace(",","."))
                    if float(aylikasgari[8])> float(context.cleaned_data['month9'].replace(",",".")) and float(context.cleaned_data['month9'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[8])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month9'].replace(",","."))
                    if float(aylikasgari[9])> float(context.cleaned_data['month10'].replace(",",".")) and float(context.cleaned_data['month10'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[9])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month10'].replace(",","."))
                    if float(aylikasgari[10])> float(context.cleaned_data['month11'].replace(",",".")) and float(context.cleaned_data['month11'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[10])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month11'].replace(",","."))
                    if float(aylikasgari[11])> float(context.cleaned_data['month12'].replace(",",".")) and float(context.cleaned_data['month12'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[11])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(context.cleaned_data['month12'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month1'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month2'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month3'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month4'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month5'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month6'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month7'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month8'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month9'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month10'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month11'].replace(",","."))
                    gosterilenbrut.append(context.cleaned_data['month12'].replace(",","."))
                if parabirimi[0]=="pick1":
                    if float(aylikasgari[0])> float(context.cleaned_data['month1'].replace(",","."))*dolar and float(context.cleaned_data['month1'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[0])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month1'].replace(",","."))*dolar)
                    if float(aylikasgari[1])> float(context.cleaned_data['month2'].replace(",","."))*dolar and float(context.cleaned_data['month2'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[1])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month2'].replace(",","."))*dolar)
                    if float(aylikasgari[2])> float(context.cleaned_data['month3'].replace(",","."))*dolar and float(context.cleaned_data['month3'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[2])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month3'].replace(",","."))*dolar)
                    if float(aylikasgari[3])> float(context.cleaned_data['month4'].replace(",","."))*dolar and float(context.cleaned_data['month4'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[3])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:    
                        brutucret1.append(float(context.cleaned_data['month4'].replace(",","."))*dolar)
                    if float(aylikasgari[4])> float(context.cleaned_data['month5'].replace(",","."))*dolar and float(context.cleaned_data['month5'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[4])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month5'].replace(",","."))*dolar)
                    if float(aylikasgari[5])> float(context.cleaned_data['month6'].replace(",","."))*dolar and float(context.cleaned_data['month6'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[5])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month6'].replace(",","."))*dolar)
                    if float(aylikasgari[6])> float(context.cleaned_data['month7'].replace(",","."))*dolar and float(context.cleaned_data['month7'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[6])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month7'].replace(",","."))*dolar)
                    if float(aylikasgari[7])> float(context.cleaned_data['month8'].replace(",","."))*dolar and float(context.cleaned_data['month8'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[7])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month8'].replace(",","."))*dolar)
                    if float(aylikasgari[8])> float(context.cleaned_data['month9'].replace(",","."))*dolar and float(context.cleaned_data['month9'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[8])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month9'].replace(",","."))*dolar)
                    if float(aylikasgari[9])> float(context.cleaned_data['month10'].replace(",","."))*dolar and float(context.cleaned_data['month10'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[9])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month10'].replace(",","."))*dolar)
                    if float(aylikasgari[10])> float(context.cleaned_data['month11'].replace(",","."))*dolar and float(context.cleaned_data['month11'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[10])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month11'].replace(",","."))*dolar)
                    if float(aylikasgari[11])> float(context.cleaned_data['month12'].replace(",","."))*dolar and float(context.cleaned_data['month12'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[11])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month12'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month1'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month2'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month3'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month4'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month5'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month6'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month7'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month8'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month9'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month10'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month11'].replace(",","."))*dolar)
                    gosterilenbrut.append(float(context.cleaned_data['month12'].replace(",","."))*dolar)
                if parabirimi[0]=="pick2":
                    if float(aylikasgari[0])> float(context.cleaned_data['month1'].replace(",","."))*euro and float(context.cleaned_data['month1'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[0])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month1'].replace(",","."))*euro)
                    if float(aylikasgari[1])> float(context.cleaned_data['month2'].replace(",","."))*euro and float(context.cleaned_data['month2'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[1])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month2'].replace(",","."))*euro)
                    if float(aylikasgari[2])> float(context.cleaned_data['month3'].replace(",","."))*euro and float(context.cleaned_data['month3'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[2])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month3'].replace(",","."))*euro)
                    if float(aylikasgari[3])> float(context.cleaned_data['month4'].replace(",","."))*euro and float(context.cleaned_data['month4'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[3])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:    
                        brutucret1.append(float(context.cleaned_data['month4'].replace(",","."))*euro)
                    if float(aylikasgari[4])> float(context.cleaned_data['month5'].replace(",","."))*euro and float(context.cleaned_data['month5'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[4])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month5'].replace(",","."))*euro)
                    if float(aylikasgari[5])> float(context.cleaned_data['month6'].replace(",","."))*euro and float(context.cleaned_data['month6'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[5])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month6'].replace(",","."))*euro)
                    if float(aylikasgari[6])> float(context.cleaned_data['month7'].replace(",","."))*euro and float(context.cleaned_data['month7'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[6])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month7'].replace(",","."))*euro)
                    if float(aylikasgari[7])> float(context.cleaned_data['month8'].replace(",","."))*euro and float(context.cleaned_data['month8'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[7])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month8'].replace(",","."))*euro)
                    if float(aylikasgari[8])> float(context.cleaned_data['month9'].replace(",","."))*euro and float(context.cleaned_data['month9'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[8])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month9'].replace(",","."))*euro)
                    if float(aylikasgari[9])> float(context.cleaned_data['month10'].replace(",","."))*euro and float(context.cleaned_data['month10'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[9])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month10'].replace(",","."))*euro)
                    if float(aylikasgari[10])> float(context.cleaned_data['month11'].replace(",","."))*euro and float(context.cleaned_data['month11'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[10])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month11'].replace(",","."))*euro)
                    if float(aylikasgari[11])> float(context.cleaned_data['month12'].replace(",","."))*euro and float(context.cleaned_data['month12'].replace(",","."))!=0:
                        brutucret1.append(aylikasgari[11])
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        brutucret1.append(float(context.cleaned_data['month12'].replace(",","."))*euro)

                    gosterilenbrut.append(float(context.cleaned_data['month1'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month2'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month3'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month4'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month5'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month6'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month7'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month8'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month9'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month10'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month11'].replace(",","."))*euro)
                    gosterilenbrut.append(float(context.cleaned_data['month12'].replace(",","."))*euro)
                gunsayisi1.append(context.cleaned_data['day1'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day2'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day3'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day4'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day5'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day6'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day7'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day8'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day9'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day10'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day11'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day12'].replace(",","."))
                if float(context.cleaned_data['argegun1']) > float(gunsayisi1[0]):
                    argegun.append(gunsayisi1[0])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun1'].replace(",","."))
                if float(context.cleaned_data['argegun2']) > float(gunsayisi1[1]):
                    argegun.append(gunsayisi1[1])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun2'].replace(",","."))
                if float(context.cleaned_data['argegun3']) > float(gunsayisi1[2]):
                    argegun.append(gunsayisi1[2])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun3'].replace(",","."))
                if float(context.cleaned_data['argegun4']) > float(gunsayisi1[3]):
                    argegun.append(gunsayisi1[3])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun4'].replace(",","."))
                if float(context.cleaned_data['argegun5']) > float(gunsayisi1[4]):
                    argegun.append(gunsayisi1[4])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun5'].replace(",","."))
                if float(context.cleaned_data['argegun6']) > float(gunsayisi1[5]):
                    argegun.append(gunsayisi1[5])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun6'].replace(",","."))
                if float(context.cleaned_data['argegun7']) > float(gunsayisi1[6]):
                    argegun.append(gunsayisi1[6])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun7'].replace(",","."))
                if float(context.cleaned_data['argegun8']) > float(gunsayisi1[7]):
                    argegun.append(gunsayisi1[7])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun8'].replace(",","."))
                if float(context.cleaned_data['argegun9']) > float(gunsayisi1[8]):
                    argegun.append(gunsayisi1[8])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun9'].replace(",","."))
                if float(context.cleaned_data['argegun10']) > float(gunsayisi1[9]):
                    argegun.append(gunsayisi1[9])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun10'].replace(",","."))
                if float(context.cleaned_data['argegun11']) > float(gunsayisi1[10]):
                    argegun.append(gunsayisi1[10])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun11'].replace(",","."))
                if float(context.cleaned_data['argegun12']) > float(gunsayisi1[11]):
                    argegun.append(gunsayisi1[11])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun12'].replace(",","."))
                if (calisanturu[0]=='pick4' or calisanturu[0]=='pick5' or calisanturu[0]=='pick6' or calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9') and context.cleaned_data['ellibesonindirimi']==True :
                    indirimm.append(False)
                    messages.add_message(request, messages.INFO, 'Seçilen çalışan türü için 5510/5746 indirimi uygulanamamaktadır.')
                else:
                    indirimm.append(context.cleaned_data['ellibesonindirimi'])
                
                context.clean()
                
                return calculate(request)
            elif hesaplamaturu=="pick2":#emekli için oranları ddeğiştir
                if parabirimi[0]=="pick0":
                    if float(aylikasgari[0]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month1'].replace(",",".")) and float(context.cleaned_data['month1'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[0]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month1'].replace(",","."))
                    if float(aylikasgari[1]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month2'].replace(",",".")) and float(context.cleaned_data['month2'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[1]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month2'].replace(",","."))
                    if float(aylikasgari[2]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month3'].replace(",",".")) and float(context.cleaned_data['month3'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[2]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month3'].replace(",","."))
                    if float(aylikasgari[3]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month4'].replace(",",".")) and float(context.cleaned_data['month4'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[3]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month4'].replace(",","."))
                    if float(aylikasgari[4]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month5'].replace(",",".")) and float(context.cleaned_data['month5'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[4]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month5'].replace(",","."))
                    if float(aylikasgari[5]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month6'].replace(",",".")) and float(context.cleaned_data['month6'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[5]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month6'].replace(",","."))
                    if float(aylikasgari[6]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month7'].replace(",",".")) and float(context.cleaned_data['month7'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[6]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month7'].replace(",","."))
                    if float(aylikasgari[7]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month8'].replace(",",".")) and float(context.cleaned_data['month8'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[7]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month8'].replace(",","."))
                    if float(aylikasgari[8]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month9'].replace(",",".")) and float(context.cleaned_data['month9'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[8]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month9'].replace(",","."))
                    if float(aylikasgari[9]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month10'].replace(",",".")) and float(context.cleaned_data['month10'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[9]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month10'].replace(",","."))
                    if float(aylikasgari[10]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month11'].replace(",",".")) and float(context.cleaned_data['month11'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[10]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month11'].replace(",","."))
                    if float(aylikasgari[11]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month12'].replace(",",".")) and float(context.cleaned_data['month12'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[11]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(context.cleaned_data['month12'].replace(",","."))
                elif parabirimi[0]=="pick1":
                    if float(aylikasgari[0]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month1'].replace(",","."))*dolar and float(context.cleaned_data['month1'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[0]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month1'].replace(",","."))*dolar)
                    if float(aylikasgari[1]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month2'].replace(",","."))*dolar and float(context.cleaned_data['month2'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[1]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month2'].replace(",","."))*dolar)
                    if float(aylikasgari[2]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month3'].replace(",","."))*dolar and float(context.cleaned_data['month3'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[2]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month3'].replace(",","."))*dolar)
                    if float(aylikasgari[3]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month4'].replace(",","."))*dolar and float(context.cleaned_data['month4'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[3]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month4'].replace(",","."))*dolar)
                    if float(aylikasgari[4]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month5'].replace(",","."))*dolar and float(context.cleaned_data['month5'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[4]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month5'].replace(",","."))*dolar)
                    if float(aylikasgari[5]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month6'].replace(",","."))*dolar and float(context.cleaned_data['month6'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[5]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month6'].replace(",","."))*dolar)
                    if float(aylikasgari[6]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month7'].replace(",","."))*dolar and float(context.cleaned_data['month7'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[6]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month7'].replace(",","."))*dolar)
                    if float(aylikasgari[7]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month8'].replace(",","."))*dolar and float(context.cleaned_data['month8'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[7]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month8'].replace(",","."))*dolar)
                    if float(aylikasgari[8]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month9'].replace(",","."))*dolar and float(context.cleaned_data['month9'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[8]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month9'].replace(",","."))*dolar)
                    if float(aylikasgari[9]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month10'].replace(",","."))*dolar and float(context.cleaned_data['month10'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[9]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month10'].replace(",","."))*dolar)
                    if float(aylikasgari[10]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month11'].replace(",","."))*dolar and float(context.cleaned_data['month11'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[10]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month11'].replace(",","."))*dolar)
                    if float(aylikasgari[11]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month12'].replace(",","."))*dolar and float(context.cleaned_data['month12'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[11]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month12'].replace(",","."))*dolar)
                elif parabirimi[0]=="pick2":
                    if float(aylikasgari[0]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month1'].replace(",","."))*euro and float(context.cleaned_data['month1'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[0]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month1'].replace(",","."))*euro)
                    if float(aylikasgari[1]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month2'].replace(",","."))*euro and float(context.cleaned_data['month2'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[1]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month2'].replace(",","."))*euro)
                    if float(aylikasgari[2]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month3'].replace(",","."))*euro and float(context.cleaned_data['month3'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[2]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month3'].replace(",","."))*euro)
                    if float(aylikasgari[3]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month4'].replace(",","."))*euro and float(context.cleaned_data['month4'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[3]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month4'].replace(",","."))*euro)
                    if float(aylikasgari[4]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month5'].replace(",","."))*euro and float(context.cleaned_data['month5'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[4]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month5'].replace(",","."))*euro)
                    if float(aylikasgari[5]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month6'].replace(",","."))*euro and float(context.cleaned_data['month6'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[5]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month6'].replace(",","."))*euro)
                    if float(aylikasgari[6]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month7'].replace(",","."))*euro and float(context.cleaned_data['month7'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[6]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month7'].replace(",","."))*euro)
                    if float(aylikasgari[7]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month8'].replace(",","."))*euro and float(context.cleaned_data['month8'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[7]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month8'].replace(",","."))*euro)
                    if float(aylikasgari[8]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month9'].replace(",","."))*euro and float(context.cleaned_data['month9'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[8]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month9'].replace(",","."))*euro)
                    if float(aylikasgari[9]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month10'].replace(",","."))*euro and float(context.cleaned_data['month10'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[9]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month10'].replace(",","."))*euro)
                    if float(aylikasgari[10]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month11'].replace(",","."))*euro and float(context.cleaned_data['month11'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[10]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month11'].replace(",","."))*euro)
                    if float(aylikasgari[11]*float(asgarimatrahorani[0]))> float(context.cleaned_data['month12'].replace(",","."))*euro and float(context.cleaned_data['month12'].replace(",","."))!=0:
                        nettenbrut1.append(aylikasgari[11]*float(asgarimatrahorani[0]))
                        messages.add_message(request, messages.INFO, 'Minimum tutarın altındaki aylar için asgari ücret uygulanmıştır.')
                    else:
                        nettenbrut1.append(float(context.cleaned_data['month12'].replace(",","."))*euro)
                gunsayisi1.append(context.cleaned_data['day1'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day2'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day3'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day4'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day5'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day6'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day7'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day8'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day9'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day10'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day11'].replace(",","."))
                gunsayisi1.append(context.cleaned_data['day12'].replace(",","."))
                if float(context.cleaned_data['argegun1']) > float(gunsayisi1[0]):
                    argegun.append(gunsayisi1[0])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun1'].replace(",","."))
                if float(context.cleaned_data['argegun2']) > float(gunsayisi1[1]):
                    argegun.append(gunsayisi1[1])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun2'].replace(",","."))
                if float(context.cleaned_data['argegun3']) > float(gunsayisi1[2]):
                    argegun.append(gunsayisi1[2])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun3'].replace(",","."))
                if float(context.cleaned_data['argegun4']) > float(gunsayisi1[3]):
                    argegun.append(gunsayisi1[3])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun4'].replace(",","."))
                if float(context.cleaned_data['argegun5']) > float(gunsayisi1[4]):
                    argegun.append(gunsayisi1[4])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun5'].replace(",","."))
                if float(context.cleaned_data['argegun6']) > float(gunsayisi1[5]):
                    argegun.append(gunsayisi1[5])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun6'].replace(",","."))
                if float(context.cleaned_data['argegun7']) > float(gunsayisi1[6]):
                    argegun.append(gunsayisi1[6])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun7'].replace(",","."))
                if float(context.cleaned_data['argegun8']) > float(gunsayisi1[7]):
                    argegun.append(gunsayisi1[7])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun8'].replace(",","."))
                if float(context.cleaned_data['argegun9']) > float(gunsayisi1[8]):
                    argegun.append(gunsayisi1[8])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun9'].replace(",","."))
                if float(context.cleaned_data['argegun10']) > float(gunsayisi1[9]):
                    argegun.append(gunsayisi1[9])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun10'].replace(",","."))
                if float(context.cleaned_data['argegun11']) > float(gunsayisi1[10]):
                    argegun.append(gunsayisi1[10])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun11'].replace(",","."))
                if float(context.cleaned_data['argegun12']) > float(gunsayisi1[11]):
                    argegun.append(gunsayisi1[11])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun12'].replace(",","."))
                if calisanturu[0]=='pick4' or calisanturu[0]=='pick5' or calisanturu[0]=='pick6' or calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9' and context.cleaned_data['ellibesonindirimi']==True  :
                    indirimm.append(False)
                    messages.add_message(request, messages.INFO, 'Seçilen çalışan türü için 5510/5746 indirimi uygulanamamaktadır.')
                else:
                    indirimm.append(context.cleaned_data['ellibesonindirimi'])
                get_nettenbrute1(nettenbrut1,gunsayisi1)
                return calculate(request)

            else:
                nettenbrut1.append(context.cleaned_data['month1'])
                nettenbrut1.append(context.cleaned_data['month2'])
                nettenbrut1.append(context.cleaned_data['month3'])
                nettenbrut1.append(context.cleaned_data['month4'])
                nettenbrut1.append(context.cleaned_data['month5'])
                nettenbrut1.append(context.cleaned_data['month6'])
                nettenbrut1.append(context.cleaned_data['month7'])
                nettenbrut1.append(context.cleaned_data['month8'])
                nettenbrut1.append(context.cleaned_data['month9'])
                nettenbrut1.append(context.cleaned_data['month10'])
                nettenbrut1.append(context.cleaned_data['month11'])
                nettenbrut1.append(context.cleaned_data['month12'])
                gunsayisi1.append(context.cleaned_data['day1'])
                gunsayisi1.append(context.cleaned_data['day2'])
                gunsayisi1.append(context.cleaned_data['day3'])
                gunsayisi1.append(context.cleaned_data['day4'])
                gunsayisi1.append(context.cleaned_data['day5'])
                gunsayisi1.append(context.cleaned_data['day6'])
                gunsayisi1.append(context.cleaned_data['day7'])
                gunsayisi1.append(context.cleaned_data['day8'])
                gunsayisi1.append(context.cleaned_data['day9'])
                gunsayisi1.append(context.cleaned_data['day10'])
                gunsayisi1.append(context.cleaned_data['day11'])
                gunsayisi1.append(context.cleaned_data['day12'])
                if float(context.cleaned_data['argegun1']) > float(gunsayisi1[0]):
                    argegun.append(gunsayisi1[0])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun1'].replace(",","."))
                if float(context.cleaned_data['argegun2']) > float(gunsayisi1[1]):
                    argegun.append(gunsayisi1[1])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun2'].replace(",","."))
                if float(context.cleaned_data['argegun3']) > float(gunsayisi1[2]):
                    argegun.append(gunsayisi1[2])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun3'].replace(",","."))
                if float(context.cleaned_data['argegun4']) > float(gunsayisi1[3]):
                    argegun.append(gunsayisi1[3])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun4'].replace(",","."))
                if float(context.cleaned_data['argegun5']) > float(gunsayisi1[4]):
                    argegun.append(gunsayisi1[4])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun5'].replace(",","."))
                if float(context.cleaned_data['argegun6']) > float(gunsayisi1[5]):
                    argegun.append(gunsayisi1[5])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun6'].replace(",","."))
                if float(context.cleaned_data['argegun7']) > float(gunsayisi1[6]):
                    argegun.append(gunsayisi1[6])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun7'].replace(",","."))
                if float(context.cleaned_data['argegun8']) > float(gunsayisi1[7]):
                    argegun.append(gunsayisi1[7])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun8'].replace(",","."))
                if float(context.cleaned_data['argegun9']) > float(gunsayisi1[8]):
                    argegun.append(gunsayisi1[8])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun9'].replace(",","."))
                if float(context.cleaned_data['argegun10']) > float(gunsayisi1[9]):
                    argegun.append(gunsayisi1[9])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun10'].replace(",","."))
                if float(context.cleaned_data['argegun11']) > float(gunsayisi1[10]):
                    argegun.append(gunsayisi1[10])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun11'].replace(",","."))
                if float(context.cleaned_data['argegun12']) > float(gunsayisi1[11]):
                    argegun.append(gunsayisi1[11])
                    messages.add_message(request, messages.INFO, 'Arge gün sayısı aylık çalışma gün sayısından fazla olamaz.')
                else:
                    argegun.append(context.cleaned_data['argegun12'].replace(",","."))
                if calisanturu[0]=='pick4' or calisanturu[0]=='pick5' or calisanturu[0]=='pick6' or calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9' and context.cleaned_data['ellibesonindirimi']==True  :
                    indirimm.append(False)
                    messages.add_message(request, messages.INFO, 'Seçilen çalışan türü için 5510/5746 indirimi uygulanamamaktadır.')
                else:
                    indirimm.append(context.cleaned_data['ellibesonindirimi'])
                get_maliyettenbrute(nettenbrut1,gunsayisi1)
                return calculate(request)


        else:

            print(context.errors.as_data())   
  

    context['form']=monthsanddays()
    return render(request, 'deneme.html',context)
            

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
def autouser(request,brutucret=[],gunsayisi=[],argegun1=[],tesvik="",engelli1="",indirim="",year="",parabirim="",emekli=""):

    indirimm.clear()
    calisanturu.clear()
    engelli.clear()
    indirimm.append(indirim)
    calisanturu.append(tesvik)
    engelli.append(engelli1)
    nettenbrut1.clear()
    gunsayisi1.clear()
    parabirimi.clear()
    emeklicalisan.clear()
    emeklicalisan.append(emekli)
    parabirimi.append(parabirim)
    data=hesaplama.objects.get(hesaplama_yili=year)
    otuzbesvergidilimi.append(data.otuzbesvergidilimi)
    yirmiyedivergidilimi.append(data.yirmiyedivergidilimi)
    yirmivergidilimi.append(data.yirmivergidilimi)
    onbesvergidilimi.append(data.onbesvergidilimi)
    ocakhaziranasgari=5004
    temmuzagustosasgari=6471
    birinciderece.append(data.birinciderece)
    ikinciderece.append(data.ikinciderece)
    ucuncuderece.append(data.ucuncuderece)
    sgkkesintiorani1.append(data.sgkkesintiorani1)
    emeklisgkorani.append(data.emeklisgkorani)
    issizlikkesintiorani.append(data.issizlikkesintiorani)
    gelirvergioran1.append(data.gelirvergioran1)
    gelirvergioran2.append(data.gelirvergioran2)
    gelirvergioran3.append(data.gelirvergioran3)
    gelirvergioran4.append(data.gelirvergioran4)
    egitim1geliroran.append(data.egitim1geliroran)
    egitim2geliroran.append(data.egitim2geliroran)
    egitim3geliroran.append(data.egitim3geliroran)
    issizlikisverenoran.append(data.issizlikisverenoran)
    damgavergiorani.append(data.damgavergiorani)
    indirimorani5510.append(data.indirimorani5510)
    sgkkesintiorani.append(data.sgkkesintiorani)
    isverenissizlikoran.append(data.isverenissizlikoran)
    issizlikisverenoran.append(data.issizlikisverenoran)
    asgaritavanorani.append(data.asgaritavanorani)
    asgarimatrahorani.append(data.asgarimatrahorani)

    aylikasgari.clear()
    aylikasgari.append(float(data.ocakasgari))
    aylikasgari.append(float(data.subatasgari))
    aylikasgari.append(float(data.martasgari))
    aylikasgari.append(float(data.nisanasgari))
    aylikasgari.append(float(data.mayisasgari))
    aylikasgari.append(float(data.haziranasgari))
    aylikasgari.append(float(data.temmuzasgari))
    aylikasgari.append(float(data.agustosasgari))
    aylikasgari.append(float(data.eylulasgari))
    aylikasgari.append(float(data.ekimasgari))
    aylikasgari.append(float(data.kasimasgari))
    aylikasgari.append(float(data.aralikasgari))   
    dolar=float(getdolar()[0][1])
    euro=float(geteuro()[0][1])
    for i in range(12):
        
        
            if parabirimi[0]=="pick0":
                nettenbrut1.append(brutucret[i])
                gunsayisi1.append(gunsayisi[i])
                argegun.append(argegun1[i])
                
            elif parabirimi[0]=="pick1":
                nettenbrut1.append(float(brutucret[i])*dolar)
                gunsayisi1.append(gunsayisi[i])
                argegun.append(argegun1[i])
                
            elif parabirimi[0]=="pick2":
                nettenbrut1.append(float(brutucret[i])*euro)
                gunsayisi1.append(gunsayisi[i])
                argegun.append(argegun1[i])
                
    get_nettenbrute1(nettenbrut1,gunsayisi1)
    return calculate(request)
def sendlist(request,brutucret=[],gunsayisi=[],argegun1=[],tesvik="",engelli1="",indirim="",year="",parabirim=""):
    indirimm.clear()
    calisanturu.clear()
    engelli.clear()
    indirimm.append(indirim)
    calisanturu.append(tesvik)
    engelli.append(engelli1)
    nettenbrut1.clear()
    gunsayisi1.clear()
    argegun.clear()
    parabirimi.clear()
    parabirimi.append(parabirim)
    data=hesaplama.objects.get(hesaplama_yili=year)
    otuzbesvergidilimi.append(data.otuzbesvergidilimi)
    yirmiyedivergidilimi.append(data.yirmiyedivergidilimi)
    yirmivergidilimi.append(data.yirmivergidilimi)
    onbesvergidilimi.append(data.onbesvergidilimi)
    ocakhaziranasgari=5004
    temmuzagustosasgari=6471
    birinciderece.append(data.birinciderece)
    ikinciderece.append(data.ikinciderece)
    ucuncuderece.append(data.ucuncuderece)
    sgkkesintiorani1.append(data.sgkkesintiorani1)
    emeklisgkorani.append(data.emeklisgkorani)
    issizlikkesintiorani.append(data.issizlikkesintiorani)
    gelirvergioran1.append(data.gelirvergioran1)
    gelirvergioran2.append(data.gelirvergioran2)
    gelirvergioran3.append(data.gelirvergioran3)
    gelirvergioran4.append(data.gelirvergioran4)
    egitim1geliroran.append(data.egitim1geliroran)
    egitim2geliroran.append(data.egitim2geliroran)
    egitim3geliroran.append(data.egitim3geliroran)
    issizlikisverenoran.append(data.issizlikisverenoran)
    damgavergiorani.append(data.damgavergiorani)
    indirimorani5510.append(data.indirimorani5510)
    sgkkesintiorani.append(data.sgkkesintiorani)
    isverenissizlikoran.append(data.isverenissizlikoran)
    issizlikisverenoran.append(data.issizlikisverenoran)
    asgaritavanorani.append(data.asgaritavanorani)
    asgarimatrahorani.append(data.asgarimatrahorani)
    dolar=float(getdolar()[0][1])
    euro=float(geteuro()[0][1])

    aylikasgari.clear()
    aylikasgari.append(float(data.ocakasgari))
    aylikasgari.append(float(data.subatasgari))
    aylikasgari.append(float(data.martasgari))
    aylikasgari.append(float(data.nisanasgari))
    aylikasgari.append(float(data.mayisasgari))
    aylikasgari.append(float(data.haziranasgari))
    aylikasgari.append(float(data.temmuzasgari))
    aylikasgari.append(float(data.agustosasgari))
    aylikasgari.append(float(data.eylulasgari))
    aylikasgari.append(float(data.ekimasgari))
    aylikasgari.append(float(data.kasimasgari))
    aylikasgari.append(float(data.aralikasgari))   
    
    for i in range(12):
        if parabirimi[0]=="pick0":
            nettenbrut1.append(brutucret[i])
            gunsayisi1.append(gunsayisi[i])
            argegun.append(argegun1[i])
        elif parabirimi[0]=="pick1":
            nettenbrut1.append(float(brutucret[i])*dolar)
            gunsayisi1.append(gunsayisi[i])
            argegun.append(argegun1[i])
        elif parabirimi[0]=="pick2":
            nettenbrut1.append(float(brutucret[i])*euro)
            gunsayisi1.append(gunsayisi[i])
            argegun.append(argegun1[i])
    get_nettenbrute1(nettenbrut1,gunsayisi1)
    empmaas=hesapla(brutucret1,gunsayisi1)
    
    return empmaas
def calculate(request):

    return render(request, "calculated.html", {
       

        'range':range(13),
        "maaslar":hesapla(brutucret1,gunsayisi1)
        })
    
def hesapla(brutucret1,gunsayisi1):
    brut= get_bordroyaesasbrut1(brutucret1, gunsayisi1)
    sgkmatrah= get_sgkmatrahi1(brutucret1, gunsayisi1)
    sgkkesintisi= get_sgkkesintisi1(brutucret1, gunsayisi1)
    issizlikkesintisi= get_issizlikkesintisi1(brutucret1, gunsayisi1)
    vergimatrah = get_vergimatrahi1(brutucret1, gunsayisi1)
    kumulatif1= get_kumulatifvergimatrahi1(brutucret1, gunsayisi1)
    istisnaoncesi1= get_istisnaoncesigelirvergisi1(brutucret1, gunsayisi1)
    asgarivergimatrah1= get_asgariucretvergimatrahi1(brutucret1,gunsayisi1)
    kumulatifasgari1= get_kumulatifasgariucret1(brutucret1,gunsayisi1)
    asgarigelirvergisiistisnasi1= get_asgarigelirvergisiistisnasi1(brutucret1,gunsayisi1)
    damgavergisi1= get_damgavergisi1(brutucret1,gunsayisi1)
    gelirvergisi1= get_gelirvergisiodemesi1(brutucret1,gunsayisi1)
    netucret1= get_netucret1(brutucret1,gunsayisi1)
    sgkisveren1= get_sgkisveren1(brutucret1,gunsayisi1)
    issizlikkesintisiisveren1= get_issizlikkesintisiisveren1(brutucret1,gunsayisi1)
    toplamsgk1= get_toplamsgkkesintisi1(brutucret1,gunsayisi1)
    toplam1= get_toplammaliyet1(brutucret1,gunsayisi1)
    aylar=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık","Toplam"]
    sgkistisnasi= get_sgkistisnasi(brutucret1,gunsayisi1)
    odeneceksgk=get_odeneceksgk()
    odenecekgelirvergisi=get_gelirvergisi()
    odenecekdamgavergisi=get_damgavergisiodemesi()
    geliroran=get_gelirvergidenemeoran()
    gelirödeme=get_gelirvergideneme()
    damga=get_indirimsizdamgavergisi()
    damgaistisnasi=get_damgaistisnasi()
    geliristisnasi=get_gelirvergisi1()
    damgaistisnasi1=get_damgavergisiodemesi1()
    for i in range(13):
        brut[i]=("{:.2f}".format(brut[i]))
        sgkmatrah[i]=("{:.2f}".format(sgkmatrah[i]))
        sgkkesintisi[i]=("{:.2f}".format(sgkkesintisi[i]))
        issizlikkesintisi[i]=("{:.2f}".format(issizlikkesintisi[i]))
        vergimatrah[i]=("{:.2f}".format(vergimatrah[i]))
        kumulatif1[i]=("{:.2f}".format(kumulatif1[i]))
        istisnaoncesi1[i]=("{:.2f}".format(istisnaoncesi1[i]))
        asgarivergimatrah1[i]=("{:.2f}".format(asgarivergimatrah1[i]))
        kumulatifasgari1[i]=("{:.2f}".format(kumulatifasgari1[i]))
        asgarigelirvergisiistisnasi1[i]=("{:.2f}".format(asgarigelirvergisiistisnasi1[i]))
        damgavergisi1[i]=("{:.2f}".format(damgavergisi1[i]))
        gelirvergisi1[i]=("{:.2f}".format(gelirvergisi1[i]))
        netucret1[i]=("{:.2f}".format(netucret1[i]))
        sgkisveren1[i]=("{:.2f}".format(sgkisveren1[i]))
        issizlikkesintisiisveren1[i]=("{:.2f}".format(issizlikkesintisiisveren1[i]))
        toplamsgk1[i]=("{:.2f}".format(toplamsgk1[i]))
        toplam1[i]=("{:.2f}".format(toplam1[i]))
        sgkistisnasi[i]=("{:.2f}".format(sgkistisnasi[i]))
        odeneceksgk[i]=("{:.2f}".format(odeneceksgk[i]))
        odenecekgelirvergisi[i]=("{:.2f}".format(odenecekgelirvergisi[i]))
        odenecekdamgavergisi[i]=("{:.2f}".format(odenecekdamgavergisi[i]))
        gelirödeme[i]=("{:.2f}".format(gelirödeme[i]))
        damga[i]=("{:.2f}".format(damga[i]))
        damgaistisnasi[i]=("{:.2f}".format(damgaistisnasi[i]))
        geliristisnasi[i]=("{:.2f}".format(geliristisnasi[i]))
        damgaistisnasi1[i]=("{:.2f}".format(damgaistisnasi1[i]))
    temp=0
    temp1=0
    temp2=0
    for i in range(12):
        temp=temp+float(gunsayisi1[i])
        temp1=float(gosterilenbrut[i])+temp1
        temp2=float(argegun[i])+temp2
    gunsayisi1.append(temp)
    gosterilenbrut.append(temp1)
    argegun.append(temp2)


    maaslar=zip(aylar,brut,gunsayisi1,sgkmatrah,sgkkesintisi,issizlikkesintisi,vergimatrah,kumulatif1,istisnaoncesi1,asgarivergimatrah1,kumulatifasgari1,asgarigelirvergisiistisnasi1,damgavergisi1,gelirvergisi1,netucret1,sgkisveren1,issizlikkesintisiisveren1,toplamsgk1,toplam1,gosterilenbrut,sgkistisnasi,odeneceksgk,odenecekgelirvergisi,odenecekdamgavergisi,gelirödeme,geliroran,damga,damgaistisnasi,geliristisnasi,damgaistisnasi1,argegun)
 
    
    

    return maaslar

def get_nettenbrute1(nettenbrut1,gunsayisi1):
    
    enteredamount=0
    nettenbrut=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    for i in range(12):
        enteredamount= float(nettenbrut1[i])*(float(gunsayisi1[i])/30)
        left = enteredamount/30
        right = 30* enteredamount
        middle= (left+right)/2
        nettenbrut[i]=middle
        brutucret1.clear()
        k=0
        while abs(left-right)>0.0001 and k<100:
            brutucret1.clear()
            for j in range(12):
            
                brutucret1.append(float(nettenbrut[j]))
                       
            if float(get_netucret1(nettenbrut,gunsayisi1)[i])>enteredamount:
                right=middle
                
            else:
                left=middle
            middle=(left+right)/2

            nettenbrut[i]=middle
            k=k+1


        nettenbrut[i]=((middle))

        brutucret1.clear()
        gosterilenbrut.clear()
        for j in range(12):
            
            brutucret1.append(float(nettenbrut[j]))
            gosterilenbrut.append("{:.2f}".format(float(nettenbrut[j])))
  
    return nettenbrut
    

def get_maliyettenbrute(nettenbrut1,gunsayisi1):
    enteredamount=0
    nettenbrut=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(12):
        enteredamount= float(nettenbrut1[i])
        left = 0
        right = 2* enteredamount
        middle= (left+right)/2
        nettenbrut[i]=middle
        brutucret1.clear()
        calculatednet=[0,0,0,0,0,0,0,0,0,0,0,0]
        k=0
        while abs(float(calculatednet[i])-float(enteredamount))>0.0001 and k<100:
            brutucret1.clear()
            for j in range(12):
            
                brutucret1.append(float(nettenbrut[j]))
           
            calculatednet[i]=get_toplammaliyet1(nettenbrut,gunsayisi1)[i]
           
            if float(calculatednet[i])>enteredamount:
                right=middle
                
            else:
                left=middle
            middle=(left+right)/2
            nettenbrut[i]=middle
            k=k+1
          
        nettenbrut[i]=((middle))
        brutucret1.clear()
        gosterilenbrut.clear()
        for j in range(12):
            brutucret1.append(float(nettenbrut[j]))
            gosterilenbrut.append("{:.2f}".format(float(nettenbrut[j])))
    return nettenbrut

def get_bordroyaesasbrut1(brutucret1,gunsayisi1):
    bbrutucret=[]
    
    for i in range(12):
        bbrutucret.append((float(brutucret1[i])/30*float(gunsayisi1[i])))
    temp=0
    for i in range(12):
        temp=temp+float(bbrutucret[i])
    bbrutucret.append(temp)

    return bbrutucret

def get_vergimatrahi1(brutucret1,gunsayisi1):
    vvergimatrahi=[]
    bordroyaesasbrut = get_bordroyaesasbrut1(brutucret1,gunsayisi1)
    sgkkesintisi = get_sgkkesintisi1(brutucret1,gunsayisi1)
    issizlikkesintisi = get_issizlikkesintisi1(brutucret1,gunsayisi1)
    
    for i in range(12):
        if engelli[0]=="pick0":
            vvergimatrahi.append((float(bordroyaesasbrut[i])-float(sgkkesintisi[i])-float(issizlikkesintisi[i])))
        elif engelli[0]=="pick1":
            vvergimatrahi.append((float(bordroyaesasbrut[i])-float(sgkkesintisi[i])-float(issizlikkesintisi[i])-float(birinciderece)))
        elif engelli[0]=="pick2":
            vvergimatrahi.append((float(bordroyaesasbrut[i])-float(sgkkesintisi[i])-float(issizlikkesintisi[i])-float(ikinciderece)))
        elif engelli[0]=="pick3":
            vvergimatrahi.append((float(bordroyaesasbrut[i])-float(sgkkesintisi[i])-float(issizlikkesintisi[i])-float(ucuncuderece)))
    temp=0
    for i in range(12):
        temp=temp+float(vvergimatrahi[i])
    vvergimatrahi.append(temp)

    return vvergimatrahi

def get_kumulatifvergimatrahi1(brutucret1,gunsayisi1):
    kumulatif=[]
    vergimatrahi=get_vergimatrahi1(brutucret1,gunsayisi1)
    

    for i in range(12):
        if i==0:
                kumulatif.append((float(vergimatrahi[i])))
        else:
                kumulatif.append((float(kumulatif[i-1])+float(vergimatrahi[i])))
    temp=0
    for i in range(12):
        temp=temp+float(kumulatif[i])
    kumulatif.append(temp)

    return kumulatif

def get_istisnaoncesigelirvergisi1(brutucret1,gunsayisi1):
    kumulatif=get_kumulatifvergimatrahi1(brutucret1,gunsayisi1)
  
    istisnaoncesi=[]
    for i in range(12):
        if i==0:
            istisnaoncesi.append((float((max(((float(kumulatif[i])-float(otuzbesvergidilimi[0]))*5/100),0)+max((float(kumulatif[i])-float(yirmiyedivergidilimi[0]))*8/100,0)+max((float(kumulatif[i])-float(yirmivergidilimi[0]))*7/100,0)+max((float(kumulatif[i])-float(onbesvergidilimi[0]))*5/100,0)+(float(kumulatif[i])*15/100))+max((0-float(yirmivergidilimi[0]))*7/100,0)+max((0-float(onbesvergidilimi[0]))*5/100,0))))
        else:
            istisnaoncesi.append((float(max(((float(kumulatif[i])-float(otuzbesvergidilimi[0]))*5/100),0)+max((float(kumulatif[i])-float(yirmiyedivergidilimi[0]))*8/100,0)+max((float(kumulatif[i])-float(yirmivergidilimi[0]))*7/100,0)+max((float(kumulatif[i])-float(onbesvergidilimi[0]))*5/100,0)+(float(kumulatif[i]*15/100)))-(max((kumulatif[i-1]-float(otuzbesvergidilimi[0]))*5/100,0)+max((kumulatif[i-1]-float(yirmiyedivergidilimi[0]))*8/100,0)+max((float(kumulatif[i-1])-float(yirmivergidilimi[0]))*7/100,0)+max((float(kumulatif[i-1])-float(onbesvergidilimi[0]))*5/100,0)+(float(kumulatif[i-1])*15/100))))
    

    temp=0
    for i in range(12):
        temp=temp+float(istisnaoncesi[i])
    istisnaoncesi.append(temp)
    return istisnaoncesi


def get_asgariucretvergimatrahi1(brutucret1,gunsayisi1):
    asgarivergimatrah=[]
    vergimatrah=get_vergimatrahi1(brutucret1,gunsayisi1)
    for i in range(12):
        
        
            asgarivergimatrah.append(float((aylikasgari[i]*float(asgarimatrahorani[0]))))
    temp=0
    for i in range(12):
        temp=temp+float(asgarivergimatrah[i])
    asgarivergimatrah.append(temp)
        
    return asgarivergimatrah

def get_kumulatifasgariucret1(brutucret1,gunsayisi1):
    kumulatifasgari=[]
    asgarivergimatrahi=get_asgariucretvergimatrahi1(brutucret1,gunsayisi1)
    for i in range(12):
        if i==0:
            kumulatifasgari.append((float(asgarivergimatrahi[i])))
        else:
            kumulatifasgari.append((float(float(kumulatifasgari[i-1])+float(asgarivergimatrahi[i]))))
    temp=0
    for i in range(12):
        temp=temp+float(kumulatifasgari[i])
    kumulatifasgari.append(temp)

    return kumulatifasgari


#değişecek fonksiyon!!!!
def get_asgarigelirvergisiistisnasi1(brutucret1,gunsayisi1):
    kumulatifasgari=get_kumulatifasgariucret1(brutucret1,gunsayisi1)
    asgarigelirvergisiistisnasi=[]
    istisnaoncesi=get_istisnaoncesigelirvergisi1(brutucret1,gunsayisi1)

    for i in range(12):
        
        if i==0:
                temp=((max(((float(kumulatifasgari[i])-float(otuzbesvergidilimi[0]))*5/100),0)+max((float(kumulatifasgari[i])-float(yirmiyedivergidilimi[0]))*8/100,0)+max((float(kumulatifasgari[i])-float(yirmivergidilimi[0]))*7/100,0)+max((float(kumulatifasgari[i])-float(onbesvergidilimi[0]))*5/100,0)+(float(kumulatifasgari[i])*15/100))-(max((0-float(otuzbesvergidilimi[0]))*5/100,0)+max((0-float(yirmiyedivergidilimi[0]))*8/100,0)+max((0-float(yirmivergidilimi[0]))*7/100,0)+max((0-float(onbesvergidilimi[0]))*5/100,0)))
                asgarigelirvergisiistisnasi.append(min(temp,istisnaoncesi[i]))
        else:
                temp=((max(((float(kumulatifasgari[i])-float(otuzbesvergidilimi[0]))*5/100),0)+max((float(kumulatifasgari[i])-float(yirmiyedivergidilimi[0]))*8/100,0)+max((float(kumulatifasgari[i])-float(yirmivergidilimi[0]))*7/100,0)+max((float(kumulatifasgari[i])-float(onbesvergidilimi[0]))*5/100,0)+(float(kumulatifasgari[i])*15/100))-(max((float(kumulatifasgari[i-1])-float(otuzbesvergidilimi[0]))*5/100,0)+max((float(kumulatifasgari[i-1])-float(yirmiyedivergidilimi[0]))*8/100,0)+max((float(kumulatifasgari[i-1])-float(yirmivergidilimi[0]))*7/100,0)+max((float(kumulatifasgari[i-1])-float(onbesvergidilimi[0]))*5/100,0)+(float(kumulatifasgari[i-1])*15/100)))
                asgarigelirvergisiistisnasi.append(min(temp,istisnaoncesi[i]))
    temp=0
    for i in range(12):
        temp=temp+float(asgarigelirvergisiistisnasi[i])
    asgarigelirvergisiistisnasi.append(temp)
      

    return asgarigelirvergisiistisnasi


def get_damgavergisi1(brutucret1,gunsayisi1):
    damgavergisi=[]
    brutucret=get_bordroyaesasbrut1(brutucret1,gunsayisi1)
    for i in range(12):
    
        if aylikasgari[i]>float(brutucret[i]):
            damgavergisi.append(float((0)))
        else:
            damgavergisi.append(((float(brutucret[i])-aylikasgari[i])*float(damgavergiorani[0])))
    temp=0
    for i in range(12):
        temp=temp+float(damgavergisi[i])
    damgavergisi.append(temp)
        
    return damgavergisi
    
def get_gelirvergisiodemesi1(brutucret1,gunsayisi1):
    gelirvergisiodemesi=[]
    brutucret=get_bordroyaesasbrut1(brutucret1,gunsayisi1)
    asgarivergimatrahi=get_asgariucretvergimatrahi1(brutucret1,gunsayisi1)
    istisnaoncesi=get_istisnaoncesigelirvergisi1(brutucret1,gunsayisi1)
    asgarigelirvergisi=get_asgarigelirvergisiistisnasi1(brutucret1,gunsayisi1)
    for i in range(12):
        if float(brutucret[i])<float(asgarivergimatrahi[i]):
            gelirvergisiodemesi.append(float((0)))
        else:
            gelirvergisiodemesi.append(abs(float((float(istisnaoncesi[i])-float(asgarigelirvergisi[i])))))
    temp=0
    for i in range(12):
        temp=temp+float(gelirvergisiodemesi[i])
    gelirvergisiodemesi.append(temp)
    
    return gelirvergisiodemesi


def get_netucret1(brutucret1,gunsayisi1):
    netucret=[]
    brutucret=get_bordroyaesasbrut1(brutucret1,gunsayisi1)
    damgavergisi=get_damgavergisi1(brutucret1,gunsayisi1)
    gelirvergisiodemesi=get_gelirvergisiodemesi1(brutucret1,gunsayisi1)
    issizlikkesintisi= get_issizlikkesintisi1(brutucret1,gunsayisi1)
    sgkkesintisi= get_sgkkesintisi1(brutucret1,gunsayisi1)
    damgavergisi1=get_damgavergisiodemesi()
    gelirvergisiodemesi1=get_gelirvergisi()
    gelir=get_istisnaoncesigelirvergisi1(brutucret1,gunsayisi1)
    temp=engelli[0]
    engelli[0]="pick0"
    gelirvergisiodemesi2=get_gelirvergisi()
    gelirindirimi=[]
    engelli[0]=temp      

    for i in range(12):
       
        netucret.append(float((float(brutucret[i])-float(damgavergisi1[i])-float(gelirvergisiodemesi[i])- float(issizlikkesintisi[i])- float(sgkkesintisi[i]))))
    temp=0
    for i in range(12):
        temp=temp+float(netucret[i])
    netucret.append(temp)
    return netucret

def get_damgavergisiodemesi():
    damgavergisiodemesi=[]
    damgavergisi=get_damgavergisi1(brutucret1,gunsayisi1)
    if calisanturu[0]=='pick1':
        for i in range(12):
            damgavergisiodemesi.append(float(damgavergisi[i]))
    elif calisanturu[0]=='pick2':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(0))
            else:
                damgavergisiodemesi.append((float(damgavergisi[i])-float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i])))
    elif calisanturu[0]=='pick3':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(0))
            else:
                damgavergisiodemesi.append((float(damgavergisi[i])-float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i]))) 
    elif calisanturu[0]=='pick4':
        for i in range(12):
            damgavergisiodemesi.append(float(damgavergisi[i]))
    elif calisanturu[0]=='pick5':
        for i in range(12):
            damgavergisiodemesi.append(float(damgavergisi[i]))
    elif calisanturu[0]=='pick6':
        for i in range(12):
            damgavergisiodemesi.append(float(damgavergisi[i]))
    elif calisanturu[0]=='pick7':
        for i in range(12):
            damgavergisiodemesi.append(float(damgavergisi[i]))
    elif calisanturu[0]=='pick8':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(0))
            else:
                damgavergisiodemesi.append((float(damgavergisi[i])-float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i])))
    elif calisanturu[0]=='pick9':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(0))
            else:
                damgavergisiodemesi.append((float(damgavergisi[i])-float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i])))

    
    temp=0
    for i in range(12):
        temp=temp+float(damgavergisiodemesi[i])
    damgavergisiodemesi.append(temp)
    return damgavergisiodemesi
def get_damgavergisiodemesi1():
    damgavergisiodemesi=[]
    damgavergisi=get_damgavergisi1(brutucret1,gunsayisi1)

    if calisanturu[0]=='pick1':
        for i in range(12):
            damgavergisiodemesi.append(float(0))
    elif calisanturu[0]=='pick2':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(damgavergisi[i]))
            else:
                
                if float(argegun[i])==0:
                    
                    
                    damgavergisiodemesi.append((float(0)))
                else:
                    
                    damgavergisiodemesi.append((float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i])))
    elif calisanturu[0]=='pick3':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(damgavergisi[i]))
                
            else:

                if float(argegun[i])==0:
                    
                    damgavergisiodemesi.append((float(0)))
                else:
                    
                    damgavergisiodemesi.append((float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i]))) 
    elif calisanturu[0]=='pick4':
        for i in range(12):
            damgavergisiodemesi.append(float(0))
    elif calisanturu[0]=='pick5':
        for i in range(12):
            damgavergisiodemesi.append(float(0))
    elif calisanturu[0]=='pick6':
        for i in range(12):
            damgavergisiodemesi.append(float(0))
    elif calisanturu[0]=='pick7':
        for i in range(12):
            damgavergisiodemesi.append(float(0))
    elif calisanturu[0]=='pick8':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(damgavergisi[i]))
            else:
                if argegun[i]==0:
                    damgavergisiodemesi.append((float(0)))
                else:
                    damgavergisiodemesi.append((float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i])))
    elif calisanturu[0]=='pick9':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                damgavergisiodemesi.append(float(damgavergisi[i]))
            else:
                if argegun[i]==0:
                    damgavergisiodemesi.append((float(0)))
                else:
                    damgavergisiodemesi.append((float(damgavergisi[i])*float(argegun[i])/float(gunsayisi1[i])))

    
    temp=0
    for i in range(12):
        temp=temp+float(damgavergisiodemesi[i])
    damgavergisiodemesi.append(temp)
    return damgavergisiodemesi
def get_indirimsizdamgavergisi():
    indirimsizdamgavergisi=[]
    brut=get_bordroyaesasbrut1(brutucret1,gunsayisi1)
    for i in range(12):
        indirimsizdamgavergisi.append((float(brut[i])*float(damgavergiorani[0])))
    temp=0
    for i in range(12):
        temp=temp+float(indirimsizdamgavergisi[i])
    indirimsizdamgavergisi.append(temp)

    return indirimsizdamgavergisi
def get_damgaistisnasi():
    damgaistisnasi=[]
    damgavergisi=get_damgavergisi1(brutucret1,gunsayisi1)
    indirimsiz=get_indirimsizdamgavergisi()
    for i in range(12):
        damgaistisnasi.append((float(indirimsiz[i])-float(damgavergisi[i])))
    temp=0
    for i in range(12):
        temp=temp+float(damgaistisnasi[i])
    damgaistisnasi.append(temp)
    return damgaistisnasi


def get_toplammaliyet1(brutucret1,gunsayisi1):
    toplammaliyet=[]
    netucret = get_netucret1(brutucret1,gunsayisi1)
    sgk=get_odeneceksgk()
    gelirvergisi=get_gelirvergisi()
    damgavergisi1=get_damgavergisiodemesi()

    for i in range(12):
        toplammaliyet.append((float(netucret[i])+float(sgk[i])+float(gelirvergisi[i])+float(damgavergisi1[i])))
    temp=0
    for i in range(12):
        temp=temp+float(toplammaliyet[i])
    toplammaliyet.append(temp)
    return toplammaliyet

def get_sgkmatrahi1(brutucret1,gunsayisi1):
    ssgkmatrahi=[]
    for i in range(12):
        
            ssgkmatrahi.append((min(float(brutucret1[i]),(aylikasgari[i]*float(asgaritavanorani[0])))/30*float(gunsayisi1[i])))
    temp=0
    for i in range(12):
        temp=temp+float(ssgkmatrahi[i])
    ssgkmatrahi.append(temp)
       

    return ssgkmatrahi

def get_sgkkesintisi1(brutucret1,gunsayisi1):
    ssgkkesintisi=[]
    sgkmatrah= get_sgkmatrahi1(brutucret1,gunsayisi1)
    for i in range(12):
        if calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9':
            ssgkkesintisi.append((0))
        else:
            if emeklicalisan[0]==False:
                ssgkkesintisi.append((float(sgkmatrah[i])*float(sgkkesintiorani1[0])))
            else:
                ssgkkesintisi.append((float(sgkmatrah[i])*float(emeklisgkorani[0])))#netten brütede asgariyle karşılaştır
        
    temp=0
    for i in range(12):
        temp=temp+float(ssgkkesintisi[i])
    ssgkkesintisi.append(temp)
    return ssgkkesintisi


def get_issizlikkesintisi1(brutucret1,gunsayisi1):
    iissizlikkesintisi=[]
    ssgkmatrah=get_sgkmatrahi1(brutucret1,gunsayisi1)
    if calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9' or emeklicalisan[0]==True:
        for i in range(12):
            iissizlikkesintisi.append((0))
    else:
        for i in range(12):
            iissizlikkesintisi.append((float(ssgkmatrah[i])*float(issizlikkesintiorani[0])))
    temp=0
    for i in range(12):
        temp=temp+float(iissizlikkesintisi[i])
    iissizlikkesintisi.append(temp)
    return iissizlikkesintisi

def get_sgkistisnasi(brutucret1,gunsayisi1):
    sgkistisnasi=[]
    sgk=get_sgkmatrahi1(brutucret1,gunsayisi1)
    sgkisveren=get_sgkisveren1(brutucret1,gunsayisi1)
    toplamsgk=get_toplamsgkkesintisi1(brutucret1,gunsayisi1)
    if emeklicalisan[0]==True:

        for i in range(12):
            sgkistisnasi.append((0))
    elif calisanturu[0]=='pick1':
        for i in range(12):
            
            if indirimm[0]==False:
                sgkistisnasi.append(0)
            else:
                sgkistisnasi.append(float(sgk[i])*0.05)
                print(sgkistisnasi[i])

    elif calisanturu[0]=='pick2':
        for i in range(12):

            if indirimm[0]==False:
                #sgkistisnasi.append((float(sgk[i])*float(sgkkesintiorani[0])*0.5*float(argegun[i])/float(gunsayisi1[i])))eski fonksiyon
                sgkistisnasi.append(float(0))
            else:
                #sgkistisnasi.append((float(sgk[i])*0.5*(float(sgkkesintiorani[0])-float(indirimorani5510[0]))*float(argegun[i])/float(gunsayisi1[i])))eski fonksiyon
                sgkistisnasi.append((float(sgk[i])*0.05)+((float(sgk[i])*0.0775)*(float(argegun[i])/float(gunsayisi1[i]))))
    elif calisanturu[0]=='pick3':
        for i in range(12):
            if indirimm[0]==False:
                #sgkistisnasi.append((float(sgk[i])*float(sgkkesintiorani[0])*0.5*float(argegun[i])/float(gunsayisi1[i])))
                sgkistisnasi.append(float(0))
            else:
                #sgkistisnasi.append((float(sgk[i])*0.5*(float(sgkkesintiorani[0])-float(indirimorani5510[0]))*float(argegun[i])/float(gunsayisi1[i])))
                sgkistisnasi.append((float(sgk[i])*0.05)+((float(sgk[i])*0.0775)*float(argegun[i])/float(gunsayisi1[i])))

    elif calisanturu[0]=='pick4':
        for i in range(12):
            sgkistisnasi.append((float(sgkisveren[i])))
    elif calisanturu[0]=='pick5':
        for i in range(12):
            #sgkistisnasi.append((float(aylikasgari[i]*0.375)))
            istisna=float(float(aylikasgari[i])*float(gunsayisi1[i])/30)*0.375
            istisna=min(istisna,toplamsgk[i])
            sgkistisnasi.append(istisna)
           
    elif calisanturu[0]=='pick6':
        for i in range(12):
             #istisna=float(brutucret1[i])*0.375
             istisna=float(float(aylikasgari[i])/0.375*float(gunsayisi1[i])/30)*0.375
             istisna=min(istisna,toplamsgk[i])
             sgkistisnasi.append(istisna)
            #  if istisna<aylikasgari[i]:
            #      sgkistisnasi.append(float(istisna)*gunsayisi1[i]/30)
            #  else:
            #      sgkistisnasi.append(sgk[i])
            #sgkistisnasi.append((float(aylikasgari[i]/30*float(gunsayisi1[i]))))
           
    elif  calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9':
        for i in range(12):
            sgkistisnasi.append((0))

            

    temp=0
    for i in range(12):
        temp=temp+float(sgkistisnasi[i])
    sgkistisnasi.append(temp)
    return sgkistisnasi

def get_gelirvergideneme():

    gelirvergideneme=[]
    kumulatif=get_kumulatifvergimatrahi1(brutucret1,gunsayisi1)
    oncekiaylar=0
    brut=0

    if calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9':
        for i in range(12):
            oncekiaylar=0
            brut+=float(brutucret1[i])
            if brut<=0:
                gelirvergideneme.append(0)

            elif brut>0 and brut<float(gelirvergioran1[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])

                gelirvergideneme.append(((float(brut)*0.15)-oncekiaylar))
            elif brut>=float(gelirvergioran1[0]) and brut<float(gelirvergioran2[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((4800+(float(brut)-float(gelirvergioran1[0]))*0.20)-oncekiaylar))
            elif brut>=float(gelirvergioran2[0]) and brut<float(gelirvergioran3[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((12400+(float(brut)-float(gelirvergioran2[0]))*0.27)-oncekiaylar))
            elif brut>=float(gelirvergioran3[0]) and brut<float(gelirvergioran4[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((39400+(float(brut)-float(gelirvergioran3[0]))*0.35)-oncekiaylar))
            elif brut>=float(gelirvergioran4[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((287900+(float(brut)-float(gelirvergioran4[0]))*0.40)-oncekiaylar))
            else:

                gelirvergideneme.append((0))

    else:
        for i in range(12):
            oncekiaylar=0
            if kumulatif[i]<=0:
                gelirvergideneme.append(0)

            elif kumulatif[i]>0 and kumulatif[i]<float(gelirvergioran1[0]):
                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
               
                gelirvergideneme.append(((float(kumulatif[i])*0.15)-oncekiaylar))
            elif kumulatif[i]>=float(gelirvergioran1[0]) and kumulatif[i]<float(gelirvergioran2[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])

                
                gelirvergideneme.append(((4800+(float(kumulatif[i])-float(gelirvergioran1[0]))*0.20)-oncekiaylar))
            elif kumulatif[i]>=float(gelirvergioran2[0]) and kumulatif[i]<float(gelirvergioran3[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((12400+(float(kumulatif[i])-float(gelirvergioran2[0]))*0.27)-oncekiaylar))
            elif kumulatif[i]>=float(gelirvergioran3[0]) and kumulatif[i]<float(gelirvergioran4[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((39400+(float(kumulatif[i])-float(gelirvergioran3[0]))*0.35)-oncekiaylar))
            elif kumulatif[i]>=float(gelirvergioran4[0]):

                for j in range(i):
                    oncekiaylar+=float(gelirvergideneme[j])
                gelirvergideneme.append(((287900+(float(kumulatif[i])-float(gelirvergioran4[0]))*0.40)-oncekiaylar))
            else:

                gelirvergideneme.append((0))

    temp=0
    for i in range(12):
        temp+=float(gelirvergideneme[i])
    gelirvergideneme.append(temp)
    return gelirvergideneme


def get_gelirvergidenemeoran():

    gelirvergideneme1=[]
    kumulatif=get_kumulatifvergimatrahi1(brutucret1,gunsayisi1)
    j=0
    k=0
    t=0
    y=0
    x=0

    for i in range(12):
        if kumulatif[i]<=0:
            gelirvergideneme1.append("%0")
            
        elif kumulatif[i]>0 and kumulatif[i]<gelirvergioran1[0]:
            gelirvergideneme1.append("%15")
            
        elif kumulatif[i]>=gelirvergioran1[0] and kumulatif[i]<gelirvergioran2[0]:
            if j ==0:
                gelirvergideneme1.append("%15-20")
                j+=1
            else:
                gelirvergideneme1.append("%20")
           
        elif kumulatif[i]>=gelirvergioran2[0] and kumulatif[i]<gelirvergioran3[0]:
            if k ==0:
                if j==0:
                    gelirvergideneme1.append("%15-20-27")
                    k+=1
                else:
                    gelirvergideneme1.append("%20-27")
                    k+=1
            else:
                gelirvergideneme1.append("%27")
            
        elif kumulatif[i]>=gelirvergioran3[0] and kumulatif[i]<gelirvergioran4[0]:
            if t ==0:
                if k==0:
                    if j==0:
                        gelirvergideneme1.append("%15-20-27-35")
                        t+=1
                    else:
                        gelirvergideneme1.append("%20-27-35")
                        t+=1
                else:
                    gelirvergideneme1.append("%27-35")
                    t+=1
            else:
                gelirvergideneme1.append("%35")

            
        elif kumulatif[i]>=gelirvergioran4[0]:
            if y ==0:
                if t==0:
                    if k==0:
                        if j==0:
                            gelirvergideneme1.append("%15-20-27-35-40")
                            y+=1
                        else:
                            gelirvergideneme1.append("%20-27-35-40")
                            y+=1
                    else:
                        gelirvergideneme1.append("%27-35-40")
                        y+=1
                else:
                    gelirvergideneme1.append("%35-40")
                    y+=1
            else:
                gelirvergideneme1.append("%40")
            
          

    gelirvergideneme1.append(" ")
    return gelirvergideneme1


def get_sgkisveren1(brutucret1,gunsayisi1):
    sgkisveren=[]
    matrah=get_sgkmatrahi1(brutucret1,gunsayisi1)
    if calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9':
        for i in range(12):
            sgkisveren.append((0))
    else:
        for i in range(12):
            if emeklicalisan[0]==False:
                    
                sgkisveren.append((float(matrah[i])*float(sgkkesintiorani[0])))
            else:
                sgkisveren.append((float(matrah[i])*0.225))
    temp=0
    for i in range(12):
        temp+=float(sgkisveren[i])
    sgkisveren.append(temp)
        
    return sgkisveren

def get_issizlikkesintisiisveren1(brutucret1,gunsayisi1):
    issizlikkesintisiisveren=[]
    matrah=get_sgkmatrahi1(brutucret1,gunsayisi1)
    if calisanturu[0]=='pick7' or calisanturu[0]=='pick8' or calisanturu[0]=='pick9' or emeklicalisan[0]==True:
        for i in range(12):
            issizlikkesintisiisveren.append((0))
    else:
        for i in range(12):
            issizlikkesintisiisveren.append((float(matrah[i])*float(issizlikisverenoran[0])))
    temp=0
    for i in range(12):
        temp+=float(issizlikkesintisiisveren[i])
    issizlikkesintisiisveren.append(temp)
    return issizlikkesintisiisveren

def get_toplamsgkkesintisi1(brutucret1,gunsayisi1):
    toplamsgkkesintisi=[]
    sgkisveren=get_sgkisveren1(brutucret1,gunsayisi1)
    issizlikkesintisiisveren=get_issizlikkesintisiisveren1(brutucret1,gunsayisi1)
    sgkisci=get_sgkkesintisi1(brutucret1,gunsayisi1)
    sgkissizlik=get_issizlikkesintisi1(brutucret1,gunsayisi1)
    for i in range(12):
        toplamsgkkesintisi.append((float(sgkisveren[i])+float(issizlikkesintisiisveren[i])+float(sgkisci[i])+float(sgkissizlik[i])))
    temp=0
    for i in range(12):
        temp+=float(toplamsgkkesintisi[i])
    toplamsgkkesintisi.append(temp)
    return toplamsgkkesintisi

def get_odeneceksgk():
    odeneceksgk=[]
    sgkistisna=get_sgkistisnasi(brutucret1,gunsayisi1)
    toplamsgk=get_toplamsgkkesintisi1(brutucret1,gunsayisi1)
    print(sgkistisna)
    print(toplamsgk)
    for i in range(12):
        odeneceksgk.append((float(toplamsgk[i])-float(sgkistisna[i])))
    temp=0
    for i in range(12):
        temp+=float(odeneceksgk[i])
    odeneceksgk.append(temp)
    return odeneceksgk

def get_gelirvergisi():
    gelirvergisiodemesi=[]
    gelirvergisi=get_gelirvergisiodemesi1(brutucret1,gunsayisi1)
    if calisanturu[0]=="pick1":
        for i in range(12):
            gelirvergisiodemesi.append((float(gelirvergisi[i])))
    if calisanturu[0]=='pick2':
        for i in range(12):
            if argegun[i]==gunsayisi1[i]:
                
                gelirvergisiodemesi.append((float(0)))
            else:
                gelirvergisiodemesi.append((float(gelirvergisi[i])-(float(gelirvergisi[i])*float(argegun[i])/float(gunsayisi1[i]))))

    if calisanturu[0]=="pick3":
        if egitimdurumu[0]=="pick1":
           for i in range(12):
               gelirvergisiodemesi.append((float(gelirvergisi[i]-float(gelirvergisi[i]*float(egitim1geliroran[0])*float(argegun[i])/float(gunsayisi1[i])))))

        elif egitimdurumu[0]=="pick2":
            for i in range(12):
                gelirvergisiodemesi.append((float(gelirvergisi[i]-float(gelirvergisi[i])*float(egitim2geliroran[0])*float(argegun[i])/float(gunsayisi1[i]))))

        elif egitimdurumu[0]=="pick3":
            for i in range(12):
                gelirvergisiodemesi.append((float(gelirvergisi[i]-float(gelirvergisi[i])*float(egitim3geliroran[0])*float(argegun[i])/float(gunsayisi1[i]))))
    if calisanturu[0]=="pick4":
        for i in range(12):
            gelirvergisiodemesi.append((float(gelirvergisi[i])))
    if calisanturu[0]=="pick5":
        for i in range(12):
            gelirvergisiodemesi.append((float(gelirvergisi[i])))
    if calisanturu[0]=="pick6":
        for i in range(12):
            gelirvergisiodemesi.append((float(gelirvergisi[i])))
    if calisanturu[0]=="pick7":
        for i in range(12):
            gelirvergisiodemesi.append((float(gelirvergisi[i])))
    if calisanturu[0]=="pick8":
        for i in range(12):
            if argegun[i]<gunsayisi1[i]:
                
                    gelirvergisiodemesi.append((float(gelirvergisi[i])-(float(gelirvergisi[i])*float(argegun[i])/float(gunsayisi1[i]))))
            else:
                
                    gelirvergisiodemesi.append((0))
    if calisanturu[0]=="pick9":
        if egitimdurumu[0]=="pick1":
           for i in range(12):
               gelirvergisiodemesi.append(((float(gelirvergisi[i]-float(gelirvergisi[i]*float(egitim1geliroran[0])*float(argegun[i])/float(gunsayisi1[i]))))))

        elif egitimdurumu[0]=="pick2":
            for i in range(12):
                gelirvergisiodemesi.append(((float(gelirvergisi[i])-float(gelirvergisi[i])*float(egitim2geliroran[0]))*float(argegun[i])/float(gunsayisi1[i])))

        elif egitimdurumu[0]=="pick3":
            for i in range(12):
                gelirvergisiodemesi.append(((float(gelirvergisi[i]-float(gelirvergisi[i])*float(egitim3geliroran[0])*float(argegun[i])/float(gunsayisi1[i])))))

    temp=0
    for i in range(12):
        temp+=float(gelirvergisiodemesi[i])
    gelirvergisiodemesi.append(temp)
    return gelirvergisiodemesi

def get_gelirvergisi1():
    gelirvergisiodemesi=[]
    gelirvergisi=get_gelirvergisiodemesi1(brutucret1,gunsayisi1)

    if calisanturu[0]=="pick1":
        for i in range(12):
            gelirvergisiodemesi.append((float(0)))
    if calisanturu[0]=='pick2':
        for i in range(12):
            
            if float(argegun[i])==float(gunsayisi1[i]):
                
                
                gelirvergisiodemesi.append((float(gelirvergisi[i])))
               
            else:
                gelirvergisiodemesi.append(((float(gelirvergisi[i])*float(argegun[i])/float(gunsayisi1[i]))))
                
                

    if calisanturu[0]=="pick3":
        if egitimdurumu[0]=="pick1":
           for i in range(12):
               if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
               else:
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])*float(argegun[i])/float(gunsayisi1[i])))

        elif egitimdurumu[0]=="pick2":
            for i in range(12):
                if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
                else:
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim2geliroran[0])*float(argegun[i])/float(gunsayisi1[i])))

        elif egitimdurumu[0]=="pick3":
            for i in range(12):
                if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
                else:
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim3geliroran[0])*float(argegun[i])/float(gunsayisi1[i])))
    if calisanturu[0]=="pick4":
        for i in range(12):
            gelirvergisiodemesi.append((float(0)))
    if calisanturu[0]=="pick5":
        for i in range(12):
            gelirvergisiodemesi.append((float(0)))
    if calisanturu[0]=="pick6":
        for i in range(12):
            gelirvergisiodemesi.append((float(0)))
    if calisanturu[0]=="pick7":
        for i in range(12):
            gelirvergisiodemesi.append((float(0)))
    if calisanturu[0]=="pick8":
        for i in range(12):
            if argegun[i]<gunsayisi1[i]:
                if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
                else:
                
                    gelirvergisiodemesi.append(((float(gelirvergisi[i])*float(argegun[i])/float(gunsayisi1[i]))))
            else:
                
                    gelirvergisiodemesi.append((gelirvergisi[i]))
    if calisanturu[0]=="pick9":
        if egitimdurumu[0]=="pick1":
           for i in range(12):
               if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
               else:
                     gelirvergisiodemesi.append(((float(gelirvergisi[i]*float(egitim1geliroran[0])*float(argegun[i])/float(gunsayisi1[i])))))

        elif egitimdurumu[0]=="pick2":
            for i in range(12):
                if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
                else:
                     gelirvergisiodemesi.append(((float(gelirvergisi[i])*float(egitim2geliroran[0]))*float(argegun[i])/float(gunsayisi1[i])))

        elif egitimdurumu[0]=="pick3":
            for i in range(12):
                if float(argegun[i])==0 :
                     gelirvergisiodemesi.append((float(gelirvergisi[i])*float(egitim1geliroran[0])/float(gunsayisi1[i])))
                else:
                     gelirvergisiodemesi.append(((float(gelirvergisi[i])*float(egitim3geliroran[0])*float(argegun[i])/float(gunsayisi1[i]))))
                    
    temp=0
    for i in range(12):
        temp=temp+float(gelirvergisiodemesi[i])
    gelirvergisiodemesi.append(temp)

    return gelirvergisiodemesi
def get_iscitoplamsgk():
    iscitoplamsgk=[]
    isci=get_sgkkesintisi1(brutucret1,gunsayisi1)
    issizlik=get_issizlikkesintisi1(brutucret1,gunsayisi1)
    for i in range(12):
        iscitoplamsgk.append((float(isci[i])+float(issizlik[i])))
    temp=0
    for i in range(12):
        temp=temp+float(iscitoplamsgk[i])
    iscitoplamsgk.append(temp)
    return iscitoplamsgk

