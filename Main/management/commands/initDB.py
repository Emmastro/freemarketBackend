# 1st command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from Main.models import*

import json

import os


class Command(BaseCommand):
    """Closes the specified poll for voting"""
    # def add_arguments(self, parser):
    #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        """	Initialise the Database with Libraries names,
        shelfs and shelf steps"""


        with open(os.path.join(settings.BASE_DIR,'initData.json')) as f:
            Data = json.load(f)
        
        self.initCalendar(Data["calendar"])
        
    def initCalendar (self, data):
        
        for day in data:
            
            schedule = Schedule.objects.create(date=day['date'])
            
            for ds in day["dailySchedule"]:

                dailySchedule = DailySchedule.objects.create(
                    start_time=ds["start_time"],
                    end_time=ds["end_time"],
                    title=ds['title'])

                schedule.dailySchedule.add(dailySchedule)
                dailySchedule.save()
                
            
            schedule.save()