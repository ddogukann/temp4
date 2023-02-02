from email.policy import default
from django.db import models

# Create your models here.
class nace(models.Model):
    nace=models.CharField(max_length=50,verbose_name="Nace Kodu")
    nace_aciklama=models.CharField(max_length=50,verbose_name="Nace Açıklama")
    class Meta:
        verbose_name_plural="Nace Kodları"
    def __str__(self):
        return self.nace + " - " + self.nace_aciklama
class vergidairesi(models.Model):
    vd_adi=models.CharField(max_length=50,verbose_name="Vergi Dairesi Adı")
    vd_kodu=models.CharField(max_length=50,verbose_name="Vergi Dairesi Kodu")
    vd_sehir=models.CharField(max_length=50,verbose_name="Vergi Dairesi Şehir")
    class Meta:
        verbose_name_plural="Vergi Daireleri"
    def __str__(self):
        return str(self.vd_kodu) + " - " +  self.vd_sehir + " - " + self.vd_adi

isyeritur=[
    ("1","Merkez"),
    ("2","Şube"),
    ("3","Mükellefiyetsiz Şube"),
]
class subs(models.Model):
    subs_sirket_adi=models.CharField(max_length=50,verbose_name="Şirket Adı")
    subs_aktiflik=models.BooleanField(default=True,verbose_name="Şirket Aktiflik Durumu")
    subs_baslangic_tarihi=models.DateField(verbose_name="Şirket Başlangıç Tarihi")
    subs_maksimum_calisan=models.IntegerField(verbose_name="Şirket Maksimum Çalışan Sayısı")
    subs_gun_sayisi=models.IntegerField(verbose_name="Paket Gün Sayısı")
    def __str__(self):
        return self.subs_sirket_adi
    class Meta:
        verbose_name_plural="Üyelikler"
class sirket(models.Model):
    sirket_adi=models.CharField(max_length=50,verbose_name="Şirket Adı")
    sirket_kisa_unvan=models.CharField(max_length=50,verbose_name="Şirket Kısa Ünvanı")
    sirket_vergi_numarasi=models.CharField(max_length=50,verbose_name="Şirket Vergi Numarası")
    sirket_vergi_dairesi=models.ForeignKey(vergidairesi,on_delete=models.RESTRICT,verbose_name=("Şirket Vergi Dairesi"))
    sirket_tc_no=models.CharField(max_length=50,verbose_name="Şirket TC Kimlik Numarası")
    sirket_mersis_no=models.CharField(max_length=50,verbose_name="Şirket Mersis Numarası")
    sirket_kurulus_tarihi=models.DateField(verbose_name="Şirket Kuruluş Tarihi")
    sirket_nace_kodu=models.ForeignKey(nace,on_delete=models.RESTRICT,verbose_name="Şirket Nace Kodu")
    sirket_adres=models.CharField(max_length=50,verbose_name="Şirket Adresi")
    sirket_telefon=models.CharField(max_length=50,verbose_name="Şirket Telefonu")
    sirket_mail=models.CharField(max_length=50,verbose_name="Şirket Mail")
    sirket_website=models.CharField(max_length=50,verbose_name="Şirket Web Sitesi")
    sirket_aktiflik=models.BooleanField(default=True,verbose_name="Şirket Aktiflik Durumu")
    sirket_tur=models.CharField(max_length=50,verbose_name="Şirket Türü",choices=isyeritur)
    sirket_davet_kodu=models.CharField(max_length=50,verbose_name="Şirket Davet Kodu")
    sirket_uyelik=models.ForeignKey(subs,on_delete=models.RESTRICT,verbose_name="Şirket Üyelik Paketi",null=True,blank=True)
    

    def __str__(self):
        return self.sirket_adi

    class Meta:
        verbose_name_plural="Şirketler"
        permissions = [
            ('sirket_listele', 'Şirketleri Listele'),
            ('calisan_listele', 'Çalışanları Listele'),
            

        ]


    
class sube(models.Model):
    sube_adi=models.CharField(max_length=50,verbose_name="Şube Adı",null=True,blank=True)
    sube_kisa_unvan=models.CharField(max_length=50,verbose_name="Şube Kısa Ünvanı", null=True,blank=True)
    sube_adres=models.CharField(max_length=50,verbose_name="Şube Adresi",null=True,blank=True)
    sube_telefon=models.CharField(max_length=50,verbose_name="Şube Telefonu", null=True,blank=True)
    sube_mail=models.CharField(max_length=50,verbose_name="Şube Mail", null=True,blank=True)
    sube_website=models.CharField(max_length=50,verbose_name="Şube Web Sitesi", null=True,blank=True)
    sube_vergi_dairesi=models.ForeignKey(vergidairesi,on_delete=models.RESTRICT,verbose_name="Şube Vergi Dairesi",null=True,blank=True)
    sube_vergi_numarasi=models.CharField(max_length=50,verbose_name="Şube Vergi Numarası",null=True,blank=True)
    sube_kurulus_tarihi=models.DateField(verbose_name="Şube Kuruluş Tarihi",null=True,blank=True)
    sube_mersis_no=models.CharField(max_length=50,verbose_name="Şube Mersis Numarası" ,null=True,blank=True)
    sube_nace_kodu=models.ForeignKey(nace,on_delete=models.RESTRICT,verbose_name="Şube Nace Kodu",null=True,blank=True)
    sube_turu=models.CharField(max_length=50,verbose_name="Şube Türü",choices=isyeritur,null=True,blank=True)
    sube_aktiflik=models.BooleanField(default=True,verbose_name="Şube Aktiflik Durumu")
    sube_sirket_id=models.ForeignKey(sirket,on_delete=models.CASCADE,verbose_name="Şube Şirket ID",related_name="subeler")

    

    def __str__(self):
        return self.sube_adi

    class Meta:
        verbose_name_plural="Şubeler"


class sgkisyeri(models.Model):
    sube_id=models.ForeignKey(sube,on_delete=models.RESTRICT,verbose_name="Şirket",null=True,blank=True)
    sgk_isyeri_adi=models.CharField(max_length=50,verbose_name="SGK İşyeri Adı",null=True,blank=True)
    sgk_isyeri_acilis_tarihi=models.DateField(verbose_name="SGK İşyeri Açılış Tarihi",null=True,blank=True)
    sgk_isyeri_sicil_no=models.CharField(max_length=50,verbose_name="SGK İşyeri Sicil Numarası",null=True,blank=True)
    sgk_isyeri_sifre=models.CharField(max_length=50,verbose_name="SGK İşyeri Şifresi",null=True,blank=True)
    sgk_isyeri_kodu=models.CharField(max_length=50,verbose_name="SGK İşyeri Kodu",null=True,blank=True)
    sgk_isyeri_adres_no=models.CharField(max_length=50,verbose_name="SGK İşyeri Adres Numarası",null=True,blank=True)
    sgk_isyeri_mulk=models.CharField(max_length=50,verbose_name="SGK İşyeri Mülkiyeti",null=True,blank=True)

class iskur(models.Model):
    sube_id=models.ForeignKey(sube,on_delete=models.CASCADE,verbose_name="Şube ID",related_name="iskur",null=True,blank=True)
    iskur_no=models.CharField(max_length=50,verbose_name="İşkur Numarası",null=True,blank=True)
    iskur_sifre=models.CharField(max_length=50,verbose_name="İşkur Şifresi",null=True,blank=True)


BOOL_CHOICES = ((True, 'Uygula'), (False, 'Uygulama'))
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
parabirimleri = [
    ('pick0','TL'),
    ('pick1','USD'),
    ('pick2','EUR'),
]
gender=[
    ('pick1','Erkek'),
    ('pick2','Kadın'),
]
def unique_filename(path):

    import os, base64, datetime
    def _func(instance, filename):
        name, ext = os.path.splitext(filename)
        name = str(base64.urlsafe_b64encode) + str(datetime.datetime.now())
        return os.path.join(path, name + ext)
    return _func

