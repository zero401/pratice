import sys
from collections import Counter

class Person(object):
    def __init__(self):
        return self

    def get_grade(self):
        return self

class Student(Person):
    def __init__(self):
        Person.__init__(self)
    
    def get_grade(self,grade):
        self.grade = grade
        i = Counter(self.grade).most_common()
        p, f = 0, 0
        for x in i:
            if x[0] != 'D':
                p += x[1]
            else:
                f += x[1]
        print("Pass: {}, Fail: {}".format(p, f))

class Teacher(Person):
    def __init__(self):
        Person.__init__(self)

    def get_grade(self,grade):
        self.grade =grade
        i = Counter(self.grade).most_common()
        o = []
        for k, v in i:
            o.append("{}: {}".format(k, v))
        print(', '.join(o))

if sys.argv[1] =="student":
    s1 = Student()
    s1.get_grade(sys.argv[2])
else:
    t1 = Teacher()
    t1.get_grade(sys.argv[2])    
               
           
        
