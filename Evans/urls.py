from django.urls import path
from Evans import views

urlpatterns =[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('resume',views.resume, name='resume'),
    path('services', views.services, name='services'),
]

