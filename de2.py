import math
import time


#Cách 1 code sạch - gọn - dễ đọc
# số lớn thì này nhanh hơn 
def c1(x):
  S = 0
  for i in range(2, x + 1, 2):
    S += i**-0.5 # i**-n == 1/(i**n)
  return S
 


#Cách 2 code sạch nhanh gọn cần import thư viện nha
# số nhỏ thì này lại nhanh hơn kia 
def c2(x):
  can = math.sqrt
  return sum(map(lambda a: can(a), range(2, x + 1, 2)))
 


#----Test tốc độ ------
n = int(input("Nhập số nguyên dương n = "))
start = time.time()
c = c1(n)
end = time.time()
print(f'Cách 1 kết quả là {c} và chạy xg trong {end - start}')
start2 = time.time()
c = c2(n)
end2 = time.time()
print(f'Cách 2 kết quả là {c} và chạy xg trong {end2 - start2}')
ss = "Cách 1 nhanh hơn cách 2" if (end - start) < (end2 - start2) else "Cách 2 nhanh hơn cách 1"
print(ss)
#linh sài cách 1 oke ròi cách 2 thì nhanh hơn 1 síu nhg mà khoai á 
#học thuộc này nek :
# n = int(input("Nhập số nguyên dương n = "))
# S = 0
#  for i in range(2, x + 1, 2):
#   S += i**-0.5 # i**-n == 1/(i**n)
# return S
