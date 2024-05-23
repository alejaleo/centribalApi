import requests
import random

ENDPOINT = "http://127.0.0.1:8000/articles/"
idArticle = 0
products = [
    {'reference': '111111' , 'name' : 'articulo 1' , 'description' : 'description articulo 1'},
    {'reference': '121212' , 'name' : 'articulo 2' , 'description' : 'description articulo 2'},
    {'reference': '131313' , 'name' : 'articulo 3'  , 'description': 'description articulo 3'},
    {'reference': '141414' , 'name' : 'articulo 4' , 'description' : 'description articulo 4'},
    {'reference': '151515' , 'name' : 'articulo 5' , 'description' : 'description articulo 5'},
    {'reference': '161616' , 'name' : 'articulo 6'  , 'description': 'description articulo 6'}
]
class TestArticleView:

    #test para crear un articulo con todos los datos requeridos
    def test_postArticle(self):
        for product in products:
            data = {
                "reference": product['reference'],
                "name": product['name'],
                "description": product['description'],
                "priceWithOutTaxes": str(random.randint(10000,20000))+".00",
                "taxes": str(random.randint(1000,5000))+".10"
            }
            res = requests.post(ENDPOINT, json = data)
            assert res.status_code == 200
            assert res.json() == {'message' : 'Article created successfully'}
    
    #test para crear un articulo sin todos los datos requeridos
    def test_postArticleIncomplete(self):
        data = {
            "reference": "171717",
            "name": "articulo 7",
            "description": "descripcion articulo 7",
            "priceWithOutTaxes": "18000.00"
        }
        res = requests.post(ENDPOINT, json = data)
        assert res.status_code == 200 
        assert res.json() == {'message' : 'fill out fields please!'}

    #test para consultar la lista de todos los articulos en la BD y seleccionar el id del ultimo
    def test_getAllArticles(self):
        global idArticle
        res = requests.get(ENDPOINT)
        assert res.status_code == 200
        idArticle = res.json()['articles'][len(res.json()['articles'])-1]['id']

    #test para consultar un articulo de la BD con un id correcto
    def  test_getArticleCorrectId(self):
        res = requests.get(ENDPOINT + str(idArticle))
        assert res.status_code == 200
        assert res.json()["articles"]["id"] == idArticle
        
    #test para consultar un articulo con un id incorrecto
    def test_getArticleIncorrectId (self):
        res = requests.get(ENDPOINT + str(idArticle+1))
        assert res.status_code == 200
        assert res.json() == {'message':"No article found"}

    #test para actualizar un articulo con un id correcto
    def test_putArticle (self):
        data = {
            "reference": "111112",
            "name": "articulo actualizado 1",
            "description": "descripcion articulo actualizado 1",
            "priceWithOutTaxes": 18000.00,
            "taxes": 1500.00
        }
        res = requests.put(ENDPOINT + str(idArticle), json = data)
        assert res.status_code == 200
        assert res.json() == {'message':"Article successfully updated"}

    #test para actualizar un articulo con un id incorrecto
    def test_putArticleIncorrectId (self):
        data = {
            "reference": "121212",
            "name": "articulo actualizado 2",
            "description": "descripcion de articulo actualizado 2",
            "priceWithOutTaxes": 25000.00,
            "taxes": 200.00
        }
        res = requests.put(ENDPOINT + str(idArticle+1), json = data)
        assert res.status_code == 200
        assert res.json() == {'message':'No article found'}
    
    #test para actualizar un articulo con datos faltantes
    def test_putArticleIncomplete (self):
        data = {
            "reference": "131313",
            "name": "articulo actualizado 3",
            "description": "descripcion articulo actualizado 3",
            "priceWithOutTaxes": 30000.00
        }
        res = requests.put(ENDPOINT + str(idArticle), json = data)
        assert res.status_code == 200
        assert res.json() == {'message' : 'No article found'}

    #test para eliminar un articulo con un id correcto
    def test_deleteArticle (self):
        res = requests.delete(ENDPOINT + str(idArticle))
        assert res.status_code == 200
        assert res.json() == {'message':"Article successfully deleted"}

    #test para eliminar un articulo con un id incorrecto
    def test_deleteArticleIncorrectId(self):
        res = requests.delete(ENDPOINT + str(idArticle+1))
        assert res.status_code == 200
        assert res.json() == {'message':"No article found"}


#Se crea un nuevo articulo para agregarlo en los pedidos
article = TestArticleView()
article.test_postArticle()