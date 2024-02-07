from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name='index'),
    path('shelves',views.list_Shelves , name='list_Shelves'),
    path('shelves/add',views.add_Shelve , name='add_Shelve'),
    
    path('authors',views.list_Authors , name='list_Authors'),
    path('authors/add',views.add_Author , name='add_Author'),
    
    path('books',views.list_Books , name='list_Books'),
    path('books/add',views.add_Book , name='add_Book')
    
]

