
# #multiple inheritace
#
# class one:
#     x=10
#     y=20
#     def add(self):
#         z= self.x+self.y
#         print(z)
# class second:
#     a=100
#     b=200
#     def mul(self):
#         c=self.a*self.b
#         print(c)
# class third(one , second):
#     def sub(self):
#         w=self.a-self.x
#         print(w)
#
# k2=third()
# k2.add()
# k2.mul()
# k2.sub()



# #heirarchical inheritance
#
# class one:
#     x=10
#     y=20
#     def add(self):
#         z= self.x+self.y
#         print(z)
# class second(one):
#     a=100
#     b=200
#     def mul(self):
#         c=self.a*self.b
#         print(c)
# class third(one):
#     def sub(self):
#         w=self.a-self.x
#         print(w)
#
# k2=third()
# k2.add()
# k2.mul()
# k2.sub()



#hybrid inheritace
class one:
    x=10
    y=20
    def add(self):
        z= self.x+self.y
        print(z)
class second(one):
    a=100
    b=200
    def mul(self):
        c=self.a*self.b
        print(c)
class third(second):
    def sub(self):
        w=self.a-self.x
        print(w)


class four(third):
    pass
class five(third):
    pass
class six(third):
    pass
class seven(four,five,six):
    pass


k2=third()
k2.add()
k2.mul()
k2.sub()