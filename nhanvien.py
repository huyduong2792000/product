import thaotacfile,os
danhsachnhanvien=thaotacfile.XuLyFileNhanVien.LoadDsNhanVien()
def KiemTraSoCmnd(socmnd):
    kiemtra=os.listdir('dirtree/thang1/danhsachnhanvien')
    if (socmnd+'.json') in kiemtra:
        return False
    return True
def ThemNhanVien(danhsachnhanvien):
    tennhanvien=input('nhap ten nhan vien: ')
    quequan=input('nhap que quan nhan vien: ')
    tuoi=input('nhap tuoi nhan vien: ')
    while True:
        socmnd=input('nhap so cmnd cua nhan vien: ')
        if KiemTraSoCmnd(socmnd) ==True:
            break
        else:
            print('so cmnd nay da ton tai xin moi nhap so cmnd khac')
    while True:
        mucluong=input('\33[91mnhap muc luong(muc luong phai la so): ')
        try:
            mucluong=float(mucluong)
            break
        except:
            print('nhap lai muc luong: ')
    nhanvien={
        'tennhanvien':tennhanvien,
        'quequan':quequan,
        'tuoi':tuoi,
        'socmnd':socmnd,
        'mucluong':mucluong}
    danhsachnhanvien.append(nhanvien)
    opject=thaotacfile.XuLyFileNhanVien(nhanvien)
    opject.MakeFileJson()
    return nhanvien
def XuaNhanVien(danhsachnhanvien):
    while True:
        socmnd_nvcanxua = input('nhap so cmnd cua nhan vien can xua: ')
        check_cmnd=KiemTraSoCmnd(socmnd_nvcanxua)
        if check_cmnd==True:
            print('khong tim thay so cmnd nay')
        else:
            break
    danhsachnhanvien_copy=danhsachnhanvien*1
    print('NHAP THONG TIN MOI')
    nhanvien_canxua=ThemNhanVien(danhsachnhanvien_copy)
    opject = thaotacfile.XuLyFileNhanVien(data=nhanvien_canxua,filename=socmnd_nvcanxua)
    for idx in range(len(danhsachnhanvien_copy)):
        if danhsachnhanvien_copy[idx]['socmnd']==socmnd_nvcanxua:
            danhsachnhanvien_copy[idx]=nhanvien_canxua
            danhsachnhanvien_copy.pop()
            break
    chon=input('ban co chac chan muon xua nhan vien nay khong( nhap c de dong y): ')
    if chon=='c':
        danhsachnhanvien.clear()
        danhsachnhanvien.extend(danhsachnhanvien_copy)
        opject.RemoveFile()
    else:
        return
def XemDanhSachNhanVien(danhsachnhanvien):
    print('+------------------------+----------------+-----------+--------------+----------------+')
    print('|     TEN NHAN VIEN      |    QUE QUAN    |    TUOI   |   SO CMND    |    MUC LUONG   |')
    print('+------------------------+----------------+-----------+--------------+----------------+')
    for nhanvien in danhsachnhanvien:
        print('|'+nhanvien['tennhanvien'].rjust(24,' ')+'|'+nhanvien['quequan'].rjust(16,' ')+'|'+nhanvien['tuoi'].rjust(11,' ')+'|'+nhanvien['socmnd'].rjust(14,' ')+'|'+str(nhanvien['mucluong']).rjust(16,' ')+'|')
        print('+------------------------+----------------+-----------+--------------+----------------+')
def XoaNhanVien(danhsachnhanvien):
    danhsachnhanvien_copy=danhsachnhanvien*1
    while True:
        socmnd_nvcanxoa = input('nhap so cmnd cua nhan vien can xoa: ')
        check_cmnd=KiemTraSoCmnd(socmnd_nvcanxoa)
        if check_cmnd==True:
            print('khong tim thay so cmnd nay')
            return
        else:
            print('da tim thay nhan vien')
            break
    for idx in range(len(danhsachnhanvien_copy)):
        if danhsachnhanvien_copy[idx]['socmnd']==socmnd_nvcanxoa:
            danhsachnhanvien_copy.pop(idx)
            break
    chose=input('ban co muon xoa nhan vien nay khong( an c de xoa): ')
    if chose.lower()=='c':
        danhsachnhanvien.clear()
        danhsachnhanvien.extend(danhsachnhanvien_copy)
        opject=thaotacfile.XuLyFileNhanVien(filename=socmnd_nvcanxoa)
        opject.RemoveFile()

if __name__=='__main__':
    XemDanhSachNhanVien(danhsachnhanvien)