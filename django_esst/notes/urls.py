from django.urls import path
from . import views
urlpatterns = [
  # path('notes/',views.list_note,name='list_note'),
  path('notes/',views.NotesListView.as_view(),name='list_note'),
  # path('notes/<int:pk>',views.detail,name="detail"),
    path('notes/<int:pk>',views.NotesDetailView.as_view(),name="detail"),

]