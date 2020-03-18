from django import template

from django.db import connection
from django.contrib.auth.models import User

register = template.Library()
#SITE  = "/127.0.0.1:8000"

@register.filter(is_safe=True)
def split(lst,n):
	""" regroupe la liste en n sous listes"""
	result = []
	for l in range(int(len(lst)/5)):
		result.append(lst[5*l:5*(l+1)])
	try:
		result.append(lst[5*(l+1)])
	except:
		pass	

	return result

@register.filter(is_safe=True)
def book_statut(user, book):
	''' Return the statut of a book, 0|1|2'''
	print("User", user)
	return book.statut(user)

