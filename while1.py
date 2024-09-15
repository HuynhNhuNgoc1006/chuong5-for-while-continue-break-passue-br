while True:
    
        so = int(input("Nhập vào một số nguyên trong khoảng [-99;99]: "))
        if -99 <= so <= 99:
            print("Giá trị bạn nhập hợp lệ!")
            break
        else:
            print("Giá trị không nằm trong khoảng cho phép. Vui lòng nhập lại!")
    
        print("Bạn phải nhập một số nguyên. Vui lòng nhập lại!")