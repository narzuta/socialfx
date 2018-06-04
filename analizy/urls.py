from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('analizy/', views.analiza_list, name='analizy_list'),
    re_path(r'^analiza/(?P<pk>\d+)/$', views.analiza_detail, name='analiza_detail'),
]