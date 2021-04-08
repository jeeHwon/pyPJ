# 03_03

class Parent:
    def sing(self):
        print('sing a song')
        
class LuckyChild(Parent):
    pass

luckyboy = LuckyChild()
luckyboy.sing()

class B:
    pass
inst1 = B()
inst2 = B()
inst1.data = 3
inst2.num = 4
print(inst1.data)
print(inst2.num)
