from . import settings
from django.core.mail import send_mail

from Messaging.models import WeeklyMail
from background_task import background

@background(schedule=5)
def weekly_mail():
	
	send_mail(
		"Registration",
		"""
		You have been registered in the ALA Library.""",#.format('Emma'),
		settings.DEFAULT_FROM_EMAIL,
		recipient_list = ['emurairi18@alastudents.org'])
weekly_mail()