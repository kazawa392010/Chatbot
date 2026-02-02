
import math
import time


#Cách 1 code sạch - gọn - dễ đọc
def c1(x):
  S = 0
  for i in range(3, x + 1, 2):
    S += i**0.5
  return S


#Cách 2 code sạch nhanh gọn cần import thư viện nha
def c2(x):
  S = sum(math.sqrt(i) for i in range(3, x + 1, 2))
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
ss = "Cách 1 nhanh hơn cách 2" if (end - start) < (end2 - start2) else "Cách 2 nhanh hơn cách 1"
print(ss)
