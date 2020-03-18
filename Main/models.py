from django.db import models
from django.db.models.signals import post_save
from django_extensions.db.models import TimeStampedModel #A Django model that adds created_at and updated_at fields by default.
from Accounts.models import UserALAMAU
from django.dispatch import receiver

from django.conf import settings

from pyfcm import FCMNotification

class Update(TimeStampedModel):
	"""
	Description: Notification updates for Delegates and other users
	"""
	title = models.CharField(max_length=128)
	content = models.TextField()
	category = models.ForeignKey('UpdateCategory', on_delete=models.CASCADE, null=True, blank=True)
	url = models.URLField(null=True, blank=True) # redirection url

	def __str__(self):
		return self.title

	class Meta:
		
		ordering = ['-pk']

class UpdateCategory(models.Model):
	"""
	Categories to consider:
		-- New article: a click will redirect the user to the article on the website
		-- Late notification: A click will show the text message for the user	
		-- Youtube video (Course, ...): stream on the app

	"""
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Schedule(models.Model):
	""" Conference schedule"""

	date = models.DateField(auto_now_add=False)
	dailySchedule = models.ManyToManyField('Main.DailySchedule')

	class Meta:
		
		ordering = ['pk']

class DailySchedule(models.Model):
	""" """

	start_time = models.TimeField(auto_now_add=False)
	end_time = models.TimeField(auto_now_add=False)
	title = models.CharField(max_length=128)

	class Meta:
		
		ordering = ['pk']
		
class BusSchedule(models.Model):
	""" """
	start = models.CharField(max_length=128)
	destination = models.CharField(max_length=128)
	chaperone = models.ManyToManyField('Accounts.UserALAMAU') # A bus can have more than 1 chaperone
	departureTime = models.TimeField()
	arrivalTime = models.TimeField()
	date = models.DateField()
	busNumber = models.CharField(max_length=128)


	class Meta:
		
		ordering = ['-pk']


class Feed(TimeStampedModel):
	
	title = models.CharField(max_length=128)
	content = models.TextField()
	image = models.ImageField(upload_to="Feed", verbose_name="Feed")
	

class Event(models.Model):
	"""
	Description: appear on the Event feed. List different ALAMAU events
	"""
	title = models.CharField(max_length=128)
	content = models.TextField()

	venue = models.CharField(max_length=128) # Change to a foreign key to include more information
	star_time = models.DateTimeField(auto_now_add=False)
	end_time = models.DateTimeField(auto_now_add=False)
	
	image = models.ImageField(upload_to="event",
		verbose_name="Event", null=True, blank=True)
	
	dressCode = models.CharField(max_length=128)

	class Meta:
		
		ordering = ['-pk']

class School(models.Model):
	""" 
	Description: 
	"""
	name = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100)
	address = models.CharField(max_length=500, null=True, blank=True, default=None)
	postal_code = models.CharField(max_length=5, null=True, blank=True, default=None)

	website = models.CharField(max_length=100, null=True, blank=True, default='None')

	
	def __str__(self):
		return self.name

class InAppMessage(models.Model):
	""" 
	Description : 
	"""

	sender = models.ForeignKey(UserALAMAU, related_name='sent_messages', on_delete=models.CASCADE)
	recipient = models.ForeignKey(UserALAMAU, related_name='received_messages', on_delete=models.CASCADE)
	content = models.CharField(max_length=512)

	class Meta:
		
		ordering = ['-pk']

@receiver(post_save, sender=InAppMessage)
def sendNewMessageNotification(sender, **kwargs):
	""" 
	Description: 
	"""
	message = kwargs['instance'] # Retrieve the message that has been saved
	sendNewMessagePushNotification(sender_id=message.sender.id,
									   recipient_id=message.recipient.id,
									   content=message.content)
	class Meta:
		
		ordering = ['-pk']
		
@receiver(post_save, sender=Update)
def sendUpdateNotification(**kwargs):

	""" Update notification is sent to every users that accept notifications"""
	instance = kwargs['instance']

	push_service = FCMNotification(api_key="AIzaSyBdxS0kL7mvEmki_hk4p0Z3J1lYQ66BDSs")
	# Get the registration ID from the user device saved on database
	# Push the registration ID after the user has accepted to receive notifications
	
	notification_tokens = ["euvrkBEXRlXmgonZxrUwFI:APA91bF30qMldPLUiSKxLU7HWMofQ1irb-72DhgBiOcjAQVMOWgMgJL53rREW3dVPeDnBiWiT_i7r5Gjzp3CdCGW6n2SJ7fVzFqqL5ttA3E_aSlTxhop5yJLoQm3H6jxYcOwKDN79qYA"]
	
	# list of all user IDs
	for el in UserALAMAU.objects.exclude(notification_token__isnull=True):
		if el.notification_token != "":
			notification_tokens.append(el.notification_token)

	notification_title = instance.title
	notification_content = instance.content

	data_payload = {
		"badge": 5,
		"alert": notification_title,
		"notification_id": 1,
		"body": notification_content,
	}

	result = push_service.notify_multiple_devices(
		registration_ids=notification_tokens,
		badge=5,
		data_message=data_payload,
		message_body=notification_content)

def sendNewMessagePushNotification(**kwargs):
	sender = UserALAMAU.objects.get(id=kwargs.get("sender_id"))
	recipient = UserALAMAU.objects.get(id=kwargs.get("recipient_id"))
	content = kwargs.get("content")
	notification = MobileNotification()
	notification.recipient = recipient
	notification.title = "New notification"
	sender_full_name = "{} {}".format(sender.first_name, 
									  sender.last_name)
	message = '{} has sent you a message: "{}"'.format(sender_full_name, 
													   content)
	notification.message = message

	data_payload = {
		"badge": recipient.unread_notifications_count(),
		"alert": notification.title,
		"notification_id": notification.pk,
		"body": notification.message,
	}
	fcm = FCMNotification(api_key=settings.FIREBASE_API_KEY)

	return fcm.notify_single_device(
		#registration_id=str(recipient.device.token),
		badge=recipient.unread_notifications_count(),
		data_message=data_payload,
		message_body=content)