import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('calisan_photo', filename)
class calisan(models.Model):
    calisan_adi=models.CharField(max_length=50,verbose_name="Çalışan Adı")
    calisan_soyadi=models.CharField(max_length=50,verbose_name="Çalışan Soyadı")
    calisan_telefon=models.CharField(max_length=50,verbose_name="Çalışan Telefonu")
    calisan_adres=models.CharField(max_length=50,verbose_name="Çalışan Adresi")
    calisan_mail=models.CharField(max_length=50,verbose_name="Çalışan Mail")
    calisan_sirket_id=models.ForeignKey(sirket,on_delete=models.CASCADE,verbose_name="Çalışan Şirket ID",related_name="calisanlar")
    calisan_sube_id=models.ForeignKey(sube,on_delete=models.CASCADE,verbose_name="Çalışan Şube ID",related_name="calisanlar")
    calisan_tc=models.CharField(max_length=50,verbose_name="Çalışan TC")
    calisan_dogum_tarihi=models.DateField(verbose_name="Çalışan Doğum Tarihi")
    calisan_ise_giris_tarihi=models.DateField(verbose_name="Çalışan İşe Giriş Tarihi")
    calisan_isten_ayrilma_tarihi=models.DateField(verbose_name="Çalışan İşten Ayrılma Tarihi",null=True,blank=True)
    calisan_isten_ayrilma_nedeni=models.CharField(max_length=50,verbose_name="Çalışan İşten Ayrılma Nedeni",null=True,blank=True)
    calisan_aktiflik=models.BooleanField(default=True,verbose_name="Çalışan Aktiflik Durumu")
    calisan_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name="Çalışan ID")
    calisan_engelli=models.CharField(max_length=50,verbose_name="Çalışan Engelli Durumu")
    calisan_tur=models.CharField(max_length=50,verbose_name="Çalışan Türü")
    calisan_tesvik=models.CharField(max_length=50,verbose_name="Çalışan Tesvik Durumu",choices=calisantur)
    calisan_indirim=models.BooleanField(default=False,verbose_name="5510/5746 İndirim Durumu",choices=BOOL_CHOICES)
    calisan_emekli=models.BooleanField(default=False,verbose_name="Çalışan Emekli Durumu",choices=BOOL_CHOICES)
    calisan_photo=models.ImageField(upload_to=get_file_path,verbose_name="Çalışan Fotoğrafı",null=True,blank=True)
    calisan_gender=models.CharField(max_length=50,verbose_name="Çalışan Cinsiyeti",choices=gender,default="pick1")
    calisan_eski_hukumlu=models.BooleanField(default=False,verbose_name="Çalışan Eski Hükümlü Durumu",choices=BOOL_CHOICES)
    calisan_ogrenim_durumu=models.CharField(max_length=50,verbose_name="Çalışan Öğrenim Durumu",null=True,blank=True)
    calisan_iban=models.CharField(max_length=50,verbose_name="Çalışan IBAN",null=True,blank=True)
    calisan_isten_ayrilma=models.BooleanField(default=False,verbose_name="Çalışan İşten Ayrıldı",)
    calisan_isten_ayrilma_tarihi=models.DateField(verbose_name="Çalışan İşten Ayrılma Tarihi",null=True,blank=True)
    calisan_isten_ayrilma_nedeni=models.CharField(max_length=200,verbose_name="Çalışan İşten Ayrılma Nedeni",null=True,blank=True)
    calisan_isten_ayrilma_kodu=models.CharField(max_length=50,verbose_name="Çalışan İşten Ayrılma Kodu",null=True,blank=True)

   

    def __str__(self):
        return self.calisan_adi+" "+self.calisan_soyadi

    class Meta:
        verbose_name_plural="Çalışanlar"
ucrettipi = [
    ('pick0','Brüt'),
    ('pick1','Net'),
]
class maas(models.Model):
    ucret=models.FloatField(verbose_name="Ücret",default=0)
    ucrettipi=models.CharField(max_length=50,verbose_name="Ücret Tipi",choices=ucrettipi,default="pick0")
    maas_tutari1=models.FloatField(verbose_name="Ocak",default=0)
    gunsayisi1=models.IntegerField(verbose_name="Ocak Gün",default=0)
    argegun1=models.IntegerField(verbose_name="Ocak AR-GE Gün",default=0)
    maas_tutari2=models.FloatField(verbose_name="Şubat",default=0)
    gunsayisi2=models.IntegerField(verbose_name="Şubat Gün",default=0)
    argegun2=models.IntegerField(verbose_name="Şubat AR-GE Gün",default=0)
    maas_tutari3=models.FloatField(verbose_name="Mart",default=0)
    gunsayisi3=models.IntegerField(verbose_name="Mart Gün",default=0)
    argegun3=models.IntegerField(verbose_name="Mart AR-GE Gün",default=0)
    maas_tutari4=models.FloatField(verbose_name="Nisan",default=0)
    gunsayisi4=models.IntegerField(verbose_name="Nisan Gün",default=0)
    argegun4=models.IntegerField(verbose_name="Nisan AR-GE Gün",default=0)
    maas_tutari5=models.FloatField(verbose_name="Mayıs",default=0)
    gunsayisi5=models.IntegerField(verbose_name="Mayıs Gün",default=0)
    argegun5=models.IntegerField(verbose_name="Mayıs AR-GE Gü",default=0)
    maas_tutari6=models.FloatField(verbose_name="Haziran",default=0)
    gunsayisi6=models.IntegerField(verbose_name="Haziran Gün",default=0)
    argegun6=models.IntegerField(verbose_name="Haziran AR-GE Gün",default=0)
    maas_tutari7=models.FloatField(verbose_name="Temmuz",default=0)
    gunsayisi7=models.IntegerField(verbose_name="Temmuz Gün",default=0)
    argegun7=models.IntegerField(verbose_name="Temmuz AR-GE Gün",default=0)
    maas_tutari8=models.FloatField(verbose_name="Ağustos",default=0)
    gunsayisi8=models.IntegerField(verbose_name="Ağustos Gün",default=0)
    argegun8=models.IntegerField(verbose_name="Ağustos AR-GE Gün",default=0)
    maas_tutari9=models.FloatField(verbose_name="Eylül",default=0)
    gunsayisi9=models.IntegerField(verbose_name="Eylül Gün",default=0)
    argegun9=models.IntegerField(verbose_name="Eylül AR-GE Gün",default=0)
    maas_tutari10=models.FloatField(verbose_name="Ekim",default=0)
    gunsayisi10=models.IntegerField(verbose_name="Ekim Gün",default=0)
    argegun10=models.IntegerField(verbose_name="Ekim AR-GE Gün",default=0)
    maas_tutari11=models.FloatField(verbose_name="Kasım",default=0)
    gunsayisi11=models.IntegerField(verbose_name="Kasım Gün",default=0)
    argegun11=models.IntegerField(verbose_name="Kasım AR-GE Gü",default=0)
    maas_tutari12=models.FloatField(verbose_name="Aralık",default=0)
    gunsayisi12=models.IntegerField(verbose_name="Aralıkv",default=0)
    argegun12=models.IntegerField(verbose_name="Aralık AR-GE Gün",default=0)
    yil=models.IntegerField(verbose_name="Yıl")
    calisan_id=models.ForeignKey(calisan,on_delete=models.CASCADE,verbose_name="Çalışan ID")
    para_birimi=models.CharField(max_length=50,verbose_name="Para Birimi",choices=parabirimleri,default="pick0")
    def __str__(self):
        return str(self.calisan_id) +" "+ str(self.yil)
    class Meta:
        verbose_name_plural="Maaşlar"
    
