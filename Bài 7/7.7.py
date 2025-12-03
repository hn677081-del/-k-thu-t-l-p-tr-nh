print("Nguyễn Văn Hùng")
print("245752021610031")

def demsodong(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return len(lines)

print("Tổng số dòng là:", demsodong(r'D:\làm việc\Bài Thực hành KTLT\6.4.py'))
