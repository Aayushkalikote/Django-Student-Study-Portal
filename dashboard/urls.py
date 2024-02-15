from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('notes', views.notes,name="notes"),
    path('delete_notes/<int:pk>', views.delete_notes,name="delete-note"),
    path('detail_notes/<int:pk>', views.NoteDetailView,name="detail-note"),
    
     path('homeworks', views.homework,name="homeworks"),
]
