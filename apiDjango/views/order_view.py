from decimal import Decimal
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import json

from ..models import Article, Order

class orderView(View):
    #por favor revisar si con token ingresa
    # @method_decorator(csrf_exempt)
    """ def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self, request, id=0):
        try:
            if(id>0):
                orders=list(Order.objects.filter(id=id).values())
                if len(orders)>0:
                    res=orders[0]
                    data={
                        'orders':res
                        }
                else:
                    data={
                        'message':"No order found"
                    }
                return JsonResponse(data)
            else:                
                orders = list(Order.objects.values())
                if len(orders)>0:
                    data={
                        'orders':orders
                        }
                else:
                    data={
                        'message':"No orders found"
                        }
                return  JsonResponse(data)
        except Exception as e:
            print ("Error when querying orders: ",e)
            
            
        
    def post (self, request):
        jsonData=json.loads(request.body)
        priceTotalWithOutTaxes=0
        priceTotalWithTaxes=0
        try:
            if len(jsonData)==1:
                articles_extra=[]
                for x in jsonData['listArticles']:
                    articles=list(Article.objects.filter(reference=x['reference']).values())
                    if(articles==[]):
                        articles_extra.append(x['reference']+" ")
                    else:
                        priceTotalWithOutTaxes += int(articles[0]['priceWithOutTaxes'])* int(x['quantity'])
                        priceTotalWithTaxes += (int(articles[0]['priceWithOutTaxes']) + (int(articles[0]['priceWithOutTaxes'])* (int (articles[0]['taxes'])/100)))*int(x['quantity'])
                if(articles_extra !=[]):
                    data={
                        'message':"the articles are not there "+"".join(articles_extra)
                        }
                else:
                    Order.objects.create(
                        listArticles=jsonData['listArticles'],
                        priceTotalWithOutTaxes=priceTotalWithOutTaxes,
                        priceTotalWithTaxes=priceTotalWithTaxes
                    )
                    data={
                        'message':"Order created"
                        }
            else:
                data={
                    'message':"complete all fields"
                    }
                
                
                
                
            return JsonResponse(data)
        except Exception as e:
            print ("Error creating orders: ",e)
            return JsonResponse({'error': 'Error creating orders'}, status=500)
            
            
            
    def put (selft,request, id):
        jsonData=json.loads(request.body)
        priceTotalWithOutTaxes=0
        priceTotalWithTaxes=0
        try:
            if len(jsonData)==1:
                orders=list(Order.objects.filter(id=id).values())
                if len(orders)>0:
                    res=Order.objects.get(id=id)
                    articles_extra=[]
                    for x in jsonData['listArticles']:
                        articles=list(Article.objects.filter(reference=x['reference']).values())
                        if (articles==[]):
                            articles_extra.append(x['reference']+" ")
                        else:
                            priceTotalWithOutTaxes +=(Decimal(articles[0]['priceWithOutTaxes'])) * int(x['quantity'])
                            priceTotalWithTaxes += (Decimal(articles[0]['priceWithOutTaxes']) + (Decimal(articles[0]['priceWithOutTaxes'])* (Decimal (articles[0]['taxes'])/100)))*int(x['quantity'])
                    if(articles_extra !=[]):
                        data={
                            'message':"it is no possible to update"+"".join(articles_extra)
                            }
                    else:
                        
                        res.listArticles=jsonData['listArticles']
                        res.priceTotalWithOutTaxes=priceTotalWithOutTaxes
                        res.priceTotalWithTaxes=priceTotalWithTaxes
                        res.save()
                        data={
                            'message':"Updated Order"
                            }
                else:
                    data={
                        'message':"complete all fields"
                        }
            else:
                data={
                    'message':"incomplete data"
                    }
            return JsonResponse(data,status=200)
        except Exception as e:
            print ("Error updated orders: ",e)
            return JsonResponse({'error': 'Error updating orders'}, status=500)
    
    def delete(self,request,id):
        try:
            orders=list(Order.objects.filter(id=id).values())
            if len(orders)>0:
                Order.objects.filter(id=id).delete()
                data={
                    "message":"order successfully deleted"
                }
            else:
                data={
                    "message":"No order found"
                }
            return JsonResponse(data)
        except Exception as e:
            print ("Error deleted orders: ",e)
        