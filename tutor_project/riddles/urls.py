from . import views
from django.urls import path

app_name = 'riddles'

urlpatterns = [
    path('', views.main, name = 'main'),
]