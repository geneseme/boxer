"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from kombi.views import IndexView, RegisterView
from kombi.api import DeliveryResource

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^register/$', RegisterView.as_view(), name='login'),
    url(r'^signin/$', RedirectView.as_view(url="/"), name='signin'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"), name='login'),
    url(r'kombi/deliveries$', DeliveryResource.as_list(), name="kombi_deliveries"),
    url(r'kombi/deliveries/(?P<pk>\d+)$', DeliveryResource.as_detail(), name="kombi_delivery"),
]
