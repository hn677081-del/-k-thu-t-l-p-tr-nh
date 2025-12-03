print("Nguyễn Văn Hùng")
print("2455752021610031")
tu_tieng_anh = input("Nhập từ tiếng Anh viết tách nhau bằng dấu cách: ")
tutienganh_chuoi = tu_tieng_anh.split()
sap_xep = sorted(tutienganh_chuoi)
for tu in sap_xep:
    print(tu)
