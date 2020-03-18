from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User


class UserALAMAU(User):
	""""""
	bio = models.TextField(null=True, blank=True)
	category = models.CharField(max_length=128, blank=True, null=True) # Delegate, Advisor, Administrator with different rights ...
	image = models.ImageField(upload_to="profile_picture",
		verbose_name="Profil Image", null=True, blank=True)
	exploreJoburg = models.ForeignKey("Main.Event", on_delete = models.CASCADE, null=True, blank=True)
	notification_token = models.TextField(null=True, blank=True)
	

	def profile_picture_url(self):
		"""
		"""
		if self.image and hasattr(self.image, "url"):
			return self.image.url

	def get_absolute_url(self):

		return reverse('accounts', kwargs={'pk': self.pk})

	def image_url(self):
		
		if self.image and hasattr(self.image, "url"):
			return self.image.url

	class Meta(object):
		"""docstring for Meta"""
		verbose_name = 'ALAMAU User'
		verbose_name_plural = 'ALAMAU Users'

class Delegation(models.Model):
	"""
	Description: Model Description
	"""
	
	name = models.CharField(max_length=128)
	# Different category of people in the delegation will be gotten from the User_ALAMAU category
	people = models.ManyToManyField('UserALAMAU')
	school = models.OneToOneField('Main.School', on_delete=models.CASCADE)

	class Meta:
		pass