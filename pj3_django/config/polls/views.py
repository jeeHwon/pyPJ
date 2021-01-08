from django.shortcuts import render
from .models import Question

def index(request):
    return render(request, 'polls/index.html')    # 요청, 반환할 페이지

def dbtest(request):    # 127.0.0.1:8000/polls/dbtest
    # -> id 값 없는경우 : 삽입
    # q = Question(question_text='좋아하는 운동은', pub_date='2021-01-07')
    # q.save()  
    # -> id 값 있는경우 : 해당 아이디 수정
    # q = Question(id=1, question_text='좋아하는 칼라는', pub_date='2021-01-07')
    # q.save()

    # 2) 조회
    # qlist = Question.objects.all()      # 모든 데이터
    # qlist = Question.objects.get(id=3)  # 조건에 맞는 데이터
    # print(qlist)

    # return render(request, 'polls/dbtest.html')   
    # return render(request, 'polls/dbtest.html', {'aa':'bb'})
    # return render(request, 'polls/dbtest.html', {'qlist':qlist})

    # 3) 삭제
    # q= Question.objects.get(id=1)   # 해당데이터를 가져온 뒤
    # q.delete()
    qlist = Question.objects.all()
    return render(request, 'polls/dbtest.html', {'qlist':qlist})

