from .models import*

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
