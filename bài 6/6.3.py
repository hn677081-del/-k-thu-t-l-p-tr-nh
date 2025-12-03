print("Nguyễn Văn Hùng")
print("248752021610031")
class GioiTinh(object):
    def getGender(self):
        return "unknown"
class Nam(GioiTinh):
    def getGender(self):
        return "nam"
class Nu(GioiTinh):
    def getGender(self):
        return "nu"
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
