def tinh_luong(gio_lam, luong_gio):
    return gio_lam * luong_gio

def in_thong_tin(ten, gio_lam, luong_gio, tong_luong):
    print(f"Tên nhân viên: {ten}")
    print(f"Số giờ làm: {gio_lam}")
    print(f"Lương giờ: {luong_gio}")
    print(f"Tổng lương: {tong_luong}")
    
name = input("Nhập tên nhân viên: ")
hours = int(input("Nhập số giờ làm: "))
salary_per_hour = int(input("Nhập lương giờ: "))
salary = tinh_luong(hours, salary_per_hour)


in_thong_tin(name, hours, salary_per_hour, salary)