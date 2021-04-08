# 03_02

class SuperMario:
    def __init__(self):
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 20
        
mario = SuperMario()
mario.forward()
print(mario.pos)
mario.forward()
print(mario.pos)

class MyClass:
    pass

obj1 = MyClass()
print(id(obj1))
obj2 = MyClass()
print(id(obj2))