class mali_sirket(models.Model):
    mali_sirket_adi=models.CharField(max_length=50,verbose_name="Mali Şirket Adı")
    mali_sirket_telefon=models.CharField(max_length=50,verbose_name="Mali Şirket Telefonu")
    mali_sirket_adres=models.CharField(max_length=50,verbose_name="Mali Şirket Adresi")
    mali_sirket_mail=models.CharField(max_length=50,verbose_name="Mali Şirket Mail")
    mali_sirket_davet_kodu=models.CharField(max_length=50,verbose_name="Mali Şirket Davet Kodu")
    mali_sirket_bagli_sirketler=models.ManyToManyField(sirket,verbose_name="Mali Şirket Bağlı Şirketler")
    def __str__(self):
        return self.mali_sirket_adi
    class Meta:
        verbose_name_plural="Mali Şirketler"


class mali_musavir(models.Model):
    mali_musavir_adi=models.CharField(max_length=50,verbose_name="Mali Müşavir Adı")
    mali_musavir_soyadi=models.CharField(max_length=50,verbose_name="Mali Müşavir Soyadı")
    mali_musavir_telefon=models.CharField(max_length=50,verbose_name="Mali Müşavir Telefonu")
    mali_musavir_adres=models.CharField(max_length=50,verbose_name="Mali Müşavir Adresi")
    mali_musavir_mail=models.CharField(max_length=50,verbose_name="Mali Müşavir Mail")
    mali_musavir_tc=models.CharField(max_length=50,verbose_name="Mali Müşavir TC")
    mali_musavir_dogum_tarihi=models.DateField(verbose_name="Mali Müşavir Doğum Tarihi")
    mali_musavir_ise_giris_tarihi=models.DateField(verbose_name="Mali Müşavir İşe Giriş Tarihi")
    mali_musavir_aktiflik=models.BooleanField(default=True,verbose_name="Mali Müşavir Aktiflik Durumu")
    mali_musavir_id=models.ForeignKey('auth.user',on_delete=models.DO_NOTHING,verbose_name="Mali Müşavir ID")
    mali_musavir_engelli=models.CharField(max_length=50,verbose_name="Mali Müşavir Engelli Durumu")
    mali_musavir_tesvik=models.CharField(max_length=50,verbose_name="Mali Müşavir Tesvik Durumu",choices=calisantur)
    mali_musavir_indirim=models.BooleanField(default=False,verbose_name="5510/5746 İndirim Durumu",choices=BOOL_CHOICES)
    mali_musavir_emekli=models.BooleanField(default=False,verbose_name="Mali Müşavir Emekli Durumu")
    deneme_suresi=models.BooleanField(default=False,verbose_name="Deneme Süresi Durumu",null=True)
    deneme_bitis_tarihi=models.DateField(verbose_name="Deneme Bitiş Tarihi",null=True,blank=True)
    mali_sirket_id=models.ForeignKey(mali_sirket,on_delete=models.DO_NOTHING,verbose_name="Mali Şirket ID",related_name="mali_musavirler")
    mali_musavir_photo=models.ImageField(upload_to=get_file_path,verbose_name="Çalışan Fotoğrafı",null=True,blank=True)
    mali_musavir_gender=models.CharField(max_length=50,verbose_name="Çalışan Cinsiyeti",choices=gender)
    def __str__(self):
        return self.mali_musavir_adi+" "+self.mali_musavir_soyadi

    class Meta:
        verbose_name_plural="Mali Müşavirler"








