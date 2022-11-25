from main import *

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.add_course('Python')

student2 = Student('Ruoy1', 'Eman1', 'your_gender')
student2.add_course('C++')

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.add_course('Python')
reviewer1.rate_hw(student1, 'Python', 10)

reviewer2 = Reviewer('Some', 'Buddy')
reviewer2.add_course('C++')
reviewer2.rate_hw(student2, 'C++', 4)

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.add_course('Python')
lecturer1.grade_student('Python', student1, 6)

lecturer2 = Lecturer('Some', 'Buddy')
lecturer2.add_course('C++')
lecturer2.grade_student('C++', student2, 3)


print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)

print(lecturer1 < student1)
print(lecturer1 > student1)
print(lecturer1 <= student1)
print(lecturer1 <= student1)
print(lecturer1 != student1)

print(get_average_hm_grade_by_course([student1, student2], 'Python'))
print(get_average_lecture_grade_by_course([lecturer1, lecturer2], 'Python'))
