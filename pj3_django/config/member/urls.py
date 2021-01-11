from django.urls import path, include
from . import views

urlpatterns = [
    path('insert/', views.insert),             # http://127.0.0.1:8000/member/insert         
]
