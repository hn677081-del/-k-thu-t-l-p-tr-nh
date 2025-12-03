print("Nguyễn Văn Hùng")
print("245752021610031")
s = input("Nhập chuỗi: ")
for ch in s:
    if ch == " " or ch == "\t":
        continue   # Bỏ qua không in ký tự này
    print(ch)
