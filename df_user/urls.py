from django.conf.urls import include, url
from df_user import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^register_handle$', views.register_handle),
]

