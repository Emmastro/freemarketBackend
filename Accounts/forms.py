from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django import forms
from Accounts.models import User_ALAMAU

from django import forms


#{#<input name="userName" type="text" class="form-control" placeholder="Username ..."/>#}

class LoginForm(AuthenticationForm):
	
	
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username ...'

		self.fields['password'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Password ...'


class User_ALAMAUForm(forms.ModelForm):
    class Meta:
        model = User_ALAMAU
        fields = ('first_name', 'last_name', 'username', 'email', )
    