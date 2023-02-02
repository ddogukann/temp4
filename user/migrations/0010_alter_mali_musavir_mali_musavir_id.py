# Generated by Django 4.1.1 on 2022-11-22 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0009_mali_musavir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mali_musavir',
            name='mali_musavir_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Mali Müşavir ID'),
        ),
    ]