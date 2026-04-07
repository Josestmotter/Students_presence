from django.contrib import admin
from django.urls import path
from home.views import export_csv, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('export/', export_csv, name='export'),
]