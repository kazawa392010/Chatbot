import math
import time


#Cách 1 code sạch - gọn - dễ đọc
def c1(x):
  S = 0
  for i in range(2, x + 1):
    S += i / (i - 1)
  return S


#Cách 2 code  gọn (chạy chậm hơn c1)
def c2(x):
  S = sum(i / (i - 1) for i in range(2, x + 1))
  return S


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
ss = "Cách 1 nhanh hơn cách 2" if (end - start) < (   end2 - start2) else "Cách 2 nhanh hơn cách 1"
print(ss)
