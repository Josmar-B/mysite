from django.urls import path
from myapp.views import *
urlpatterns = [
    path('authors/', author_list, name="author_list"),
    path('author/add',create_author, name="create_author"),
    path('author/delete/<int:id>', delete_author, name="delete_author"),
    path('author/edit/<int:id>', update_author, name="update_author")
]