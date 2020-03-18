from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import UserALAMAU


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserALAMAU
        fields = ('username', 'first_name', 'last_name', 'exploreJoburg') 
