from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Accounts import views
#from rest_framework_jwt.views import obtain_jwt_token

#from django.urls import path




urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('Main.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
