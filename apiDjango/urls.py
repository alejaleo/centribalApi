from django.urls import path

from .views.article_view import articleView
from.views.order_view import orderView


urlpatterns=[
    path("articles/", articleView.as_view()),
    path("articles/<int:id>", articleView.as_view()),
    path("orders/", orderView.as_view()),  
    path("orders/<int:id>", orderView.as_view()),
]
