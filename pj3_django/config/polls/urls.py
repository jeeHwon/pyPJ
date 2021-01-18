from django.urls import path, include
from . import views
app_name = 'polls'
urlpatterns = [
    # path(url패턴, url이 매칭되면 호출되는 뷰함수 [, 이름]),
    path('', views.index, name='list'),                   # http://127.0.0.1:8000/polls       
    path('<int:qid>/', views.detail, name='detail'),      # http://127.0.0.1:8000/polls       
    path('vote/<int:qid>/', views.vote, name='vote1'),    # http://127.0.0.1:8000/polls/vote/3 
    # => polls:vote1 으로 표기 {% url 'polls:vote1'%} 태그 사용
    path('dbtest/', views.dbtest),                        # http://127.0.0.1:8000/polls/dbtest       
]
