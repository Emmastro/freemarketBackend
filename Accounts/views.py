from .models import*

from Accounts.models import UserALAMAU

from django.core.mail import send_mail

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from django.db.models import Q, F # Grouping for book suggestions


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here




class UserView(APIView):
    """
 Retrieve, update or delete a customer by id/pk.
 """

    def get(self, request, username):

        try:
            user = UserALAMAU.objects.get(username=username)
        except UserALAMAU.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user,context={'request': request})
        return Response(serializer.data)
    
    def put(self, request):

        pass 

    def delete(self, request):

        pass