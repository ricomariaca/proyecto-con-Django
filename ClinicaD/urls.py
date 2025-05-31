from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinicaApp.urls')),  # 👈 Solo incluye el archivo de la app
]
