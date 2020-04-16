from .models import*

import datetime

from rest_framework.response import Response
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CategoryListView(APIView):

    def get(self, request):
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

class SellersListView(APIView): #list all the sellers by category

    def get(self, request, category):
        cat = Category.objects.get(name = category)
        seller_list = Seller.objects.filter(category = cat)
        serializer = SellerSerializer(seller_list, many=True)
        return Response(serializer.data)
