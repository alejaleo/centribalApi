from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Article

class articleView(View):
    #por favor revisar si con token ingresa
    """ def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) """
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)    
        
    
    def get(self, request, id=0):
        try:
            if(id>0):
                articles=list(Article.objects.filter(id=id).values())
                if len(articles)>0:
                    res=articles[0]
                    data={
                        'articles':res
                        }
                else:
                    data={
                        'message':"No article found"
                    }
                return JsonResponse(data)
            else:                
                articles = list(Article.objects.values())
                if len(articles)>0:
                    data={
                        'articles':articles
                        }
                else:
                    data={
                        'message':"No articles found"
                        }
                return  JsonResponse(data)
        except Exception as e:
            print ("Error when querying articles: ",e)
            
            
        
    def post (self, request):
        jsonData=json.loads(request.body)
        try:
            if len(jsonData)==5:
                Article.objects.create(
                    reference=jsonData['reference'],
                    name=jsonData['name'],
                    description=jsonData['description'],
                    priceWithOutTaxes=jsonData['priceWithOutTaxes'],
                    taxes=jsonData['taxes']
                )
                data={
                    'message':'Article created successfully'
                }
                return JsonResponse(data)
            else:
                data={
                    'message':'fill out fields please!'
                }
                return JsonResponse(data)
        except Exception as e:
            print ("Error creating articles: ",e)
            return JsonResponse({'error': 'Error creating articles'}, status=500)
            
            
    def put (selft,request, id):
        jsonData=json.loads(request.body)
        try:
            if len(jsonData)==5:
                articles=list(Article.objects.filter(id=id).values())
                if len(articles)>0:
                    res=Article.objects.get(id=id)
                    res.reference=jsonData['reference']
                    res.name=jsonData['name']
                    res.description=jsonData['description']
                    res.priceWithOutTaxes=jsonData['priceWithOutTaxes']
                    res.taxes=jsonData['taxes']
                    res.save()
                    data={
                        "message":"Article successfully updated"
                    }
                else:
                    data={
                        "message":"No article found"
                    }
            else:
                data={
                    "message":"No article found"
                }
            return JsonResponse(data)
        except Exception as e:
            print ("Error updated articles: ",e)
    
    
    def delete(self,request,id):
        try:
            articles=list(Article.objects.filter(id=id).values())
            if len(articles)>0:
                Article.objects.filter(id=id).delete()
                data={
                    "message":"Article successfully deleted"
                }
            else:
                data={
                    "message":"No article found"
                }
            return JsonResponse(data)
        except Exception as e:
            print ("Error deleted articles: ",e)
            return JsonResponse({'error': 'Error deleted articles'})
        