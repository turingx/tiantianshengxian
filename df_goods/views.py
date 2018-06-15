from django.shortcuts import render

# Create your views here.

def index(request):
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0, 4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0, 4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0, 4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0, 4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0, 4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0, 4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0, 4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0, 4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0, 4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0, 4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0, 4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0, 4]

    context = {
        type0:'type0', type01:'type01',
        type1: 'type1', type11: 'type11',
        type2: 'type2', type21: 'type21',
        type3: 'type3', type31: 'type31',
        type4: 'type4', type41: 'type41',
        type5: 'type5', type51: 'type51',
               }
    return render(request, "goods_template/index.html" context)

    print(typelist)
    return render(request, 'goods_template/index.html')

def cart(request):
    return  render(request, 'goods_template/cart.html')
