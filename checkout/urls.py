from django.conf.urls import patterns, url
from checkout import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^get/(\d+)', views.get),
	url(r'^checkout/', views.checkout),
	url(r'^register', views.register)
)
