class A():
    name = "liuchan"
    age = 19
    def __init__(self):
        self.name = "yxg"
        self.age = 20
    def do_it(self):
        print("my name is {}".format(self.name))
        print("my age is {}".format(self.age))
class B():
    name = "swam"
    age = "99"
xx = A()
xx.do_it()
A.do_it(xx)

A.do_it(A)
A.do_it(B)