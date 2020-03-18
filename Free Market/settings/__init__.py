#import django_heroku
try:
	from .local import *
	#django_heroku.settings(locals())
except Exception as e:
	from .base import *
	from .production import *

#from .amazon_files import *

	#django_heroku.settings(locals())