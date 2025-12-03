print("Nguyễn Văn Hùng")
print("245752021610031")

def lay_n_dong_cuoi_cung(ten_tep, n):
    with open(ten_tep, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return lines[-n:]

danh_sach_dong = lay_n_dong_cuoi_cung(r'D:\làm việc\Bài Thực hành KTLT\4.16.py', 3)
for line in danh_sach_dong:
    print(line, end="")
