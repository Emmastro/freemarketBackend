from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from Accounts.models import UserALAMAU
import os

class Command(BaseCommand):
    """"""

    def handle(self, *args, **options):
        """"""
        for i in range(10):

            user = UserALAMAU(username='Demo{}'.format(i))
                
            user.set_password("Demo")

            user.save()