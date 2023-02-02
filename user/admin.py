from django.contrib import admin
from .models import sirket,maas,calisan,mali_musavir,bordro,sube,nace,vergidairesi,mali_sirket,subs,maintence,iskur,sgkisyeri
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(sirket)
admin.site.register(maas)
admin.site.register(calisan)
admin.site.register(mali_musavir)
admin.site.register(bordro)
admin.site.register(sube)
admin.site.register(mali_sirket)
admin.site.register(subs)
admin.site.register(maintence)
admin.site.register(iskur)
admin.site.register(sgkisyeri)
@admin.register(nace)
class NaceAdmin(ImportExportModelAdmin):
    list_display = ('nace','nace_aciklama')
    pass
@admin.register(vergidairesi)
class VergidairesiAdmin(ImportExportModelAdmin):
    list_display = ('vd_adi','vd_kodu',"vd_sehir")
    pass