from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    # http://127.0.0.1:8000/books/->
    path('', views.BooksIndexView.as_view(), name='index'), 

    # http://127.0.0.1:8000/books/book ->
    path('book/', views.BookList.as_view(), name='booklist'),   

    # http://127.0.0.1:8000/books/publisher ->
    path('publisher/', views.PublisherList.as_view(), name='publisherlist'), 

    # http://127.0.0.1:8000/books/publisher/1 ->
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisherdetail'),   

    # http://127.0.0.1:8000/books/publisher/insert->
    path('publisher/insert/', views.PublisherCreate.as_view(), name='publisherinsert'),

    # http://127.0.0.1:8000/books/publisher/update/2->
    path('publisher/update/<int:pk>/', views.PublisherUpdate.as_view(), name='publisherupdate'),

    # http://127.0.0.1:8000/books/publisher/delete/2->
    path('publisher/delete/<int:pk>/', views.PublisherDelete.as_view(), name='publisherdelete'),


]

# as_view() 메소드 - 진입메소드, 
# urls.py에서 클래스형뷰의 as_view() 메소드를 호출

