from django.shortcuts import render
from .models import Member
from django.contrib.auth.hashers import make_password

def insert(request):
    if request.method=='GET':
        return render(request,'insert.html')    #127.0.0.1:8000/member/insert
    elif request.method=='POST':
        username = request.POST['username']
        pw = request.POST['pw']
        pw1 = request.POST['pw1']
        msg = {}
        if pw != pw1:
            msg['err'] = '비밀번호를 확인하세요'
        else :
            email = request.POST['email']
            hp = request.POST['hp']
            m = Member(
                username = username,
                pw = make_password(pw),         # 패스워드 암호화 하여 저장
                email = email,
                hp = hp
            )
            m.save()
        return render(request,'insert.html', msg)
