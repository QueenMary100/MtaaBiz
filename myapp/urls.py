from django.contrib import admin
from django.urls import path

from myapp.views import blog, details, error, details, index, portfolio, services, starter, services, portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404/', error, name='error'),
    path('details/', details, name='details'),
    path('blog/', blog, name='blog'),
    path('', index, name='index'),   
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('starter/', starter, name='starter'),
]
