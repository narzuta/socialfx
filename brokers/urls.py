from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('brokers/', views.brokers_list, name='brokers_list'),
    re_path(r'^broker/(?P<pk>\d+)/$', views.broker_detail, name='broker_detail'),
]