from django.urls import path
from . import views
app_name = 'meroshop'

urlpatterns = [
    path('', views.hello, name='hello')
]
