from django.urls import path
from . import views

app_name = "society"

urlpatterns = [
	path('signup/', views.upload_image, name = 'signup'),
	path('', views.index, name = 'index'),
	path('group/', views.group, name = 'group'),
	path('event/', views.event, name = 'event'),
	path('people/', views.people, name = 'people'),
	path('group/<int:group_id>/', views.detail, name='detailview'),
	path('event/<int:event_id>/', views.detail1, name='detailview1'),
	path('people/<int:people_id>/', views.detail2, name='detailview2'),
	path('signup/success/', views.success, name='success'),
	]