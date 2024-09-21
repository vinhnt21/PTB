"""
Danh sách (list)
"""
students_name = ['Thái', 'Khánh', 'Dương', 'Hải', 'Nhật', 'Minh']
students_point = [14,12,12,15,11,13]

# len viết tắt của length
number_student = len(students_name) #6
sum = 0
for i in range(0, number_student,1):
    sum += students_point[i]

print("sum::", sum)
print("avg::", sum/number_student)
