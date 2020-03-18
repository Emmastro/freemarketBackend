from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Accounts import views
#from rest_framework_jwt.views import obtain_jwt_token

#from django.urls import path
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
	#path('accounts/', include('django.contrib.auth.urls')),
	path('api/', include('Main.urls')),
    path('api/', include('Accounts.urls')),
    path('admin/', admin.site.urls),
    path('calendar/', include('Calendar.urls')),
    path('inbox/', include('Inbox.urls')),
    path('help/', include('Help.urls')),    
    #path('token-auth/', obtain_jwt_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static("", document_root = settings.STATIC_ROOT  + '/js/firebase-messaging-sw.js')
#urlpatterns+=static(r'^static/(?P<path>.*)$', document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#handler404 = 'ALAMAU.views.my_custom_page_not_found_view'
# the custom 404 hadler make a CSRF Error on production

