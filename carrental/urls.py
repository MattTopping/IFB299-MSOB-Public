# Libraries
from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

# Car Rental Files 
from carrental import views



# Defining the urls of the project
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^signin/', views.signin, name='signin'),	
	url(r'^car/(?P<id>\d+)/$', views.car_desc, name='car'),
	url(r'^store/(?P<id>\d+)/$', views.store_stock, name='store'),
	url(r'^adminanalysis/', views.analysisLoad, name='adminAnalysis')	
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)