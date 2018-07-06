class Person():
    name = "init"
    age = 0
    __age = 0
    _name = "halfname"

    def sleep(self):
        print("sleep.....")

    def Work(self):
        print("Get some money")


class Teacher(Person):
    name = "zhaolinger"
    # def Work(self):
    # Person.Work(self)
    # print("teacher students")
    # def Work(self):
    # self.Work_01()
    # Person.Work(self)


t = Teacher()
print(t.Work())
print(t.sleep())
