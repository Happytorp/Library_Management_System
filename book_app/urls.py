from book_app import views
from django.urls import path

urlpatterns = [
    path('', views.book, name ='book'),
    path('delete/<book_id>', views.delete_book, name ='delete_book'),   # creating the urls for the respective views
    path('edit/<book_id>', views.edit_book, name ='edit_book'),
    path('student', views.student_view, name ='student_view'),
    
]