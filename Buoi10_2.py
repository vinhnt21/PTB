menu = """
==========================================================
1. Xem sản phẩm trong giỏ hàng
2. Thêm sản phẩm vào
3. Xóa sản phẩm đi (nhập số thứ tự của sản phẩm)
4. Thoát chương trình
Lựa chọn (nhập số tương ứng): """

cart = []

while True:
    user_choice = int(input(menu))
    
    if user_choice == 1:
        print("Giỏ hàng của bạn gồm: ")
        print(cart)
    elif user_choice == 2:
        new_product = input("Sản phẩm bạn muốn mua: ")
        cart.append(new_product)
    elif user_choice == 3:
        print("Chuc nang so 3")
    elif user_choice == 4:
        print("Bye bye😼")
        break
    else:
        print("Lựa chọn không hợp lệ")