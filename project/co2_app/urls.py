from django.urls import path

from co2_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
