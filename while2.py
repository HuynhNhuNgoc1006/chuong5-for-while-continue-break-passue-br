while True:
    
        so_thuc = float(input("Nhập vào một số thực trong khoảng [-89.9; 88.8]: "))
        if -89.9 <= so_thuc <= 88.8:
            print("Giá trị bạn nhập hợp lệ!")
            break
        else:
            print("Giá trị không nằm trong khoảng cho phép. Vui lòng nhập lại!")