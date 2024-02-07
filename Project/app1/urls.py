from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name='index'),
    path('form',views.form , name='form'),
    path('list',views.list_users , name='users')
    
]

