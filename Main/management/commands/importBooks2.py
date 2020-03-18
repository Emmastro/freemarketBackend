""" 
Import:
   User data
   Calendar events
   Blog articles
   
   Sample notifications
   Sample messages
   Sample Youtube videos (links or streams)

"""



import json
import os

# us a fonction to convert a list in a string format to a python list
import ast  
import pandas as pd

from django.conf import settings

from Main.models import*
from Accounts.models import*

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from django.core.files.base import ContentFile
from PIL import Image

from io import BytesIO

import datetime


class Command(BaseCommand):
    """Closes the specified poll for voting"""
    #def add_arguments(self, parser):
    #    parser.add_argument('excelDB', type=str)
    #    parser.add_argument('pictures', type=str)

    def handle(self, *args, **options):
        """
        Import the books data from an Excel file and a cover folder
        The index is the nomber of books to import
        """
        
        file = os.path.join(settings.BASE_DIR,'data.xlsx')
        pictures = os.path.join(settings.BASE_DIR,'pictures')

        user_profiles = pd.read_excel(files, sheet_name="users")

        # Fill out missing data
        datas['Number'].where(pd.notna(datas['Number']), 1, True)
        datas['Subtitle'].where(pd.notna(datas['Subtitle']), '', True)
        datas['Description'].where(pd.notna(datas['Description']), '', True)

        Author.objects.get_or_create(username='Unknown')

        # Try creating unknown publisher if it's the first import
        Publisher.objects.get_or_create(name = "Unknown")

        for i in range(10):
            
            user = User_ALAMAU.objects.get_or_create(
                    username = user_profiles['username'][i],
                    first_name = user_profiles['first_name'][i],
                    last_name = user_profiles['last_name'][i],
                )

            #Add profile image
            try:
                image_name = user_profiles['picture'][i]
                cover = Image.open(
                    pictures+'/'+image_name)

                #cover.resize((200,200))
                img = BytesIO()
                cover.save(img, cover.format)
                user.image.save(
                    image_name, 
                    ContentFile(img.getvalue()), save=True)
            except Exception as e:
                print('No profile image')

            user.save()