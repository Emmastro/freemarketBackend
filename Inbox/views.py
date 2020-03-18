from django.shortcuts import render, redirect, get_object_or_404

from django.template.loader import render_to_string


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from django.views.generic import ListView, DetailView, UpdateView
from django.views import View

from django.utils.decorators import method_decorator

from django.http import HttpResponse, FileResponse, JsonResponse
from .forms import*

from .models import*

import datetime 

from django.core.mail import send_mail

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from django.db.models import Q, F # Grouping for book suggestions



@method_decorator(login_required, name='dispatch')
class Inbox(View):
	"""docstring for Read_view"""
	
	#model = Book
	template_name = "Inbox.html"
	#context_object_name = "book"


	def get_context_data(self, **kwargs):
		
		return context

	def get_object(self):
		""""""

		pass

	def get(self, request, *args, **kwargs):
		
		pass

