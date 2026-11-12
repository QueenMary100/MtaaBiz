from django.contrib import admin
from django.urls import path

# from myapp.views import blog, details, error, details, index, portfolio, services, starter, services, portfolio, show, delete,edit
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404/', error, name='error'),
    path('details/', details, name='details'),
    path('blog/', blog, name='blog'),
    path('', index, name='index'),   
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('starter/', starter, name='starter'),
    path('show/', show, name= 'show'),

    #make url for delete function, no need for name attribute since its not an html page or attribute
    path('delete/<int:id>', delete),
    path('edit/<int:id>/', edit),
]
