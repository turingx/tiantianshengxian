from django.conf.urls import include, url
from df_user import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^register_handle$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login_handle$', views.login_handle),
    url(r'^user_center$', views.user_center),
    url(r'^order$', views.order),
    url(r'^site$', views.site),
]

