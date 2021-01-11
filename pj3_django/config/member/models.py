from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=50, verbose_name='사용자이름')
    pw = models.CharField(max_length=50, verbose_name='비밀번호')
    email = models.CharField(max_length=50, verbose_name='이메일주소')
    hp = models.CharField(max_length=50, verbose_name='휴대폰번호')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    def __str__ (self):
        return self.username+'-' + self.hp
    class Meta:
        db_table='member'

