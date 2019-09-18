import thaotacfile,quanlyuser
danhsachhoadon=[]
danhsachloaihanghoa=[]
danhsachuser=[]
danhsachhanghoa=[]
danhsachhangtonkho=[]
# def Load(danhsachloaihanghoa=None,danhsachuser=None,danhsachhanghoa=None,danhsachhoadon=None,danhsachhangtonkho=None):
#     if danhsachhanghoa is not None:
#         danhsachhanghoa = thaotacfile.XuLyFileHangHoa.LoadDsHangHoa()
#     if danhsachloaihanghoa is not None:
#         danhsachloaihanghoaload=thaotacfile.XuLyFileLoaiHangHoa.LoadDsLoaiHangHoa()
#     if danhsachuser is not None:
#         danhsachnhanvien=thaotacfile.XuLyFileNhanVien.LoadDsNhanVien()
#     if dnahsachhoadon is not None:
#         danhsachhoadon=thaotacfile.XuLyFileHoaDon.LoadDsHoaDon()
#     if danhsachhangtonkho is not None:
#         danhsachhangtonkho=thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
danhsachuser=thaotacfile.XuLyFileUser.LoadDsUser()
def menu(*tenchucnang):
    chuoi_dai_nhat=0
    for timchieudaichuoi in tenchucnang:
        if len(timchieudaichuoi) > chuoi_dai_nhat:
            chuoi_dai_nhat=len(timchieudaichuoi)
    print('+'+'+'.rjust(chuoi_dai_nhat+5,'-')+'+----+')
    i=1
    try:
        for idx in tenchucnang:
            print('|'+idx.ljust(chuoi_dai_nhat+5,' ')+'|'+str(i).rjust(4,' ')+'|')
            print('+'+'+'.rjust(chuoi_dai_nhat+5,'-')+'+----+')
            i+=1
    except:
        for idx in tenchucnang[0]:
            print('|'+idx.rjust(chuoi_dai_nhat+5,' ')+'|'+str(i).rjust(4,' ')+'|')
            print('+'+'+'.rjust(chuoi_dai_nhat+5,'-')+'+----+')
            i+=1
def Tao():
    menu('TAO HOA DON','TAO HANG HOA','TAO LOAI HANG HOA')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':

def ChucNang():
    menu('')
while True:
    print('WELCOME TO APP')
    menu('DANG NHAP ','TAO TAI KHOAN ')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':
        check_login=quanlyuser.LogIn(danhsachuser)
        if check_login==True:
            pass
        else:
            continue
    elif chon=='2':

