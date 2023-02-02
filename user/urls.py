from django.contrib import admin
from django.urls import path,include
from. import views
from django.conf.urls.static import static
from django.conf import settings

app_name='user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.index, name='homepage'),
    path('companyregister/', views.companyregister, name='companyregister'),
    path('companys/', views.listcompany, name='listcompany'),
    path('companys/<int:id>', views.detailcompany, name='detailcompany'),
    path('companys/<int:id>/addemp', views.calisanregister, name='calisanregister'),
    path('companys/<int:id>/listemp', views.listemployee, name='employeelist'),
    path('listemp/<int:id>', views.detailemployee, name='employeedetail'),
    path('addmaas/<int:id>', views.addmaas, name='addmaas'),
    path('maasdetail/<int:id>/<int:year>', views.maasdetail, name='maasdetail'),
    path('maasupdate/<int:id>/<int:maasid>',views.update_maas,name='maasupdate'),
    path('updatebymonth/<int:id>/<int:maasid>/<str:month>',views.updatebymonth,name='updatebymonth'),
    path('updateemp/<int:id>',views.update_emp,name='updateemp'),
    path('updatecompany/<int:id>',views.companyupdate,name='updatecompany'),
    path('registertype/', views.select_register_type, name='registertype'),
    path('registerwcomp/', views.register_with_company, name='register1'),
    path('senddatabase/<int:id>/<int:year>', views.getlist, name='senddatabase'),
    path("searche/<int:id>/",  views.searchemp, name="search"),
    path("searchc/",  views.searchcomp, name="searchc"),
    path("createpdf/<int:id>",  views.createpdf, name="pdf"),
    path("subelist/<int:id>",  views.listsube, name="subelist"),
    path("passemp/<int:id>",  views.passiveemployee, name="passiveemployee"),
    path("subelist/<int:id>/addsube",  views.suberegister, name="addsube"),
    path("updatesube/<int:id>",  views.updatesube, name="updatesube"),
    path("mycompany/",  views.list_malisirket_detail, name="malisirketdetail"),
    path("mycompany/addemp",  views.addmalimusavir, name="addmalimusavir"),
    path("checkusername/",  views.checkusername, name="checkusername"),
    path("addcompwurl/<slug:slug>",  views.addcompwithurl, name="addcompwithurl"),

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'user.views.handler404'