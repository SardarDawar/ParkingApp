"""parking_lot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from parking_data.views import All_Cars,car_entered,update_cars,Front_Page
from pdf.views import pdfview
from django.conf import settings
from django.conf.urls.static import static  
urlpatterns = [
    path("",Front_Page),
    path("all_cars/",All_Cars),
    path("enter/<str:slot>/",car_entered),
    path("data/", include('parking_data.urls')),
    path('pdf/',pdfview),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

