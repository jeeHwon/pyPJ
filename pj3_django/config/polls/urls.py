from django.urls import path, include
from . import views

urlpatterns = [
    # path(url패턴, url이 매칭되면 호출되는 뷰함수 [, 이름]),
    path('', views.index),             # http://127.0.0.1:8000/polls       
    path('<int:qid>/', views.detail),             # http://127.0.0.1:8000/polls       
    path('dbtest/', views.dbtest),     # http://127.0.0.1:8000/polls/dbtest       
]
