import requests
from apiDjango.models import Article


ENDPOINT = "http://127.0.0.1:8000/orders/"
idOrder = 0
articles = ["111111","121212","131313", "141414", "151515", "161616"]

class TestOrderView:
    
    

    #test para crear un pedido con todos los datos requeridos
    def test_postOrder(self):
        for x in articles:
            if not(Article.objects.filter(reference=x).values() == []):
                articleAdd = x
        data = {            
            "listArticles": [
                {
                "quantity": "3",
                "reference": articleAdd
                }
            ]
        }
        res = requests.post(ENDPOINT, json = data)
        assert res.status_code == 200
        assert res.json() == {'message':  "Order created"}
    
    #test para crear un pedido con articles no creados
    def test_postOrderIncorrect(self):
        data = {            
            "listArticles": [
                {
                "quantity": "3",
                "reference": "12364"
                },
                {
                "quantity": "6",
                "reference": "777"
                }
            ]
        }
        res = requests.post(ENDPOINT, json = data)
        assert res.status_code == 200
        assert res.json()['message'].startswith("the articles are not there ")

    #test para crear un pedido con datos incompletos
    def test_postOrderIncomplete(self):
        data = {}
        res = requests.post(ENDPOINT, json = data)
        assert res.status_code == 200
        assert res.json() == {'message' : 'complete all fields'}

    #test para consultar la lista de todos los orders en la BD y seleccionar el id del ultimo
    def test_getAllOrders (self):
        global idOrder
        res = requests.get(ENDPOINT)
        assert res.status_code == 200
        idOrder = res.json()['orders'][len(res.json()['orders'])-1]['id']

    #test para consultar un pedido de BD con un id correcto
    def test_getOrderId (self):
        res = requests.get(ENDPOINT + str(idOrder))
        assert res.status_code == 200
        assert res.json()['orders']['id'] == idOrder

    #test para consultar un pedido con un id incorrecto
    def test_getOrderIncorrectId (self):
        res = requests.get(ENDPOINT + str(idOrder+1))
        assert res.status_code == 200
        assert res.json() == {'message':"No order found"}

    #test para actualizar un pedido con un id correcto
    def test_putOrderId (self):
        for x in articles:
            if not(Article.objects.filter(reference=x).values() == []):
                ArticleAdd = x
        data = {            
            "listArticles": [
                {
                "quantity": "3",
                "reference": ArticleAdd
                }
            ]
        }
        res = requests.put(ENDPOINT + str(idOrder), json = data)
        assert res.status_code == 200
        assert res.json() == {'message':"Updated Order"}
    
    #test para actualizar un pedido con un id incorrecto
    def test_putOrderIncorrectId (self):
        data = {            
            "listArticles": [
                {
                "quantity": "3",
                "reference": "123"
                }
            ] 
        }
        res = requests.put(ENDPOINT + str(idOrder+1), json = data)
        assert res.status_code == 200
        
        assert res.json() == {'message':"complete all fields"}

    #test para actualizar un pedido con datos faltantes
    def  test_putOrderIncomplete (self):
        data = {}
        res = requests.put(ENDPOINT + str(idOrder), json = data)
        assert res.status_code == 200
        assert res.json() == {'message':"incomplete data"}
    
    #test para eliminar un pedido con un id correcto
    def test_deleteOrderId (self):
        res = requests.delete(ENDPOINT + str(idOrder))
        assert res.status_code == 200
        assert res.json() == {'message':'order successfully deleted'}

    #test para eliminar un pedido con un id incorrecto
    def test_deleteOrderIncorrectId (self):
        res = requests.delete(ENDPOINT + str(idOrder+1))
        assert res.status_code == 200
        assert res.json() == {'message':'No order found'}