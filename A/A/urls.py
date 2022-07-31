"""A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.urls import path , include
from django.conf.urls.static import static
from articles.views import (IndexView ,RetrieveView)
from django.views.generic.base import TemplateView  
from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('bankgateways/', az_bank_gateways_urls()),
    path('<int:id>/',RetrieveView.as_view(),name ='Retrieve'),
    path('',IndexView.as_view(),name ='Home'),
    path("accounts/", include("accounts.urls")), 
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="layout.html"), name="home"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)