menu = """
++++ CHƯƠNG TRÌNH XỬ LÍ CHUỖI ++++
1. Đếm số ký tự trong chuỗi
2. Đếm số từ trong chuỗi
3. Đếm số nguyên âm trong chuỗi
4. Tìm từ dài nhất trong chuỗi
5. Tìm từ ngắn nhất trong chuỗi
6. Viết thành title case
+++ Nhập 0 để thoát chương trình +++
"""


while True:
    s  = input("Nhập chuỗi cần xử lí: ")
    choice = input(menu)
    if choice == '0':
        print("Bye bye😼")
        break
    elif choice == '1':
        n = len(s)
        print(f"Chuỗi {s} có {n} ký tự")
    elif choice == '2':
        print('...2')
    elif choice == '3':
        print('...3')
    elif choice == '4':
        list_words = s.split(" ")
        print(list_words)
        max_len = 0
        max_word = ""
        for i in range(len(list_words)):
            if len(list_words[i]) > max_len:
                max_len = len(list_words[i])
                max_word = list_words[i]
        print(f"Từ dài nhất trong chuỗi là: {max_word} với {max_len} ký tự")
    elif choice == '5':
        print('...5')
    elif choice == '6':
        print('...6')
    else:
        print("Lựa chọn không hợp lệ")