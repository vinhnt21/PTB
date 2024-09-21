"""
Nhập vào số n và in ra tất cả số nguyên tố từ 1 đến n

Ví dụ: 
Input: Nhập vào 20
Output: 2 3 5 7 11 13 17 19

Input: Nhập vào 10
Output: 2 3 5 7
"""
n = int(input("Nhập vào số n: ")) # 5
for i in range(2, n+1): # i = 2, 3, 4, 5
    is_prime = True
    for j in range(2, i): # j = 2, 3, 4, 5
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')