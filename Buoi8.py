'''
- Lấy dữ liệu từ người dùng
    + input với ép sang int
    + kiểm tra dữ liệu
        - cả 3 phải > 0
- Kiểm tra:
    +  if
    +  toán tử and
'''

print("Nhập 3 cạnh của tam giác:")
a = int(input('Cạnh thứ nhất: '))
b = int(input('Cạnh thứ hai: '))
c = int(input('Cạnh thứ ba: '))

if a > 0 and b > 0 and c > 0:
    if (a+b)>c and (a+c)>b and (b+c)>a:
        print("Hợp lệ")
    else:
        print("Cạnh không hợp lệ")
else:
    print("Cạnh không được âm")