class bordro(models.Model):
    calisan_id=models.ForeignKey(calisan,on_delete=models.DO_NOTHING,verbose_name="Çalışan ID",null=True)
    maas_id=models.ForeignKey(maas,on_delete=models.CASCADE,verbose_name="Maaş ID")
    bordro_kumulatifasgarivergi=models.FloatField(verbose_name="Bordro Kumulatif Asgari Vergi",default=0)
    bordro_kumularifasgariucret=models.FloatField(verbose_name="Bordro Kumulatif Asgari Ücret",default=0)
    ocak_brut=models.FloatField(verbose_name="Ocak Brüt",default=0)
    ocak_calisilan_gun=models.FloatField(verbose_name="Ocak Çalışılan Gün",default=0)
    ocak_arge_gun=models.FloatField(verbose_name="Ocak Arge Günü",default=0)
    ocak_bordroyaesasbrut=models.FloatField(verbose_name="Ocak Bordro Yasağa Esas Brüt",default=0)
    ocak_sgk_matrahi=models.FloatField(verbose_name="Ocak SGK Matrahi",default=0)
    ocak_sgk_kesintisi=models.FloatField(verbose_name="Ocak SGK Kesintisi",default=0)
    ocak_issizlik_kesintisi=models.FloatField(verbose_name="Ocak İşsizlik Kesintisi",default=0)
    ocak_kumulatif_asgari_ucret=models.FloatField(verbose_name="Ocak Kumulatif Asgari Vergi",default=0)
    ocak_kumulatif_vergi=models.FloatField(verbose_name="Ocak Kumulatif Vergi",default=0)
    ocak_vergi_dilimi=models.CharField(max_length=50,verbose_name="Ocak Vergi Dilimi",default=0)
    ocak_istisna_oncesi_gelir=models.FloatField(verbose_name="Ocak İstisna Öncesi Gelir",default=0)
    ocak_istisna_oncesi_damga=models.FloatField(verbose_name="Ocak İstisna Öncesi Damga",default=0)
    ocak_vergi_matrahi=models.FloatField(verbose_name="Ocak Vergi Matrahi",default=0)
    ocak_asgari_vergi=models.FloatField(verbose_name="Ocak Asgari Vergi",default=0)
    ocak_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Ocak Asgari Gelir Vergisi İstisnası",default=0)
    ocak_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Ocak Asgari Damga Vergisi İstisnası",default=0)
    ocak_damga_vergisi=models.FloatField(verbose_name="Ocak Damga Vergisi",default=0)
    ocak_gelir_vergisi=models.FloatField(verbose_name="Ocak Gelir Vergisi",default=0)
    ocak_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Ocak Gelir Vergisi İstisnası",default=0)
    ocak_damga_vergisi_istisnasi=models.FloatField(verbose_name="Ocak Damga Vergisi İstisnası",default=0)
    ocak_net_ucret=models.FloatField(verbose_name="Ocak Net Ücret",default=0)
    ocak_isveren_sgk_kesintisi=models.FloatField(verbose_name="Ocak İşveren SGK Kesintisi",default=0)
    ocak_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Ocak İşveren İşsizlik Kesintisi",default=0)
    ocak_toplam_sgk_kesintisi=models.FloatField(verbose_name="Ocak Toplam SGK Kesintisi",default=0)
    ocak_toplam_maliyet=models.FloatField(verbose_name="Ocak Toplam Maliyet",default=0)
    ocak_sgk_istisnasi=models.FloatField(verbose_name="Ocak SGK İstisnası",default=0)
    ocak_odenecek_sgk=models.FloatField(verbose_name="Ocak Ödenecek SGK",default=0)
    ocak_odenecek_gelir_vergisi=models.FloatField(verbose_name="Ocak Ödenecek Gelir Vergisi",default=0)
    ocak_odenecek_damga_vergisi=models.FloatField(verbose_name="Ocak Ödenecek Damga Vergisi",default=0)
    ocak_kanun_no=models.CharField(max_length=50,verbose_name="Ocak Kanun No",default="pick1")
    subat_brut=models.FloatField(verbose_name="Şubat Brüt",default=0)
    subat_calisilan_gun=models.FloatField(verbose_name="Şubat Çalışılan Gün",default=0)
    subat_arge_gun=models.FloatField(verbose_name="Şubat Arge Günü",default=0)
    subat_bordroyaesasbrut=models.FloatField(verbose_name="Şubat Bordro Yasağa Esas Brüt",default=0)
    subat_sgk_matrahi=models.FloatField(verbose_name="Şubat SGK Matrahi",default=0)
    subat_sgk_kesintisi=models.FloatField(verbose_name="Şubat SGK Kesintisi",default=0)
    subat_issizlik_kesintisi=models.FloatField(verbose_name="Şubat İşsizlik Kesintisi",default=0)
    subat_kumulatif_asgari_ucret=models.FloatField(verbose_name="Şubat Kumulatif Asgari Vergi",default=0)
    subat_kumulatif_vergi=models.FloatField(verbose_name="Şubat Kumulatif Vergi",default=0)
    subat_vergi_dilimi=models.CharField(max_length=50,verbose_name="Şubat Vergi Dilimi",default=0)
    subat_istisna_oncesi_gelir=models.FloatField(verbose_name="Şubat İstisna Öncesi Gelir",default=0)
    subat_istisna_oncesi_damga=models.FloatField(verbose_name="Şubat İstisna Öncesi Damga",default=0)
    subat_vergi_matrahi=models.FloatField(verbose_name="Şubat Vergi Matrahi",default=0)
    subat_asgari_vergi=models.FloatField(verbose_name="Şubat Asgari Vergi",default=0)
    subat_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Şubat Asgari Gelir Vergisi İstisnası",default=0)
    subat_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Şubat Asgari Damga Vergisi İstisnası",default=0)
    subat_damga_vergisi=models.FloatField(verbose_name="Şubat Damga Vergisi",default=0)
    subat_gelir_vergisi=models.FloatField(verbose_name="Şubat Gelir Vergisi",default=0)
    subat_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Şubat Gelir Vergisi İstisnası",default=0)
    subat_damga_vergisi_istisnasi=models.FloatField(verbose_name="Şubat Damga Vergisi İstisnası",default=0)
    subat_net_ucret=models.FloatField(verbose_name="Şubat Net Ücret",default=0)
    subat_isveren_sgk_kesintisi=models.FloatField(verbose_name="Şubat İşveren SGK Kesintisi",default=0)
    subat_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Şubat İşveren İşsizlik Kesintisi",default=0)
    subat_toplam_sgk_kesintisi=models.FloatField(verbose_name="Şubat Toplam SGK Kesintisi",default=0)
    subat_toplam_maliyet=models.FloatField(verbose_name="Şubat Toplam Maliyet",default=0)
    subat_sgk_istisnasi=models.FloatField(verbose_name="Şubat SGK İstisnası",default=0)
    subat_odenecek_sgk=models.FloatField(verbose_name="Şubat Ödenecek SGK",default=0)
    subat_odenecek_gelir_vergisi=models.FloatField(verbose_name="Şubat Ödenecek Gelir Vergisi",default=0)
    subat_odenecek_damga_vergisi=models.FloatField(verbose_name="Şubat Ödenecek Damga Vergisi",default=0)
    subat_kanun_no=models.CharField(max_length=50,verbose_name="Şubat Kanun No",default="pick1")
    mart_brut=models.FloatField(verbose_name="Mart Brüt",default=0)
    mart_calisilan_gun=models.FloatField(verbose_name="Mart Çalışılan Gün",default=0)
    mart_arge_gun=models.FloatField(verbose_name="Mart Arge Günü",default=0)
    mart_bordroyaesasbrut=models.FloatField(verbose_name="Mart Bordro Yasağa Esas Brüt",default=0)
    mart_sgk_matrahi=models.FloatField(verbose_name="Mart SGK Matrahi",default=0)
    mart_sgk_kesintisi=models.FloatField(verbose_name="Mart SGK Kesintisi",default=0)
    mart_issizlik_kesintisi=models.FloatField(verbose_name="Mart İşsizlik Kesintisi",default=0)
    mart_kumulatif_asgari_ucret=models.FloatField(verbose_name="Mart Kumulatif Asgari Vergi",default=0)
    mart_kumulatif_vergi=models.FloatField(verbose_name="Mart Kumulatif Vergi",default=0)
    mart_vergi_dilimi=models.CharField(max_length=50,verbose_name="Mart Vergi Dilimi",default=0)
    mart_istisna_oncesi_gelir=models.FloatField(verbose_name="Mart İstisna Öncesi Gelir",default=0)
    mart_istisna_oncesi_damga=models.FloatField(verbose_name="Mart İstisna Öncesi Damga",default=0)
    mart_vergi_matrahi=models.FloatField(verbose_name="Mart Vergi Matrahi",default=0)
    mart_asgari_vergi=models.FloatField(verbose_name="Mart Asgari Vergi",default=0)
    mart_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Mart Asgari Gelir Vergisi İstisnası",default=0)
    mart_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Mart Asgari Damga Vergisi İstisnası",default=0)
    mart_damga_vergisi=models.FloatField(verbose_name="Mart Damga Vergisi",default=0)
    mart_gelir_vergisi=models.FloatField(verbose_name="Mart Gelir Vergisi",default=0)
    mart_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Mart Gelir Vergisi İstisnası",default=0)
    mart_damga_vergisi_istisnasi=models.FloatField(verbose_name="Mart Damga Vergisi İstisnası",default=0)
    mart_net_ucret=models.FloatField(verbose_name="Mart Net Ücret",default=0)
    mart_isveren_sgk_kesintisi=models.FloatField(verbose_name="Mart İşveren SGK Kesintisi",default=0)
    mart_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Mart İşveren İşsizlik Kesintisi",default=0)
    mart_toplam_sgk_kesintisi=models.FloatField(verbose_name="Mart Toplam SGK Kesintisi",default=0)
    mart_toplam_maliyet=models.FloatField(verbose_name="Mart Toplam Maliyet",default=0)
    mart_sgk_istisnasi=models.FloatField(verbose_name="Mart SGK İstisnası",default=0)
    mart_odenecek_sgk=models.FloatField(verbose_name="Mart Ödenecek SGK",default=0)
    mart_odenecek_gelir_vergisi=models.FloatField(verbose_name="Mart Ödenecek Gelir Vergisi",default=0)
    mart_odenecek_damga_vergisi=models.FloatField(verbose_name="Mart Ödenecek Damga Vergisi",default=0)
    mart_kanun_no=models.CharField(max_length=50,verbose_name="Mart Kanun No",default="pick1")
    nisan_brut=models.FloatField(verbose_name="Nisan Brüt",default=0)
    nisan_calisilan_gun=models.FloatField(verbose_name="Nisan Çalışılan Gün",default=0)
    nisan_arge_gun=models.FloatField(verbose_name="Nisan Arge Günü",default=0)
    nisan_bordroyaesasbrut=models.FloatField(verbose_name="Nisan Bordro Yasağa Esas Brüt",default=0)
    nisan_sgk_matrahi=models.FloatField(verbose_name="Nisan SGK Matrahi",default=0)
    nisan_sgk_kesintisi=models.FloatField(verbose_name="Nisan SGK Kesintisi",default=0)
    nisan_issizlik_kesintisi=models.FloatField(verbose_name="Nisan İşsizlik Kesintisi",default=0)
    nisan_kumulatif_asgari_ucret=models.FloatField(verbose_name="Nisan Kumulatif Asgari Vergi",default=0)
    nisan_kumulatif_vergi=models.FloatField(verbose_name="Nisan Kumulatif Vergi",default=0)
    nisan_vergi_dilimi=models.CharField(max_length=50,verbose_name="Nisan Vergi Dilimi",default=0)
    nisan_istisna_oncesi_gelir=models.FloatField(verbose_name="Nisan İstisna Öncesi Gelir",default=0)
    nisan_istisna_oncesi_damga=models.FloatField(verbose_name="Nisan İstisna Öncesi Damga",default=0)
    nisan_vergi_matrahi=models.FloatField(verbose_name="Nisan Vergi Matrahi",default=0)
    nisan_asgari_vergi=models.FloatField(verbose_name="Nisan Asgari Vergi",default=0)
    nisan_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Nisan Asgari Gelir Vergisi İstisnası",default=0)
    nisan_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Nisan Asgari Damga Vergisi İstisnası",default=0)
    nisan_damga_vergisi=models.FloatField(verbose_name="Nisan Damga Vergisi",default=0)
    nisan_gelir_vergisi=models.FloatField(verbose_name="Nisan Gelir Vergisi",default=0)
    nisan_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Nisan Gelir Vergisi İstisnası",default=0)
    nisan_damga_vergisi_istisnasi=models.FloatField(verbose_name="Nisan Damga Vergisi İstisnası",default=0)
    nisan_net_ucret=models.FloatField(verbose_name="Nisan Net Ücret",default=0)
    nisan_isveren_sgk_kesintisi=models.FloatField(verbose_name="Nisan İşveren SGK Kesintisi",default=0)
    nisan_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Nisan İşveren İşsizlik Kesintisi",default=0)
    nisan_toplam_sgk_kesintisi=models.FloatField(verbose_name="Nisan Toplam SGK Kesintisi",default=0)
    nisan_toplam_maliyet=models.FloatField(verbose_name="Nisan Toplam Maliyet",default=0)
    nisan_sgk_istisnasi=models.FloatField(verbose_name="Nisan SGK İstisnası",default=0)
    nisan_odenecek_sgk=models.FloatField(verbose_name="Nisan Ödenecek SGK",default=0)
    nisan_odenecek_gelir_vergisi=models.FloatField(verbose_name="Nisan Ödenecek Gelir Vergisi",default=0)
    nisan_odenecek_damga_vergisi=models.FloatField(verbose_name="Nisan Ödenecek Damga Vergisi",default=0)
    nisan_kanun_no=models.CharField(max_length=50,verbose_name="Nisan Kanun No",default="pick1")
    mayis_brut=models.FloatField(verbose_name="Mayıs Brüt",default=0)
    mayis_calisilan_gun=models.FloatField(verbose_name="Mayıs Çalışılan Gün",default=0)
    mayis_arge_gun=models.FloatField(verbose_name="Mayıs Arge Günü",default=0)
    mayis_bordroyaesasbrut=models.FloatField(verbose_name="Mayıs Bordro Yasağa Esas Brüt",default=0)
    mayis_sgk_matrahi=models.FloatField(verbose_name="Mayıs SGK Matrahi",default=0)
    mayis_sgk_kesintisi=models.FloatField(verbose_name="Mayıs SGK Kesintisi",default=0)
    mayis_issizlik_kesintisi=models.FloatField(verbose_name="Mayıs İşsizlik Kesintisi",default=0)
    mayis_kumulatif_asgari_ucret=models.FloatField(verbose_name="Mayıs Kumulatif Asgari Vergi",default=0)
    mayis_kumulatif_vergi=models.FloatField(verbose_name="Mayıs Kumulatif Vergi",default=0)
    mayis_vergi_dilimi=models.CharField(max_length=50,verbose_name="Mayıs Vergi Dilimi",default=0)
    mayis_istisna_oncesi_gelir=models.FloatField(verbose_name="Mayıs İstisna Öncesi Gelir",default=0)
    mayis_istisna_oncesi_damga=models.FloatField(verbose_name="Mayıs İstisna Öncesi Damga",default=0)
    mayis_vergi_matrahi=models.FloatField(verbose_name="Mayıs Vergi Matrahi",default=0)
    mayis_asgari_vergi=models.FloatField(verbose_name="Mayıs Asgari Vergi",default=0)
    mayis_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Mayıs Asgari Gelir Vergisi İstisnası",default=0)
    mayis_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Mayıs Asgari Damga Vergisi İstisnası",default=0)
    mayis_damga_vergisi=models.FloatField(verbose_name="Mayıs Damga Vergisi",default=0)
    mayis_gelir_vergisi=models.FloatField(verbose_name="Mayıs Gelir Vergisi",default=0)
    mayis_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Mayıs Gelir Vergisi İstisnası",default=0)
    mayis_damga_vergisi_istisnasi=models.FloatField(verbose_name="Mayıs Damga Vergisi İstisnası",default=0)
    mayis_net_ucret=models.FloatField(verbose_name="Mayıs Net Ücret",default=0)
    mayis_isveren_sgk_kesintisi=models.FloatField(verbose_name="Mayıs İşveren SGK Kesintisi",default=0)
    mayis_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Mayıs İşveren İşsizlik Kesintisi",default=0)
    mayis_toplam_sgk_kesintisi=models.FloatField(verbose_name="Mayıs Toplam SGK Kesintisi",default=0)
    mayis_toplam_maliyet=models.FloatField(verbose_name="Mayıs Toplam Maliyet",default=0)
    mayis_sgk_istisnasi=models.FloatField(verbose_name="Mayıs SGK İstisnası",default=0)
    mayis_odenecek_sgk=models.FloatField(verbose_name="Mayıs Ödenecek SGK",default=0)
    mayis_odenecek_gelir_vergisi=models.FloatField(verbose_name="Mayıs Ödenecek Gelir Vergisi",default=0)
    mayis_odenecek_damga_vergisi=models.FloatField(verbose_name="Mayıs Ödenecek Damga Vergisi",default=0)
    mayis_kanun_no=models.CharField(max_length=50,verbose_name="Mayıs Kanun No",default="pick1")
    haziran_brut=models.FloatField(verbose_name="Haziran Brüt",default=0)
    haziran_calisilan_gun=models.FloatField(verbose_name="Haziran Çalışılan Gün",default=0)
    haziran_arge_gun=models.FloatField(verbose_name="Haziran Arge Günü",default=0)
    haziran_bordroyaesasbrut=models.FloatField(verbose_name="Haziran Bordro Yasağa Esas Brüt",default=0)
    haziran_sgk_matrahi=models.FloatField(verbose_name="Haziran SGK Matrahi",default=0)
    haziran_sgk_kesintisi=models.FloatField(verbose_name="Haziran SGK Kesintisi",default=0)
    haziran_issizlik_kesintisi=models.FloatField(verbose_name="Haziran İşsizlik Kesintisi",default=0)
    haziran_kumulatif_asgari_ucret=models.FloatField(verbose_name="Haziran Kumulatif Asgari Vergi",default=0)
    haziran_kumulatif_vergi=models.FloatField(verbose_name="Haziran Kumulatif Vergi",default=0)
    haziran_vergi_dilimi=models.CharField(max_length=50,verbose_name="Haziran Vergi Dilimi",default=0)
    haziran_istisna_oncesi_gelir=models.FloatField(verbose_name="Haziran İstisna Öncesi Gelir",default=0)
    haziran_istisna_oncesi_damga=models.FloatField(verbose_name="Haziran İstisna Öncesi Damga",default=0)
    haziran_vergi_matrahi=models.FloatField(verbose_name="Haziran Vergi Matrahi",default=0)
    haziran_asgari_vergi=models.FloatField(verbose_name="Haziran Asgari Vergi",default=0)
    haziran_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Haziran Asgari Gelir Vergisi İstisnası",default=0)
    haziran_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Haziran Asgari Damga Vergisi İstisnası",default=0)
    haziran_damga_vergisi=models.FloatField(verbose_name="Haziran Damga Vergisi",default=0)
    haziran_gelir_vergisi=models.FloatField(verbose_name="Haziran Gelir Vergisi",default=0)
    haziran_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Haziran Gelir Vergisi İstisnası",default=0)
    haziran_damga_vergisi_istisnasi=models.FloatField(verbose_name="Haziran Damga Vergisi İstisnası",default=0)
    haziran_net_ucret=models.FloatField(verbose_name="Haziran Net Ücret",default=0)
    haziran_isveren_sgk_kesintisi=models.FloatField(verbose_name="Haziran İşveren SGK Kesintisi",default=0)
    haziran_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Haziran İşveren İşsizlik Kesintisi",default=0)
    haziran_toplam_sgk_kesintisi=models.FloatField(verbose_name="Haziran Toplam SGK Kesintisi",default=0)
    haziran_toplam_maliyet=models.FloatField(verbose_name="Haziran Toplam Maliyet",default=0)
    haziran_sgk_istisnasi=models.FloatField(verbose_name="Haziran SGK İstisnası",default=0)
    haziran_odenecek_sgk=models.FloatField(verbose_name="Haziran Ödenecek SGK",default=0)
    haziran_odenecek_gelir_vergisi=models.FloatField(verbose_name="Haziran Ödenecek Gelir Vergisi",default=0)
    haziran_odenecek_damga_vergisi=models.FloatField(verbose_name="Haziran Ödenecek Damga Vergisi",default=0)
    haziran_kanun_no=models.CharField(max_length=50,verbose_name="Haziran Kanun No",default="pick1")
    temmuz_brut=models.FloatField(verbose_name="Temmuz Brüt",default=0)
    temmuz_calisilan_gun=models.FloatField(verbose_name="Temmuz Çalışılan Gün",default=0)
    temmuz_arge_gun=models.FloatField(verbose_name="Temmuz Arge Günü",default=0)
    temmuz_bordroyaesasbrut=models.FloatField(verbose_name="Temmuz Bordro Yasağa Esas Brüt",default=0)
    temmuz_sgk_matrahi=models.FloatField(verbose_name="Temmuz SGK Matrahi",default=0)
    temmuz_sgk_kesintisi=models.FloatField(verbose_name="Temmuz SGK Kesintisi",default=0)
    temmuz_issizlik_kesintisi=models.FloatField(verbose_name="Temmuz İşsizlik Kesintisi",default=0)
    temmuz_kumulatif_asgari_ucret=models.FloatField(verbose_name="Temmuz Kumulatif Asgari Vergi",default=0)
    temmuz_kumulatif_vergi=models.FloatField(verbose_name="Temmuz Kumulatif Vergi",default=0)
    temmuz_vergi_dilimi=models.CharField(max_length=50,verbose_name="Temmuz Vergi Dilimi",default=0)
    temmuz_istisna_oncesi_gelir=models.FloatField(verbose_name="Temmuz İstisna Öncesi Gelir",default=0)
    temmuz_istisna_oncesi_damga=models.FloatField(verbose_name="Temmuz İstisna Öncesi Damga",default=0)
    temmuz_vergi_matrahi=models.FloatField(verbose_name="Temmuz Vergi Matrahi",default=0)
    temmuz_asgari_vergi=models.FloatField(verbose_name="Temmuz Asgari Vergi",default=0)
    temmuz_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Temmuz Asgari Gelir Vergisi İstisnası",default=0)
    temmuz_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Temmuz Asgari Damga Vergisi İstisnası",default=0)
    temmuz_damga_vergisi=models.FloatField(verbose_name="Temmuz Damga Vergisi",default=0)
    temmuz_gelir_vergisi=models.FloatField(verbose_name="Temmuz Gelir Vergisi",default=0)
    temmuz_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Temmuz Gelir Vergisi İstisnası",default=0)
    temmuz_damga_vergisi_istisnasi=models.FloatField(verbose_name="Temmuz Damga Vergisi İstisnası",default=0)
    temmuz_net_ucret=models.FloatField(verbose_name="Temmuz Net Ücret",default=0)
    temmuz_isveren_sgk_kesintisi=models.FloatField(verbose_name="Temmuz İşveren SGK Kesintisi",default=0)
    temmuz_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Temmuz İşveren İşsizlik Kesintisi",default=0)
    temmuz_toplam_sgk_kesintisi=models.FloatField(verbose_name="Temmuz Toplam SGK Kesintisi",default=0)
    temmuz_toplam_maliyet=models.FloatField(verbose_name="Temmuz Toplam Maliyet",default=0)
    temmuz_sgk_istisnasi=models.FloatField(verbose_name="Temmuz SGK İstisnası",default=0)
    temmuz_odenecek_sgk=models.FloatField(verbose_name="Temmuz Ödenecek SGK",default=0)
    temmuz_odenecek_gelir_vergisi=models.FloatField(verbose_name="Temmuz Ödenecek Gelir Vergisi",default=0)
    temmuz_odenecek_damga_vergisi=models.FloatField(verbose_name="Temmuz Ödenecek Damga Vergisi",default=0)
    temmuz_kanun_no=models.CharField(max_length=50,verbose_name="Temmuz Kanun No",default="pick1")
    agustos_brut=models.FloatField(verbose_name="Ağustos Brüt",default=0)
    agustos_calisilan_gun=models.FloatField(verbose_name="Ağustos Çalışılan Gün",default=0)
    agustos_arge_gun=models.FloatField(verbose_name="Ağustos Arge Günü",default=0)
    agustos_bordroyaesasbrut=models.FloatField(verbose_name="Ağustos Bordro Yasağa Esas Brüt",default=0)
    agustos_sgk_matrahi=models.FloatField(verbose_name="Ağustos SGK Matrahi",default=0)
    agustos_sgk_kesintisi=models.FloatField(verbose_name="Ağustos SGK Kesintisi",default=0)
    agustos_issizlik_kesintisi=models.FloatField(verbose_name="Ağustos İşsizlik Kesintisi",default=0)
    agustos_kumulatif_asgari_ucret=models.FloatField(verbose_name="Ağustos Kumulatif Asgari Vergi",default=0)
    agustos_kumulatif_vergi=models.FloatField(verbose_name="Ağustos Kumulatif Vergi",default=0)
    agustos_vergi_dilimi=models.CharField(max_length=50,verbose_name="Ağustos Vergi Dilimi",default=0)
    agustos_istisna_oncesi_gelir=models.FloatField(verbose_name="Ağustos İstisna Öncesi Gelir",default=0)
    agustos_istisna_oncesi_damga=models.FloatField(verbose_name="Ağustos İstisna Öncesi Damga",default=0)
    agustos_vergi_matrahi=models.FloatField(verbose_name="Ağustos Vergi Matrahi",default=0)
    agustos_asgari_vergi=models.FloatField(verbose_name="Ağustos Asgari Vergi",default=0)
    agustos_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Ağustos Asgari Gelir Vergisi İstisnası",default=0)
    agustos_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Ağustos Asgari Damga Vergisi İstisnası",default=0)
    agustos_damga_vergisi=models.FloatField(verbose_name="Ağustos Damga Vergisi",default=0)
    agustos_gelir_vergisi=models.FloatField(verbose_name="Ağustos Gelir Vergisi",default=0)
    agustos_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Ağustos Gelir Vergisi İstisnası",default=0)
    agustos_damga_vergisi_istisnasi=models.FloatField(verbose_name="Ağustos Damga Vergisi İstisnası",default=0)
    agustos_net_ucret=models.FloatField(verbose_name="Ağustos Net Ücret",default=0)
    agustos_isveren_sgk_kesintisi=models.FloatField(verbose_name="Ağustos İşveren SGK Kesintisi",default=0)
    agustos_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Ağustos İşveren İşsizlik Kesintisi",default=0)
    agustos_toplam_sgk_kesintisi=models.FloatField(verbose_name="Ağustos Toplam SGK Kesintisi",default=0)
    agustos_toplam_maliyet=models.FloatField(verbose_name="Ağustos Toplam Maliyet",default=0)
    agustos_sgk_istisnasi=models.FloatField(verbose_name="Ağustos SGK İstisnası",default=0)
    agustos_odenecek_sgk=models.FloatField(verbose_name="Ağustos Ödenecek SGK",default=0)
    agustos_odenecek_gelir_vergisi=models.FloatField(verbose_name="Ağustos Ödenecek Gelir Vergisi",default=0)
    agustos_odenecek_damga_vergisi=models.FloatField(verbose_name="Ağustos Ödenecek Damga Vergisi",default=0)
    agustos_kanun_no=models.CharField(max_length=50,verbose_name="Ağustos Kanun No",default="pick1")
    eylul_brut=models.FloatField(verbose_name="Eylül Brüt",default=0)
    eylul_calisilan_gun=models.FloatField(verbose_name="Eylül Çalışılan Gün",default=0)
    eylul_arge_gun=models.FloatField(verbose_name="Eylül Arge Günü",default=0)
    eylul_bordroyaesasbrut=models.FloatField(verbose_name="Eylül Bordro Yasağa Esas Brüt",default=0)
    eylul_sgk_matrahi=models.FloatField(verbose_name="Eylül SGK Matrahi",default=0)
    eylul_sgk_kesintisi=models.FloatField(verbose_name="Eylül SGK Kesintisi",default=0)
    eylul_issizlik_kesintisi=models.FloatField(verbose_name="Eylül İşsizlik Kesintisi",default=0)
    eylul_kumulatif_asgari_ucret=models.FloatField(verbose_name="Eylül Kumulatif Asgari Vergi",default=0)
    eylul_kumulatif_vergi=models.FloatField(verbose_name="Eylül Kumulatif Vergi",default=0)
    eylul_vergi_dilimi=models.CharField(max_length=50,verbose_name="Eylül Vergi Dilimi",default=0)
    eylul_istisna_oncesi_gelir=models.FloatField(verbose_name="Eylül İstisna Öncesi Gelir",default=0)
    eylul_istisna_oncesi_damga=models.FloatField(verbose_name="Eylül İstisna Öncesi Damga",default=0)
    eylul_vergi_matrahi=models.FloatField(verbose_name="Eylül Vergi Matrahi",default=0)
    eylul_asgari_vergi=models.FloatField(verbose_name="Eylül Asgari Vergi",default=0)
    eylul_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Eylül Asgari Gelir Vergisi İstisnası",default=0)
    eylul_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Eylül Asgari Damga Vergisi İstisnası",default=0)
    eylul_damga_vergisi=models.FloatField(verbose_name="Eylül Damga Vergisi",default=0)
    eylul_gelir_vergisi=models.FloatField(verbose_name="Eylül Gelir Vergisi",default=0)
    eylul_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Eylül Gelir Vergisi İstisnası",default=0)
    eylul_damga_vergisi_istisnasi=models.FloatField(verbose_name="Eylül Damga Vergisi İstisnası",default=0)
    eylul_net_ucret=models.FloatField(verbose_name="Eylül Net Ücret",default=0)
    eylul_isveren_sgk_kesintisi=models.FloatField(verbose_name="Eylül İşveren SGK Kesintisi",default=0)
    eylul_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Eylül İşveren İşsizlik Kesintisi",default=0)
    eylul_toplam_sgk_kesintisi=models.FloatField(verbose_name="Eylül Toplam SGK Kesintisi",default=0)
    eylul_toplam_maliyet=models.FloatField(verbose_name="Eylül Toplam Maliyet",default=0)
    eylul_sgk_istisnasi=models.FloatField(verbose_name="Eylül SGK İstisnası",default=0)
    eylul_odenecek_sgk=models.FloatField(verbose_name="Eylül Ödenecek SGK",default=0)
    eylul_odenecek_gelir_vergisi=models.FloatField(verbose_name="Eylül Ödenecek Gelir Vergisi",default=0)
    eylul_odenecek_damga_vergisi=models.FloatField(verbose_name="Eylül Ödenecek Damga Vergisi",default=0)
    eylul_kanun_no=models.CharField(max_length=50,verbose_name="Eylül Kanun No",default="pick1")
    ekim_brut=models.FloatField(verbose_name="Ekim Brüt",default=0)
    ekim_calisilan_gun=models.FloatField(verbose_name="Ekim Çalışılan Gün",default=0)
    ekim_arge_gun=models.FloatField(verbose_name="Ekim Arge Günü",default=0)
    ekim_bordroyaesasbrut=models.FloatField(verbose_name="Ekim Bordro Yasağa Esas Brüt",default=0)
    ekim_sgk_matrahi=models.FloatField(verbose_name="Ekim SGK Matrahi",default=0)
    ekim_sgk_kesintisi=models.FloatField(verbose_name="Ekim SGK Kesintisi",default=0)
    ekim_issizlik_kesintisi=models.FloatField(verbose_name="Ekim İşsizlik Kesintisi",default=0)
    ekim_kumulatif_asgari_ucret=models.FloatField(verbose_name="Ekim Kumulatif Asgari Vergi",default=0)
    ekim_kumulatif_vergi=models.FloatField(verbose_name="Ekim Kumulatif Vergi",default=0)
    ekim_vergi_dilimi=models.CharField(max_length=50,verbose_name="Ekim Vergi Dilimi",default=0)
    ekim_istisna_oncesi_gelir=models.FloatField(verbose_name="Ekim İstisna Öncesi Gelir",default=0)
    ekim_istisna_oncesi_damga=models.FloatField(verbose_name="Ekim İstisna Öncesi Damga",default=0)
    ekim_vergi_matrahi=models.FloatField(verbose_name="Ekim Vergi Matrahi",default=0)
    ekim_asgari_vergi=models.FloatField(verbose_name="Ekim Asgari Vergi",default=0)
    ekim_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Ekim Asgari Gelir Vergisi İstisnası",default=0)
    ekim_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Ekim Asgari Damga Vergisi İstisnası",default=0)
    ekim_damga_vergisi=models.FloatField(verbose_name="Ekim Damga Vergisi",default=0)
    ekim_gelir_vergisi=models.FloatField(verbose_name="Ekim Gelir Vergisi",default=0)
    ekim_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Ekim Gelir Vergisi İstisnası",default=0)
    ekim_damga_vergisi_istisnasi=models.FloatField(verbose_name="Ekim Damga Vergisi İstisnası",default=0)
    ekim_net_ucret=models.FloatField(verbose_name="Ekim Net Ücret",default=0)
    ekim_isveren_sgk_kesintisi=models.FloatField(verbose_name="Ekim İşveren SGK Kesintisi",default=0)
    ekim_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Ekim İşveren İşsizlik Kesintisi",default=0)
    ekim_toplam_sgk_kesintisi=models.FloatField(verbose_name="Ekim Toplam SGK Kesintisi",default=0)
    ekim_toplam_maliyet=models.FloatField(verbose_name="Ekim Toplam Maliyet",default=0)
    ekim_sgk_istisnasi=models.FloatField(verbose_name="Ekim SGK İstisnası",default=0)
    ekim_odenecek_sgk=models.FloatField(verbose_name="Ekim Ödenecek SGK",default=0)
    ekim_odenecek_gelir_vergisi=models.FloatField(verbose_name="Ekim Ödenecek Gelir Vergisi",default=0)
    ekim_odenecek_damga_vergisi=models.FloatField(verbose_name="Ekim Ödenecek Damga Vergisi",default=0)
    ekim_kanun_no=models.CharField(max_length=50,verbose_name="Ekim Kanun No",default="pick1")
    kasim_brut=models.FloatField(verbose_name="Kasım Brüt",default=0)
    kasim_calisilan_gun=models.FloatField(verbose_name="Kasım Çalışılan Gün",default=0)
    kasim_arge_gun=models.FloatField(verbose_name="Kasım Arge Günü",default=0)
    kasim_bordroyaesasbrut=models.FloatField(verbose_name="Kasım Bordro Yasağa Esas Brüt",default=0)
    kasim_sgk_matrahi=models.FloatField(verbose_name="Kasım SGK Matrahi",default=0)
    kasim_sgk_kesintisi=models.FloatField(verbose_name="Kasım SGK Kesintisi",default=0)
    kasim_issizlik_kesintisi=models.FloatField(verbose_name="Kasım İşsizlik Kesintisi",default=0)
    kasim_kumulatif_asgari_ucret=models.FloatField(verbose_name="Kasım Kumulatif Asgari Vergi",default=0)
    kasim_kumulatif_vergi=models.FloatField(verbose_name="Kasım Kumulatif Vergi",default=0)
    kasim_vergi_dilimi=models.CharField(max_length=50,verbose_name="Kasım Vergi Dilimi",default=0)
    kasim_istisna_oncesi_gelir=models.FloatField(verbose_name="Kasım İstisna Öncesi Gelir",default=0)
    kasim_istisna_oncesi_damga=models.FloatField(verbose_name="Kasım İstisna Öncesi Damga",default=0)
    kasim_vergi_matrahi=models.FloatField(verbose_name="Kasım Vergi Matrahi",default=0)
    kasim_asgari_vergi=models.FloatField(verbose_name="Kasım Asgari Vergi",default=0)
    kasim_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Kasım Asgari Gelir Vergisi İstisnası",default=0)
    kasim_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Kasım Asgari Damga Vergisi İstisnası",default=0)
    kasim_damga_vergisi=models.FloatField(verbose_name="Kasım Damga Vergisi",default=0)
    kasim_gelir_vergisi=models.FloatField(verbose_name="Kasım Gelir Vergisi",default=0)
    kasim_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Kasım Gelir Vergisi İstisnası",default=0)
    kasim_damga_vergisi_istisnasi=models.FloatField(verbose_name="Kasım Damga Vergisi İstisnası",default=0)
    kasim_net_ucret=models.FloatField(verbose_name="Kasım Net Ücret",default=0)
    kasim_isveren_sgk_kesintisi=models.FloatField(verbose_name="Kasım İşveren SGK Kesintisi",default=0)
    kasim_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Kasım İşveren İşsizlik Kesintisi",default=0)
    kasim_toplam_sgk_kesintisi=models.FloatField(verbose_name="Kasım Toplam SGK Kesintisi",default=0)
    kasim_toplam_maliyet=models.FloatField(verbose_name="Kasım Toplam Maliyet",default=0)
    kasim_sgk_istisnasi=models.FloatField(verbose_name="Kasım SGK İstisnası",default=0)
    kasim_odenecek_sgk=models.FloatField(verbose_name="Kasım Ödenecek SGK",default=0)
    kasim_odenecek_gelir_vergisi=models.FloatField(verbose_name="Kasım Ödenecek Gelir Vergisi",default=0)
    kasim_odenecek_damga_vergisi=models.FloatField(verbose_name="Kasım Ödenecek Damga Vergisi",default=0)
    kasim_kanun_no=models.CharField(max_length=50,verbose_name="Kasım Kanun No",default="pick1")
    aralik_brut=models.FloatField(verbose_name="Aralık Brüt",default=0)
    aralik_calisilan_gun=models.FloatField(verbose_name="Aralık Çalışılan Gün",default=0)
    aralik_arge_gun=models.FloatField(verbose_name="Aralık Arge Günü",default=0)
    aralik_bordroyaesasbrut=models.FloatField(verbose_name="Aralık Bordro Yasağa Esas Brüt",default=0)
    aralik_sgk_matrahi=models.FloatField(verbose_name="Aralık SGK Matrahi",default=0)
    aralik_sgk_kesintisi=models.FloatField(verbose_name="Aralık SGK Kesintisi",default=0)
    aralik_issizlik_kesintisi=models.FloatField(verbose_name="Aralık İşsizlik Kesintisi",default=0)
    aralik_kumulatif_asgari_vergi=models.FloatField(verbose_name="Aralık Kumulatif Asgari Vergi",default=0)
    aralik_kumulatif_ucret=models.FloatField(verbose_name="Aralık Kumulatif Vergi",default=0)
    aralik_vergi_dilimi=models.CharField(max_length=50,verbose_name="Aralık Vergi Dilimi",default=0)
    aralik_istisna_oncesi_gelir=models.FloatField(verbose_name="Aralık İstisna Öncesi Gelir",default=0)
    aralik_istisna_oncesi_damga=models.FloatField(verbose_name="Aralık İstisna Öncesi Damga",default=0)
    aralik_vergi_matrahi=models.FloatField(verbose_name="Aralık Vergi Matrahi",default=0)
    aralik_asgari_vergi=models.FloatField(verbose_name="Aralık Asgari Vergi",default=0)
    aralik_asgari_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Aralık Asgari Gelir Vergisi İstisnası",default=0)
    aralik_asgari_damga_vergisi_istisnasi=models.FloatField(verbose_name="Aralık Asgari Damga Vergisi İstisnası",default=0)
    aralik_damga_vergisi=models.FloatField(verbose_name="Aralık Damga Vergisi",default=0)
    aralik_gelir_vergisi=models.FloatField(verbose_name="Aralık Gelir Vergisi",default=0)
    aralik_gelir_vergisi_istisnasi=models.FloatField(verbose_name="Aralık Gelir Vergisi İstisnası",default=0)
    aralik_damga_vergisi_istisnasi=models.FloatField(verbose_name="Aralık Damga Vergisi İstisnası",default=0)
    aralik_net_ucret=models.FloatField(verbose_name="Aralık Net Ücret",default=0)
    aralik_isveren_sgk_kesintisi=models.FloatField(verbose_name="Aralık İşveren SGK Kesintisi",default=0)
    aralik_isveren_issizlik_kesintisi=models.FloatField(verbose_name="Aralık İşveren İşsizlik Kesintisi",default=0)
    aralik_toplam_sgk_kesintisi=models.FloatField(verbose_name="Aralık Toplam SGK Kesintisi",default=0)
    aralik_toplam_maliyet=models.FloatField(verbose_name="Aralık Toplam Maliyet",default=0)
    aralik_sgk_istisnasi=models.FloatField(verbose_name="Aralık SGK İstisnası",default=0)
    aralik_odenecek_sgk=models.FloatField(verbose_name="Aralık Ödenecek SGK",default=0)
    aralik_odenecek_gelir_vergisi=models.FloatField(verbose_name="Aralık Ödenecek Gelir Vergisi",default=0)
    aralik_odenecek_damga_vergisi=models.FloatField(verbose_name="Aralık Ödenecek Damga Vergisi",default=0)
    aralik_kanun_no=models.CharField(max_length=50,verbose_name="Aralık Kanun No",default="pick1")
    class Meta:
        verbose_name_plural="Bordrolar"



class maintence(models.Model):
    maintence=models.BooleanField(("Bakım"),default=False)
    class Meta:
        verbose_name_plural="Bakım"
