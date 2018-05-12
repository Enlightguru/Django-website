from django.urls import path
from .import views

urlpatterns = [

	path('home/', views.home, name = 'home'),
	path('testimonials/',views.testimonials,name = 'testimonials'),
	path('articles/',views.articles,name ='articles'),
	path('gallery/',views.gallery,name ='gallery'),
	path('', views.home, name = 'home'),
	path('about/',views.about,name ='about'),
	path('events/',views.events,name ='events'),
	path('registration/',views.registration,name = 'registration'),

]