from django import forms
from Accounts.models import UserALAMAU


class RegisterForm(forms.ModelForm):

	class Meta:
		model = UserALAMAU
		fields = ['username','email', 'password']
		widgets = {
		'password': forms.PasswordInput()
		}