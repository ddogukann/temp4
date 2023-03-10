# Generated by Django 4.1.1 on 2022-11-25 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_mali_musavir_mali_musavir_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='agustos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Ağustos Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='aralik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Aralık Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='ekim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Ekim Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='eylul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Eylül Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='haziran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Haziran Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='kasim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Kasım Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='mart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Mart Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='mayis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Mayıs Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='nisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Nisan Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='ocak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Ocak Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='subat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Şubat Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='temmuz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brut', models.FloatField(default=0, verbose_name='Temmuz Brüt')),
            ],
        ),
        migrations.CreateModel(
            name='bordro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.maas', verbose_name='Maaş ID')),
            ],
        ),
    ]
