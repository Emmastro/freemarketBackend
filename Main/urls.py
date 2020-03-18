from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
	path(r'update/', views.UpdatesView.as_view()),
    path(r'update/<int:pk>', views.UpdateView.as_view()),

	path(r'event/', views.EventsView.as_view()),
    path(r'event/<int:pk>', views.EventView.as_view()),

	path(r'busschedule/', views.BusSchedulesView.as_view()),
    path(r'busschedule/<int:pk>', views.BusScheduleView.as_view()),

	path(r'calendar/', views.CalendarView.as_view()),

	path(r'notification/<str:username>', views.NotificationView.as_view(),),
	path(r'notification/', views.NotificationView.as_view(),),
	]