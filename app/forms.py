from email.policy import default
from django import forms
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from .models import hesaplama

hesaplamatur = [
    ('pick1','Brütten Nete'),
     ('pick2','Netten Brüte'),
     ('pick3','Maliyetten Brüte'),]
calisantur = [
    ('pick1','Standart Çalışan'),
    ('pick2','Teknokent Personeli (4691)'),
    ('pick3','AR-GE Personeli (5746)'),
    ('pick4','6111 Sayılı Kanun'),
    ('pick5','27103 Sayılı Kanun'),
    ('pick6','17103 Sayılı Kanun'),
    ('pick7','İşveren'),
    ('pick8','İşveren Teknokent Personeli'),
    ('pick9','İşveren AR-GE Personeli'),
       ]
egitimdurum=[
    ('pick1','Diğer AR-GE Personeli'),
    ('pick2','Doktoralı veya Temel Bilimler Yüksek Lisanslı'),
    ('pick3','Yüksek Lisanslı veya Temel Bilimler Lisanslı'),
]

engelliderecesi=[
    ('pick0','Engelli Değil'),
    ('pick1','1. Derece'),
    ('pick2','2. Derece'),
    ('pick3','3. Derece'),
]
parabirimi=[
    ('pick0','TL'),
    ('pick1','USD'),
    ('pick2','EUR'),
]

class monthsanddays(forms.Form):
    month1 = forms.CharField( max_length=100)
    day1 = forms.CharField(max_length=100, initial=30)
    month2 = forms.CharField( max_length=100)
    day2 = forms.CharField( max_length=100, initial=30)
    month3 = forms.CharField( max_length=100)
    day3 = forms.CharField(max_length=100, initial=30)
    month4 = forms.CharField( max_length=100)
    day4 = forms.CharField( max_length=100, initial=30)
    month5 = forms.CharField( max_length=100)
    day5 = forms.CharField( max_length=100, initial=30)
    month6 = forms.CharField( max_length=100)
    day6 = forms.CharField( max_length=100, initial=30)
    month7 = forms.CharField( max_length=100)
    day7 = forms.CharField( max_length=100, initial=30)
    month8 = forms.CharField( max_length=100)
    day8 = forms.CharField( max_length=100, initial=30)
    month9 = forms.CharField( max_length=100)
    day9 = forms.CharField( max_length=100, initial=30)
    month10 = forms.CharField( max_length=100)
    day10 = forms.CharField(max_length=100, initial=30)
    month11 = forms.CharField( max_length=100)
    day11 = forms.CharField( max_length=100, initial=30)
    month12 = forms.CharField( max_length=100)
    day12 = forms.CharField( max_length=100, initial=30)
    ellibesonindirimi= forms.BooleanField( required=False)
    emeklicalisan= forms.BooleanField( required=False)
    hesaplamaturu= forms.CharField( widget= forms.Select(choices=hesaplamatur))
    calisanturu= forms.CharField( widget= forms.Select(choices=calisantur))
    egitimdurumu=forms.CharField( widget= forms.Select(choices=egitimdurum))
    engelliderecesi=forms.CharField( widget= forms.Select(choices=engelliderecesi))
    argegun1 = forms.CharField( max_length=100, initial=30)
    argegun2 = forms.CharField( max_length=100, initial=30)
    argegun3 = forms.CharField( max_length=100, initial=30)
    argegun4 = forms.CharField( max_length=100, initial=30)
    argegun5 = forms.CharField( max_length=100, initial=30)
    argegun6 = forms.CharField( max_length=100, initial=30)
    argegun7 = forms.CharField( max_length=100, initial=30)
    argegun8 = forms.CharField( max_length=100, initial=30)
    argegun9 = forms.CharField( max_length=100, initial=30)
    argegun10 = forms.CharField( max_length=100, initial=30)
    argegun11 = forms.CharField( max_length=100, initial=30)
    argegun12 = forms.CharField( max_length=100, initial=30)
    hesaplamayili = forms.CharField( max_length=100, widget=forms.Select(choices=hesaplama.objects.all().values_list('hesaplama_yili', 'hesaplama_yili')))
    parabirimi=forms.CharField( widget= forms.Select(choices=parabirimi))
    def __init__(self, *args, **kwargs):
        super(monthsanddays, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
    
