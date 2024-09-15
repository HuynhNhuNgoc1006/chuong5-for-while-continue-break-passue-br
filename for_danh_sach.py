# Viết chương trình có thể tạo danh sách:
    #Số lượng các phần tử đc chọn ngẫu nhiên từ 20 đến 30
    #Các giá trị bình phương của các số thực đc chọn ngẫu nhiên từ 18 dến 99

import random
so_luong_phan_tu = random.randint(20,30)
danh_sach = [random.randint(18, 99)**2 for i in range(so_luong_phan_tu)]
print(danh_sach)