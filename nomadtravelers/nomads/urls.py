from django.urls import path
from . import views

urlpatterns =[
    path('nomads/', views.nomads, name="nomads"),
    path('nomad/<str:pk>/', views.nomad, name="project"),
]