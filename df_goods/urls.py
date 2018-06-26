from django.conf.urls import include, url
from df_goods import views

urlpatterns = [
    url(r'^cart$', views.cart),
    #url(r'^test$', views.test),
    url(r'^', views.index),

]

