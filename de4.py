import math
import time


#Cách 1 code sạch - gọn - dễ đọc
def c1(x, y):
  S = 0
  for i in range(1, x + 1):
    S += i + y
  return S


#Cách 2 code sạch nhanh gọn 
def c2(x, y):
  S = sum(i + y for i in range(1, x + 1))
  return S


#----Test tốc độ ------
n = int(input("Nhập số nguyên dương n = "))
a = int(input("Nhập số a = "))
start = time.time()
c = c1(n, a)
end = time.time()
print(f'Cách 1 kết quả là {c} và chạy xg trong {end - start}')
start2 = time.time()
c = c2(n, a)
end2 = time.time()
print(f'Cách 2 kết quả là {c} và chạy xg trong {end2 - start2}')
ss = "Cách 1 nhanh hơn cách 2" if (end - start) < (end2 - start2) else "Cách 2 nhanh hơn cách 1"
print(ss)
