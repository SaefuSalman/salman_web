from django.contrib import admin
from django.urls import path
from portofolio_web.views import HalamanUtama

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halaman_utama/', HalamanUtama, name='HalamanUtama')
]
