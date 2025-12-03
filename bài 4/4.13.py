print("Nguyễn Văn Hùng")
print("245752026160031")
danhsach = input("Nhập chuỗi: ").split()
danhsach.append("bin")
for c in danhsach:
    print(c)
print("Vị trí chuỗi 'bin' là:", danhsach.index("bin"))
