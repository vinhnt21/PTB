"""
1. Nhập điểm của các bạn trong lớp
    - Yêu cầu nhập điểm của các bạn trong lớp
    - Khi nhập xong thì ấn enter
    - Khi muốn thoát gõ 'exit'
2. Tính điểm trung bình
    - Tính tổng
    - Tính bình cộng cả lớp
3. Sắp xếp theo điểm từ cao đến thấp
"""
student_points = []
while True:
    user_input = input("Enter student point\nType 'exit' to end programe\n")
    if user_input == 'exit':
        break
    else:
        point = float(user_input)
        student_points.append(point)
print('Points:', student_points)
# sum_points=0
# for point in student_points:
#     sum_points += point
# for i in range(len(student_points)):# start = 0, end = 4, step = 1 
#     sum_points+= student_points[i]
sum_points = sum(student_points)
avg_points = sum_points/len(student_points)
print(avg_points)
student_points.sort(reverse=True)
print(student_points)