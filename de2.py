import math
import time


#Cách 1 code sạch - gọn - dễ đọc
#học thuộc thì học từ đây đến
def c1(x):
  S = 0
  for i in range(2, x + 1, 2):
    S += i**-0.5 # i**-n == 1/(i**n)
  return S
# đến đây nha code dưới ngắn hơn nhg mà sợ thầy bắt m giải thích á nếu sài code dưới mà thầy hỏi thì bảo là đây là cách viết tối ưu gọn mà em tìm hiểu dc trên mạng 


#Cách 2 code sạch nhanh gọn cần import thư viện nha
def c2(x):
  return sum(1/(math.sqrt(i)) for i in range(2, x + 1, 2))# generator : (<biểu_thức> for <biến> in <iterable> if <điều_kiện>) 
 


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
