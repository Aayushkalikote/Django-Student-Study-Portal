from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('notes', views.notes,name="notes"),
    path('delete_notes/<int:pk>', views.delete_notes,name="delete-note"),
    path('detail_notes/<int:pk>', views.NoteDetailView,name="detail-note"),
    
    path('homeworks', views.homework,name="homeworks"),
    path('update_homework/<int:pk>', views.update_homework,name="update-homework"),
    path('delete_homework/<int:pk>', views.delete_homework,name="delete-homework"),
    
    path('youtube', views.youtube,name="youtube"),
    
    path('todos/', views.todo,name="todos"),
    path('update_todo/<int:pk>', views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo,name="delete-todo"),
    
    path('books/', views.book,name="books"),
    
    path('dictionary', views.dictionary,name="dictionary"),
   
]
