from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Publisher, Author

class BookList(ListView):
    model = Book

class PublisherList(ListView):
    model = Publisher
    
class PublisherDetail(DetailView):
    model = Publisher