from django.urls import path
from . import views

app_name = 'notes' 

urlpatterns = [
    # Change "notes/" to "" (empty string) ✅
    path("", views.note_list, name="note_list"), 
    
    path('create/', views.note_create, name='note_create'),
    
    # Change "notes/<int:pk>/edit/" to "<int:pk>/edit/" ✅
    path("<int:pk>/edit/", views.note_edit, name="note_edit"),
    
    # Change "notes/<int:pk>/delete/" to "<int:pk>/delete/" ✅
    path("<int:pk>/delete/", views.note_delete, name="note_delete"),
]