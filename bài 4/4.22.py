print("Nguyễn Văn Hùng")
print("2455752021610031")
result = []
for num in range(1000, 3001):
    s = str(num)
    if all(int(ch) % 2 == 0 for ch in s):   # kiểm tra tất cả các chữ số đều chẵn
        result.append(s)
print(",".join(result))
