from collections import namedtuple
total_n = int(input())  # the total number of students.
s = input().split() #the names of the columns in any orde
S = namedtuple('Student', s) 
students_list = []
for i in range(total_n):
    s_info = input().split()
    student_obj = S(*s_info) 
    students_list.append(student_obj)
total = 0
for s in students_list:
    total += int(s.MARKS)
avg = total / total_n
print("{:.2f}".format(avg))
