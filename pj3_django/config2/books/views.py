from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Publisher, Author
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

class BookList(ListView):
    model = Book

class PublisherList(ListView):
    model = Publisher
    
class PublisherDetail(DetailView):
    model = Publisher

class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name', 'addr', 'website', 'photo']   # 입력 받을 컬럼 지정
    template_name = 'books/publisherinsert.html'
    success_url = '/books'  # CreateView, UpdateView, DeleteView 를 사용시 특정기능 수행후 페이지 이동
    # def form_valid(self, form):
    #     print(form.instance.name)
    #     print(form.instance.addr)
    #     print(form.instance.photo)
    #     if form.is_valid():
    #         form.instance.save()
    #         return redirect('/books/publisher')
    #     else:
    #         return self.render_to_response({'form':form})

class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['name', 'addr', 'website', 'photo']   # 수정할 컬럼 지정
    template_name = 'books/publisherupdate.html'
    success_url = '/books/publisher'

class PublisherDelete(DeleteView):
    model = Publisher
    template_name = 'books/publisherdelete.html'
    success_url = '/books/publisher'

class BooksIndexView(TemplateView):
    template_name = 'books/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mlist'] = ['book', 'publisher', 'author']
        return context
