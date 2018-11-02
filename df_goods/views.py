from django.shortcuts import render
from django.http import HttpResponse
from df_goods.models import TypeInfo

# Create your views here.

def index(request):

    return render(request, "goods_template/index.html")



def cart(request):
    return  render(request, 'goods_template/cart.html')


def test(request):


    return render(request, "goods_template/test.html")

