# Generated by Django 4.1.1 on 2022-12-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_sirket_sirket_tur'),
    ]

    operations = [
        migrations.CreateModel(
            name='sgkisyeri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgk_isyeri_adi', models.CharField(max_length=50, verbose_name='SGK İşyeri Adı')),
                ('sgk_isyeri_acilis_tarihi', models.DateField(verbose_name='SGK İşyeri Açılış Tarihi')),
                ('sgk_isyeri_sicil_no', models.CharField(max_length=50, verbose_name='SGK İşyeri Sicil Numarası')),
                ('sgk_isyeri_sifre', models.CharField(max_length=50, verbose_name='SGK İşyeri Şifresi')),
                ('sgk_isyeri_kodu', models.CharField(max_length=50, verbose_name='SGK İşyeri Kodu')),
                ('sgk_isyeri_adres_no', models.CharField(max_length=50, verbose_name='SGK İşyeri Adres Numarası')),
                ('sgk_isyeri_mulk', models.CharField(max_length=50, verbose_name='SGK İşyeri Mülkiyeti')),
            ],
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi1',
            field=models.IntegerField(default=0, verbose_name='Ocak'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi10',
            field=models.IntegerField(default=0, verbose_name='Ekim'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi11',
            field=models.IntegerField(default=0, verbose_name='Kasım'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi12',
            field=models.IntegerField(default=0, verbose_name='Aralık'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi2',
            field=models.IntegerField(default=0, verbose_name='Şubat'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi3',
            field=models.IntegerField(default=0, verbose_name='Mart'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi4',
            field=models.IntegerField(default=0, verbose_name='Nisan'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi5',
            field=models.IntegerField(default=0, verbose_name='Mayıs'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi6',
            field=models.IntegerField(default=0, verbose_name='Haziran'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi7',
            field=models.IntegerField(default=0, verbose_name='Temmuz'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi8',
            field=models.IntegerField(default=0, verbose_name='Haziran'),
        ),
        migrations.AddField(
            model_name='maas',
            name='gunsayisi9',
            field=models.IntegerField(default=0, verbose_name='Eylül'),
        ),
    ]
