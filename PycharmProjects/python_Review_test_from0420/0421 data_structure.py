# list []/ tuple ()/ dic {}
# append and extend: append for only add one more element, extend adding a list
l1 = [2,3,4]
l1.append(5)
print(l1)
l1.extend([6,7,8])
print(l1)

#del / pop / remove
del(l1[0])
print(l1)
l1.pop()
print(l1) # result line 5
l1.remove(4) # remove specific #
print(l1)

## String : concat
# ASCII code american standard code for information interchange
s = 'abc'
# s[0] = 'b'
# print(s) that's wrong cuz string is unmmutable

#tuple
b = ("Bob","19","CS")
c = ('Chris','20','EECS')
(name, age, major) = c #unpacking the tuple
print((name,age))
#compare w LIST
L = [9,6,3,0]
new_L = sorted(L) # DOES NOT mutate L
print(L)
L.sort()
print(L)
L.reverse()
print(L)

# CLASS
class Student:
    def __init__(self,name,grade,school):
        self.name = name
        self.grade = grade
        self.school = school
    def display_student(self,school_year):
        print('Name:',self.name, ', Grade:',self.grade,',School_year:',school_year)


student_john = Student('John',98,'UCB')
student_john.display_student(2021)
student_kay = Student('Kay',90,'CMU')
student_kay.display_student(2019)

student_list = []
student_list.append(student_john)
student_list.append(student_kay)
for student in student_list:
    student.display_student(2022)


