from django.shortcuts import render
from .models import Question
from django.shortcuts import get_object_or_404

def detail(request, qid):
    # q = Question.objects.get(id=qid)       # select * from question where id=qid
    q = get_object_or_404(Question, id=qid)  # err 발생시 404 페이지 출력
    c = q.choice_set.all()
    print(c, len(c), '*********************************')
    msg = {}
    msg['q'] = q
    if len(c) < 1:
        msg['err'] = '선택할 항목이 없습니다.'

    return render(request,'polls/detail.html', msg)

def index(request):
    qlist = Question.objects.all()
    return render(request, 'polls/index.html', {'qlist':qlist})    # 요청, 반환할 페이지

def vote(request, qid):
    q = Question.objects.get(id=qid)
    cid = request.POST['choice']
    # Question과 Choice는 1:N 관계, 외래키로 연결된 경우 모델 소문자_set 속성이 제공
    # q.choice_set.all()  # 모든 데이터 가져오기
    c = q.choice_set.get(id=cid)    # 특정 데이터 가져오기
    c.votes = c.votes + 1
    c.save()
    return render(request, 'polls/result.html', {'q':q})    # 요청, 반환할 페이지




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

