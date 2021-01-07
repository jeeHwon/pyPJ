from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    hp = models.CharField(max_length=50)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):      # = 자바의 toString() 
        return self.question_text
