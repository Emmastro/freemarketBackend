import pandas as pd

class Url:
	
	def __init__(self, link, param=0):
		""" Support only one parameter"""
		self.link = link
		self.param = param


class Menus(object):
	"""
	Manage menus according to the user profile
	--> current : current page to highlight in the menu
	--> is_anonymous : personalise menu according to the log in statut
	"""
	
	def __init__(self, current, request, platform=False):
		super(Menus, self).__init__()
		self.current = current

		if platform:

			self.menus = ['Home']
			self.menu_urls = ['home_portail']
			if request.user.is_anonymous:
				self.menus.extend(["Register"])
				self.menu_urls.extend(['register_school'])
			else:
				self.menus.extend(['Log out',])
				self.menu_urls.extend(['logout'])

		else:
			#if request.user.is_staff:
				
			self.menus = ['Dashboard', 'Home','My readings']
			self.menu_urls = ['dashboard', 'home', 'MyReadings']
			if request.user.is_anonymous:
				self.menus.extend(["Log in"])
				self.menu_urls.extend(['login'])
			else:
				self.menus.extend(['Add book', 'My account', 'Log out'])
				self.menu_urls.extend(['addbook', Url('account_settings', request.user.id), 'logout'])

				#Convert the string to Urls
		for i,l in enumerate(self.menu_urls):
			if type(l)==type('a'):
				self.menu_urls[i] = Url(l)

		self.i = 0

	def __iter__(self):
		
		return self

	def __next__(self):
		i=self.i
		if i >= len(self.menus):
			raise StopIteration
		self.i+=1
		return self.Menu(
			self.menus[i], 
			self.menu_urls[i],
			self.is_current(i), 
			self.is_home(i))

	def is_current(self, n):
		if n==self.current:
			return "current-menu-item"
		else:
			return ''

	def is_home(self, n):

		if n==0:
			return 'menu-item-home'
		else:
			return'menu-item-object-page'

	class Menu:
		"""docstring for Menu"""
		def __init__(self, title, menu_url, current, icon, is_home):
			self.title = title
			self.menu_url = menu_url
			self.current = current
			self.icon = icon
			self.is_home = is_home
