from django.core.management.base import BaseCommand
from Main.models import*
from django.contrib.auth import get_user_model

User = get_user_model()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #so firstly there are two users, and one category
        for i in range(0,5):
            user = User.objects.get(username = str(i))
            user.username = "Tani_"+str(i)
            user.save()
