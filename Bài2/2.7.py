print("Nguyễn Văn Hùng")
print("245752021610031")
# Tạo dictionary chứa (i, i*i)
n = int(input("Nhập vào một số: "))
d = {}
for i in range(1, n + 1):
    d[i] = i * i
print(d)
