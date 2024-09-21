# x= int(input("so kwh:  "))
# if x<50 :
#     print("so tien phai tra la:", x*1700)
# if x>50 and x<=100:
#     print("so tien phai tra la:", 50*1700 + (x-50)*1900 )
# if x>100 and x<=200:
#     print("so tien phai tra la:", 50*1700 + (x-50)*2100)
# if x>200:
#     print("so tien phai tra la:", 50*1700 + (x-50)*3000)

# number_of_kwh = int(input("Nhập số kwh: "))
# total = 0
# if number_of_kwh <= 50:
#     total = number_of_kwh * 1700
# elif number_of_kwh <= 100:
#     total = 50 * 1700 + (number_of_kwh - 50) * 1900
# elif number_of_kwh <= 200:
#     total = 50 * 1700 + 50 * 1900 + (number_of_kwh - 100) * 2100
# else:
#     total = 50 * 1700 + 50 * 1900 + 100 * 2100 + (number_of_kwh - 200) * 3000
    
# print("Số tiền phải trả là: ", total)


kwh_consumed = float(input("Nhập số tiền điện:")) #145
total_cost = 0
if 0 <= kwh_consumed <= 50:
        total_cost = 1700*kwh_consumed
elif 51 <= kwh_consumed <= 100:
        total_cost = 1700*50 + 1900*(kwh_consumed-50)
elif 101 <= kwh_consumed <= 200:
        total_cost = 1700*50 + 1900*50+ 2100*(kwh_consumed-100)
else:
        total_cost = 1700*50 + 1900*50+ 2100*100 + 3000*(kwh_consumed-200)

print("Tổng số tiền" , total_cost )