from .models import*

import datetime 

from rest_framework.response import Response
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class UpdatesView(APIView):
    """
 Return all the Update items, or create a Update
 """
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):

        data = []
        nextPage = 1
        previousPage = 1
        Updates = Update.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(Updates, 5) # Send 5 Update items at a time
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = UpdateSerializer(data,context={'request': request} ,many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/update/?page=' + str(nextPage), 'prevlink': '/api/update/?page=' + str(previousPage)})
   
    def post(request):

        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(APIView):
    """
 Retrieve, update or delete a customer by id/pk.
 """

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        try:
            Update = Update.objects.get(pk=pk)
        except Update.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = UpdateSerializer(Update,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            Update = Update.objects.get(pk=pk)
        except Update.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = UpdateSerializer(Update, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        try:
            Update = Update.objects.get(pk=pk)
        except Update.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        Update.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventsView(APIView):
    """
 Return all the Event items, or create a Event
 """
    
    #permission_classes = (IsAuthenticated,)
    
    def get(self, request):

        data = []
        nextPage = 1
        previousPage = 1
        Events = Event.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(Events, 5) # Send 5 Event items at a time
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = EventSerializer(data,context={'request': request} ,many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/Update/?page=' + str(nextPage), 'prevlink': '/api/Update/?page=' + str(previousPage)})

    def post(self, request):

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventView(APIView):
    """
 Retrieve, event or delete a customer by id/pk.
 """

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        try:
            Event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(Event,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            Event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(Event, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class BusSchedulesView(APIView):
    """Return all the Event items, or create a Event"""

    #permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        data = []
        nextPage = 1
        previousPage = 1
        busSchedules = BusSchedule.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(busSchedules, 5) # Send 5 Event items at a time
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = BusScheduleSerializer(data,context={'request': request} ,many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/Update/?page=' + str(nextPage), 'prevlink': '/api/Update/?page=' + str(previousPage)})

    def post(self, request):
        serializer = BusScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusScheduleView(APIView):
    """
 Retrieve, event or delete a customer by id/pk.
 """

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        try:
            BusSchedule = BusSchedule.objects.get(pk=pk)
        except BusSchedule.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BusScheduleSerializer(BusSchedule,context={'request': request})
        return Response(serializer.data)

    def post(self, request, pk):
        
        try:
            BusSchedule = BusSchedule.objects.get(pk=pk)
        except BusSchedule.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BusScheduleSerializer(BusSchedule, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            BusSchedule = BusSchedule.objects.get(pk=pk)
        except BusSchedule.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        BusSchedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CalendarView(APIView):
    """
 Return all the Event items, or create a Event
 """

    #permission_classes = (IsAuthenticated,)
    
    def get(self, request):

        data = []
        nextPage = 1
        previousPage = 1
        schedule = Schedule.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(schedule, 5) # Send 5 Event items at a time
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ScheduleSerializer(data,context={'request': request} ,many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/Update/?page=' + str(nextPage), 'prevlink': '/api/Update/?page=' + str(previousPage)})

    def post(self, request):
        
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationsView(APIView):


    def get(self, request):
        data = []
        nextPage = 1
        previousPage = 1
        user = UserALAMAU.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(user, 5) # Send 5 Event items at a time
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = NotificationSerializer(data,context={'request': request} ,many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/Updatenotification/?page=' + str(nextPage), 'prevlink': '/api/notification/?page=' + str(previousPage)})

class NotificationView(APIView):
    """
 Return all the Event items, or create a Event
 """

    #permission_classes = (IsAuthenticated,)
    
    def get(self, request):

        try:
            notification = UserALAMAU.objects.get(username=request.GET.get("username", "Demo0"))
        except UserALAMAU.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NotificationSerializer(notification,context={'request': request})
        return Response(serializer.data)


    def put(self, request):
        # get or update a model
        #username = request.POST["username"]
        
        #token = request.POST["token"]

        notification = UserALAMAU.objects.get(username=request.POST.get("username", "Demo0"))
       
        serializer = NotificationSerializer(notification, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)