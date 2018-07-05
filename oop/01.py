'''
定义一个学生类，用来形容学生
'''
class Student():
    pass #此处占茅坑用的。。
#定义一个对象
mingyue = Student()
#定义学习python的学生
class python_Student():
    name = None
    age  = 18
    course = "python"
    def do_home_work(self):
        print("I do homework.")
        return None
#实例化
mingming = python_Student()
print(mingming.age)
print(mingming.name)
mingming.do_home_work()


