import thaotacfile,os
danhsachnhanvien=thaotacfile.LoadDsNhanVien()
def KiemTraSoCmnd(socmnd):
    kiemtra=os.listdir('dirtree/thang1/danhsachnhanvien')
    if (socmnd+'.json') in kiemtra:
        print('so cmnd nay da ton tai xin moi nhap so khac: ')
        return False
    return True
def ThemNhanVien(danhsachnhanvien):
    tennhanvien=input('nhap ten nhan vien: ')
    quequan=input('nhap que quan nhan vien: ')
    tuoi=input('nhap tuoi nhan vien: ')
    while True:
        socmnd=input('nhap so cmnd cua nhan vien: ')
        if KiemTraSoCmnd(socmnd) ==True:break
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
    thaotacfile.TaoFileNhanVien(nhanvien,socmnd)
    return nhanvien
def XuaNhanVien():
    socmnd_nvcanxua=input('nhap so cmnd cua nhan vien can xua: ')
    kiemtra=os.listdir('dirtree/thang1/danhsachnhanvien')
    if (socmnd_nvcanxua+'.json') in kiemtra:
        pass
    else:
        print('\33[91mkhong co so cmnd nay ')
        print('\33[92m')
        return

    XoaNhanVien(socmnd_nvcanxua)
    nhanvien_canxua=ThemNhanVien(danhsachnhanvien)
    for idx in range(len(danhsachnhanvien)):
        if danhsachnhanvien[idx]['socmnd']==socmnd_nvcanxua:
            danhsachnhanvien[idx]=nhanvien_canxua
            danhsachnhanvien.pop()
            thaotacfile.TaoFileNhanVien(nhanvien_canxua,nhanvien_canxua['socmnd'])
            return
def XemDanhSachNhanVien(danhsachnhanvien):
    thaotacfile.LoadDsNhanVien(danhsachnhanvien)
    print('+------------------------+----------------+-----------+--------------+----------------+')
    print('|     TEN NHAN VIEN      |     QUE QUAN   |    TUOI   |    SO CMND   |    MUC LUONG   |')
    print('+------------------------+----------------+-----------+--------------+----------------+')
    for nhanvien in danhsachnhanvien:
        print('|'+nhanvien['tennhanvien'].rjust(24,' ')+'|'+nhanvien['quequan'].rjust(16,' ')+'|'+nhanvien['tuoi'].rjust(11,' ')+'|'+nhanvien['socmnd'].rjust(14,' ')+'|'+str(nhanvien['mucluong']).rjust(16,' ')+'|')
        print('+------------------------+----------------+-----------+--------------+----------------+')
def XoaNhanVien(so_cmnd_canxoa):
    for idx in range(len(danhsachnhanvien)):
        if danhsachnhanvien[idx]['socmnd']==so_cmnd_canxoa:
            danhsachnhanvien.pop(idx)
            thaotacfile.XoaFileNhanVien(so_cmnd_canxoa)
            return
