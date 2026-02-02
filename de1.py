
import math
import time


#Cách 1 code sạch - gọn - dễ đọc
#Học thuộc cú pháp thì học từ đây đến
def c1(x):
  S = 0
  for i in range(3, x + 1, 2):
    S += i**0.5
  return S
# đến đây nha học nhiêu đây đủ sống rồi ngắn lắm cái bên dưới ngắn hơn nhg hơi khó thuộc với sợ thầy bắt giải thích code á nên ní đừng sài! :>>

#Cách 2 code sạch nhanh gọn cần import thư viện nha
def c2(x):
  return sum(math.sqrt(i) for i in range(3, x + 1, 2))
  


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


