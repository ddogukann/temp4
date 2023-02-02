# Generated by Django 4.1.1 on 2023-01-20 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0051_delete_maintence_remove_bordro_agustos_kanun_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='subs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs_sirket_adi', models.CharField(max_length=50, verbose_name='Şirket Adı')),
                ('subs_aktiflik', models.BooleanField(default=True, verbose_name='Şirket Aktiflik Durumu')),
                ('subs_baslangic_tarihi', models.DateField(verbose_name='Şirket Başlangıç Tarihi')),
                ('subs_maksimum_calisan', models.IntegerField(verbose_name='Şirket Maksimum Çalışan Sayısı')),
                ('subs_gun_sayisi', models.IntegerField(verbose_name='Paket Gün Sayısı')),
            ],
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Ağustos Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Aralık Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Ekim Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Eylül Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Haziran Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Kasım Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Mart Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Mayıs Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Nisan Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Ocak Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Şubat Kanun No'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_kanun_no',
            field=models.CharField(default='pick1', max_length=50, verbose_name='Temmuz Kanun No'),
        ),
        migrations.AddField(
            model_name='sirket',
            name='sirket_uyelik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='user.subs', verbose_name='Şirket Üyelik Paketi'),
        ),
    ]
