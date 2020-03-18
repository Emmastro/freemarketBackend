from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	#path('', views.home, name='home'),

	path('', views.Inbox.as_view(), name='inbox'),

	#path('admin/', views.Admin_view.as_view(), name='admin_lib'),

]
