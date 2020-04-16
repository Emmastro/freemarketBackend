from django.urls import path
from django.conf.urls import include
from . import views
from .views import *

urlpatterns = [
path('cat/', CategoryListView.as_view()),
path('sellers/<str:category>/', SellersListView.as_view())
]
