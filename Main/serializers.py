from rest_framework import serializers
from .models import *
from Accounts.serializers import UserSerializer


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Update
        fields = ('pk','title', 'content', 'category', 'url')

class EventSerializer(serializers.ModelSerializer):
    # Should return a flag to check if the user signed up for the event 
    # --> Check if user is in participants
    # A user can signup for only one event
    
    class Meta:
        model = Event
        fields = ('pk','title', 'content', 'dressCode','image', 'venue', 'star_time', 'end_time' )

class BusScheduleSerializer(serializers.ModelSerializer):
    
    chaperone = UserSerializer(many=True, read_only=True)

    class Meta:
        model = BusSchedule
        fields = ('pk','start', 'destination', 'chaperone', 'departureTime', 'arrivalTime', 'busNumber', 'date' )

class DailyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySchedule
        fields = ['pk', 'start_time', 'end_time', 'title']
        
class ScheduleSerializer(serializers.ModelSerializer):
    
    dailySchedule = DailyScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ('pk', 'date', 'dailySchedule')

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserALAMAU
        fields = ('username','notification_token')