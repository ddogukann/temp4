from dataclasses import field
from urllib import request
from django import forms
from .models import sirket,maas,calisan,mali_musavir,sube,mali_sirket,sube,iskur,sgkisyeri
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Kullanıcı Adı')
    password = forms.CharField(max_length=20, label='Parola', widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label='Parola Doğrula', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Parolalar uyuşmuyor!')

        values = {
            'username': username,
            'password': password
        }

        return values
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Kullanıcı Adı')
    password = forms.CharField(max_length=20, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username:
            raise forms.ValidationError('Kullanıcı adı boş bırakılamaz!')

        if not password:
            raise forms.ValidationError('Parola boş bırakılamaz!')

        values = {
            'username': username,
            'password': password
        }

        return values
class DateInput(forms.DateInput):
    input_type = 'date'

class SirketRegisterForm(forms.ModelForm):
    
    class Meta:
        model=sirket
        fields=['sirket_adi','sirket_kisa_unvan','sirket_adres','sirket_telefon','sirket_mail','sirket_website','sirket_nace_kodu','sirket_vergi_dairesi','sirket_vergi_numarasi','sirket_mersis_no','sirket_tc_no','sirket_tur','sirket_kurulus_tarihi',]
        widgets={
            'sirket_kurulus_tarihi':DateInput(),
        }
yetki=[
    ('pick0','Standart'),
    ('pick1','Muhasebe'),
    ('pick2','Mali Müşavir'),

]
engelliderecesi=[
    ('pick0','Engelli Değil'),
    ('pick1','1. Derece'),
    ('pick2','2. Derece'),
    ('pick3','3. Derece'),
]
class engelliform(forms.Form):
    engelli=forms.CharField(label='Engelli',widget=forms.Select(choices=engelliderecesi))
class yetkiform(forms.Form):
    yetki=forms.ChoiceField(choices=yetki,widget=forms.RadioSelect)

class calisanturform(forms.Form):
    tur=forms.CharField(max_length=50, label='Çalışan Türü', widget=forms.Select(choices=yetki))

from django_select2.forms import Select2MultipleWidget
bordroselect=[
    ('pick0','Brüt Ücret'),
    ('pick1','Çalışılan Gün'),
    ('pick2','Bordroya Esas Brüt Ücret'),
    ('pick3','Sgk Primleri'),
    ('pick4','Sgk İşsizlik Vergisi'),
    ('pick5','Damga Vergisi'),
    ('pick6','Gelir Vergisi'),
    ('pick7','Net Ücret'),
    
]
aylar=[
    ('maas_tutari1','Ocak'),
    ('maas_tutari2','Şubat'),
    ('maas_tutari3','Mart'),
    ('maas_tutari4','Nisan'),
    ('maas_tutari5','Mayıs'),
    ('maas_tutari6','Haziran'),
    ('maas_tutari7','Temmuz'),
    ('maas_tutari8','Ağustos'),
    ('maas_tutari9','Eylül'),
    ('maas_tutari10','Ekim'),
    ('maas_tutari11','Kasım'),
    ('maas_tutari12','Aralık'),
]
aylar1=[
    ('ocak','Ocak'),
    ('subat','Şubat'),
    ('mart','Mart'),
    ('nisan','Nisan'),
    ('mayis','Mayıs'),
    ('haziran','Haziran'),
    ('temmuz','Temmuz'),
    ('agustos','Ağustos'),
    ('eylul','Eylül'),
    ('ekim','Ekim'),
    ('kasim','Kasım'),
    ('aralik','Aralık'),
]
export=[
    ('pdf','PDF'),
    ('xls','Excel'),
]
class employeelistaylar(forms.Form):
    ay=forms.CharField(label='Aylar', widget= forms.Select(choices=aylar1))
class denemeform(forms.Form):
    aylar=forms.MultipleChoiceField(choices=aylar1,widget=Select2MultipleWidget)
    export=forms.CharField(label='Dışa Aktarma Türü',widget=forms.Select(choices=export))

    def __init__(self, *args, **kwargs):
        super(denemeform, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

class monthform(forms.Form):
    ay=forms.CharField(label='Aylar', widget= forms.Select(choices=aylar))

class updatebymonth(forms.Form):

    maas_tutari=forms.FloatField(label='Maaş Tutarı')


class CalisanRegisterForm(forms.ModelForm):
    
    class Meta:
        model=calisan
        fields=['calisan_adi','calisan_soyadi','calisan_tc','calisan_adres','calisan_telefon','calisan_mail','calisan_dogum_tarihi','calisan_ise_giris_tarihi','calisan_aktiflik','calisan_tesvik','calisan_indirim','calisan_emekli','calisan_photo',"calisan_gender"]
        widgets = {
            'calisan_dogum_tarihi': DateInput(),
            'calisan_ise_giris_tarihi': DateInput(),
        }
    def clean(self):
            form_data = self.cleaned_data
            print(type(form_data['calisan_tc']))
            if len(form_data['calisan_tc']) != 11 or not form_data['calisan_tc'].isdigit():
                self._errors["calisan_tc"] = ["Geçerli Bir TC Kimlik Numarası Gİriniz"] # Will raise a error message
                del form_data['calisan_tc']
            return form_data


class sgkisyeriregisterform(forms.ModelForm):
    class Meta:
        model=sgkisyeri
        fields=['sgk_isyeri_adi','sgk_isyeri_acilis_tarihi','sgk_isyeri_sicil_no','sgk_isyeri_sifre','sgk_isyeri_kodu','sgk_isyeri_adres_no','sgk_isyeri_mulk']
        widgets = {
            'sgk_isyeri_acilis_tarihi': DateInput(),

        }

class iskurregisterform(forms.ModelForm):
    class Meta:
        model=iskur
        fields=['iskur_no','iskur_sifre']

    
class MaasRegisterForm(forms.ModelForm):
    class Meta:
        model=maas
        fields=['maas_tutari1','gunsayisi1','argegun1','maas_tutari2','gunsayisi2','argegun2','maas_tutari3','gunsayisi3','argegun3','maas_tutari4','gunsayisi4','argegun4','maas_tutari5','gunsayisi5','argegun5','maas_tutari6','gunsayisi6','argegun6','maas_tutari7','gunsayisi7','argegun7','maas_tutari8','gunsayisi8','argegun8','maas_tutari9','gunsayisi9','argegun9','maas_tutari10','gunsayisi10','argegun10','maas_tutari11','gunsayisi11','argegun11','maas_tutari12','gunsayisi12','argegun12','para_birimi','ucrettipi']


class MaliMusavirRegisterForm(forms.ModelForm):
    class Meta:
        model=mali_musavir
        fields=['mali_musavir_adi','mali_musavir_soyadi','mali_musavir_tc','mali_musavir_adres','mali_musavir_telefon','mali_musavir_mail','mali_musavir_dogum_tarihi','mali_musavir_ise_giris_tarihi','mali_musavir_gender','mali_musavir_photo','mali_musavir_aktiflik','mali_musavir_engelli','mali_musavir_tesvik','mali_musavir_indirim','mali_musavir_emekli']
        
class malisirketRegisterForm(forms.ModelForm):
    class Meta:
        model=mali_sirket
        fields=['mali_sirket_adi','mali_sirket_adres','mali_sirket_telefon','mali_sirket_mail']
        
class SubeRegisterForm(forms.ModelForm):
    class Meta:
        model=sube
        fields=['sube_adi','sube_kisa_unvan','sube_adres','sube_telefon','sube_mail','sube_website','sube_vergi_dairesi','sube_vergi_numarasi','sube_kurulus_tarihi','sube_mersis_no','sube_nace_kodu','sube_turu','sube_aktiflik']
        widgets = {
            'sube_kurulus_tarihi': DateInput(),
        }