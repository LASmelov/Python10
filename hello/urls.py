from django.urls import path
from firstapp import views
from firstapp import views


urlpatterns = [
    path('', views.index),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('details/', views.details),
]