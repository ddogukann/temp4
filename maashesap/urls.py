from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hesapla', include('app.urls') ,name='app'),
    path('', include('user.urls'),name='user'),
]
handler404 = 'user.views.handler404'