import math

# coi t code mà học thuộc 1 2 đề ik nha bữa kiểm tra t phải lm xg bài t r t ms giúp m dc

# Đề 1 nek:
print("Đề 1")
n = int(input("Nhập số nguyên lẻ n  = "))
ketqua = 0
for i in range(3, n + 1): #cái này là nếu n là số lẻ nha
  #tại t thấy nó cộng số lẻ nếu n ko pk số lẻ thì t thêm đkienej la ổn
  if i % 2 != 0 :
    ketqua += math.sqrt(i)

print("Kết quả:", ketqua)

#Đề 2 nek 
print("Đề 2")
n = int(input("Nhập số nguyên chẵn n = ")) #này cũng y chang đề 1 lun nha khác mỗi là số chẵn, này chưa bt đúng chưa tại t chưa thấy yêu cầu đề bài :>>
ketqua = 0
for i in range(2, n + 1):
    ketqua += 1 / math.sqrt(i)

print("Kết quả:", ketqua)
    
