import thaotacfile,quanlyuser,hoadon,thaotachanghoa,loaihanghoa,thaotackhachhang,khohang,test
danhsachhoadon=[]
danhsachloaihanghoa=[]
danhsachuser=[]
danhsachhanghoa=[]
danhsachhangtonkho=[]
listhoadon=[]
danhsachhanghoa=thaotacfile.XuLyFileHangHoa.LoadDsHangHoa()
danhsachhangtrongkho=thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
danhsachuser=thaotacfile.XuLyFileUser.LoadDsUser()
danhsachloaihanghoa=thaotacfile.XuLyFileLoaiHangHoa.LoadDsLoaiHangHoa()
listhoadon=thaotacfile.XuLyFileHoaDon.LoadDsHoaDon()
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
        hoadon.Them1HoaDon(danhsachhanghoa,danhsachhangtrongkho,listhoadon)
    elif chon=='2':
        thaotachanghoa.TaoHangHoa(danhsachhanghoa)
    elif chon=='3':
        loaihanghoa.TaoLoaiHangHoa(danhsachloaihanghoa)
def Xem():
    menu('XEM HOA DON','XEM DANH SACH LOAI HANG HOA','XEM DANH SACH HANG HOA','XEM DANH SACH KHACH HANG','XEM DANH SACH KHACH HANG THAN THIET')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':
        sohoadoncanxem=input('nhap so hoa don can xem: ')
        hoadon.XemHoaDon(sohoadoncanxem)
    elif chon=='2':
        loaihanghoa.XemLoaiHangHoa(danhsachloaihanghoa)
    elif chon=='3':
        thaotachanghoa.XemHangHoa(danhsachhanghoa)
    elif chon=='4':
        thaotackhachhang.XemDanhSachKhachHang(listhoadon)
    elif chon=='5':
        sotien_toithieu=float(input('nhap so tien toi thieu de loc '))
        thaotackhachhang.TaoDanhSachKhachHangThanThiet(sotien_toithieu,listhoadon)
def Xua():
    menu('XUA HOA DON','XUA THONG TIN TAI KHOAN')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':
        sohoadon_canxua=input('nhap so hoa don can xua ')
        hoadon.XuaHoaDon(sohoadon_canxua,danhsachhanghoa,danhsachhangtrongkho,listhoadon)
    elif chon=='2':
        quanlyuser.EditUser(danhsachuser)
def Xoa():
    menu('XOA HOA DON','XOA TAI KHOAN')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':
        sohoadon_canxoa=input('nhap so hoa don can xoa ')
        hoadon.XoaHoaDon(sohoadon_canxoa,listhoadon)
    elif chon=='2':
        quanlyuser.DeleteUser(danhsachuser)
def Khac():
    menu('NHAP KHO','TIM HANG BAN CHAY THEO DOANH THU','TIM HANG BAN CHAY THEO SL','XEM SL KHAC HANG','BIEU DO SL')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':
        khohang.NhapKho(danhsachhangtrongkho)
    elif chon=='2':
        thaotachanghoa.TimHangBanChayTheoDoanhThu()
    elif chon=='3':
        thaotachanghoa.TimHangBanChayTheoSoLuong()
    elif chon=='4':
        print('so luong khach hang la: ',len(thaotackhachhang.XemDanhSachKhachHang(listhoadon)))
    elif chon=='5':
        test.display()
def LuaChon():
    menu('TAO','XEM','XUA','XOA','KHAC','DANG XUAT')
    chon=input('nhap lua chon cua ban vao day ')
    if chon=='1':
        Tao()
    elif chon=='2':
        Xem()
    elif chon=='3':
        Xua()
    elif chon=='4':
        Xoa()
    elif chon=='5':
        Khac()
    elif chon=='6':
        if quanlyuser.LogUot()==True:
            return False
        else:
            pass
while True:
    print('WELCOM TO APP BY HUYDUONG')
    menu('DANG NHAP','TAO TAI KHOAN','QUEN MAT KHAU')
    chon=input('nhap lua chon cua ban vao day: ')
    if chon=='1':
        log=quanlyuser.LogIn(danhsachuser)
        if log==False:
            print('tao tai khoan hoac mat khau sai ')
        else:
            while True:
                if LuaChon()==False:
                    break
    elif chon=='2':
        quanlyuser.CreateUser(danhsachuser)
    elif chon=='3':
        quanlyuser.ReadUser(danhsachuser)