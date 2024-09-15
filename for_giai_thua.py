# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:46:28 2024

@author: Student
"""

#viết chương trình tính giai thừa của một số cho trước n (nguyên dương) đc nhập từ bàn phím
# S= n! = 1.2.3...n

n = int(input("Nhập số nguyên dương n:"))
giai_thua = 1
for i in range(1, n+1):
    giai_thua *= i
print(n, "! =", giai_thua)

print("Vui lòng nhập số nguyên dương")    