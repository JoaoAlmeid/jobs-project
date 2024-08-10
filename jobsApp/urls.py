from django.urls import path
from . import views

app_name = 'jobApp'

urlpatterns = [
    path('', views.index, name="inicio")
]