from django.conf.urls import include, url
from df_goods import views

urlpatterns = [
    url(r'^', views.index),
]

