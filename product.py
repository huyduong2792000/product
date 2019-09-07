import os,json
import hoadon
import thaotackhachhang
import loaihanghoa
import nhanvien
import thaotacfile
listhoadon=[{'tenkhachhang': 'adsv', 'ngayhoadon': 12, 'sohoadon': '12', 'hangdamua': [{'tenhang': 'coca', 'dongia': 100000, 'soluong': 20, 'thanhtien': 2000000, 'loaihanghoa': 'do uong'}],'tongtientruocthue':180000, 'tongtiensauthue': 2000000}]
 #lu tru nhieu hoa don cua nhieu khach hang
danhsachloaihanghoa=[{'tenloaihanghoa': 'do uong11111111', 'danhsachhanghoatrongloai': ['pepsi', 'coca']},{'tenloaihanghoa': 'do an', 'danhsachhanghoatrongloai': ['asf', 'dasfsaf']}]
danhsachnhanvien=[{'tennhanvien': 'huy', 'quequan': 'tn', 'tuoi': '20', 'socmnd': '123', 'mucluong': 10.0}]

danhsachloaihanghoa=thaotacfile.LoadDsLoaiHangHoa()
danhsachnhanvien=thaotacfile.LoadDsNhanVien()

def TinhDoanhThuTheoNgay():
    listhoadon=thaotacfile.LoadDsHoaDon()
    while True:
        ngaybatdau=input('nhap ngay bat dau: ')
        ngayketthuc=input('nhap ngay ket thuc: ')
        try:
            ngaybatdau=int(ngaybatdau)
            ngayketthuc=int(ngayketthuc)
            break
        except:
            print('nhap lai ')
    doanhthu=0
    for ngay in listhoadon:
        if (ngay['ngayhoadon'] in range(ngaybatdau,ngayketthuc+1)):
            doanhthu+=ngay['tongtiensauthue']
    print('danh thu tu ngay {0} den ngay {1} la: {2} '.format(ngaybatdau,ngayketthuc,doanhthu))

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

def CapQuyenTruyCap():
    menu('SALESMAN','MANAGER')
    quyentruycap=input('WHO ARE YOU ')
    if quyentruycap=='1':
        return 'nhanvien'
    elif quyentruycap=='2':
        acc=input('nhap account manager: ')
        password=input('nhap password manager: ')
        if (acc=='huyduong' and password=='2792000'):
            return 'quanly'
        elif (acc=='huyclone' and password=='123456'):
            return 'quanlytamthoi'

def QuyenNhanVien():
    menu('TAO HOA DON ','XEM','SUA','XOA')
    luachon=input('nhap lua chon cua ban vao day: ')
    if luachon=='1':
        hoadonmoi=hoadon.Them1HoaDon()
        listhoadon.append(hoadonmoi)
    elif luachon=='2':
        menu('XEM HOA DON ','XEM DANH SACH CAC LOAI HANG HOA')
        luachonxem=input('nhap lua chon cua ban vao day: ')
        if luachonxem=='1':
            sohoadoncanxem=input('nhap so hoa don can xem')
            hoadon.XemHoaDon(sohoadoncanxem)
        elif luachonxem=='2':

            loaihanghoa.XemLoaiHangHoa(danhsachloaihanghoa)
    elif luachon=='3':
        menu('XUA HOA DON')
        sohoadoncanxua=input('nhap so hoa don can xua: ')
        hoadon.XuaHoaDon(sohoadoncanxua)

    elif luachon=='4':
        menu('XOA HOA DON ')
        sohoadoncanxoa=input('nhap so hoa don can xoa: ')
        hoadon.XoaHoaDon(sohoadoncanxoa)

# doan code duoi danh cho quan ly
def QuyenQuanLy():
    menu('TAO            ','XEM','XUA','XOA')
    luachon=input('nhap lua chon cua ban vao day: ')
    if luachon=='1':
        menu('THEM HOA DON ','THEM LOAI HANG HOA','THEM NHAN VIEN','TAO DANH SACH KHACH HANG THAN THIET')
        luachonthem=input('nhap lua chon cua ban vao day ')
        if luachonthem=='1':
            hoadonmoi=hoadon.Them1HoaDon()
            listhoadon.append(hoadonmoi)
            loaihanghoa.TaoLoaiHangHoa(hanghoa['loaihanghoa'],hanghoa['tenhang'])
        elif luachonthem=='2':
            loaihanghoa.ThemLoaiHangHoaTrucTiep()
        elif luachonthem=='3':
            nhanvien.ThemNhanVien(danhsachnhanvien)
        elif luachonthem=='4':
            while True:
                sotientoithieu=input('nhap so tien toi thieu de loc: ')
                try:
                    sotientoithieu=float(sotientoithieu)
                    break
                except:
                    print('xin moi nhap lai so tien toi thieu: ')
            thaotackhachhang.TaoDanhSachKhachHangThanThiet(sotientoithieu,listhoadon)
    elif luachon=='2':
        menu('XEM HOA DON ','XEM DANH SACH CAC LOAI HANG HOA','XEM DOANH THU TU NGAY A DEN NGAY B','XEM DANH SACH KHACH HANG','XEM DANH SACH NHAN VIEN')
        luachonxem=input('nhap lua chon cua ban vao day: ')
        if luachonxem=='1':
            sohoadoncanxem=input('nhap so hoa don can xem') 
            hoadon.XemHoaDon(sohoadoncanxem)
        elif luachonxem=='2':
            loaihanghoa.XemLoaiHangHoa(danhsachloaihanghoa)
        elif luachonxem=='3':
            TinhDoanhThuTheoNgay()
        elif luachonxem=='4':
            thaotackhachhang.XemDanhSachKhachHang(listhoadon)
        elif luachonxem=='5':
            nhanvien.XemDanhSachNhanVien(danhsachnhanvien)
    elif luachon=='3':
        menu('XUA HOA DON','XUA NHAN VIEN')
        luachonxua=input('nhap lua chon cua ban vao day: ')
        if luachonxua=='1':
            sohoadoncanxua=input('nhap so hoa don can xua: ')
            hoadon.XuaHoaDon(sohoadoncanxua)
        elif luachonxua=='2':
            nhanvien.XuaNhanVien()
    elif luachon=='4':
        menu('XOA HOA DON ','XOA NHAN VIEN')
        luachonxoa=input('nhap lua chon cua ban vao day: ')
        if luachonxoa=='1':
            sohoadoncanxoa=input('nhap so hoa don can xoa: ')
            hoadon.XoaHoaDon(sohoadoncanxoa)
        elif luachonxoa=='2':
            socmnd_nvcanxoa=input('nhap so cmnd cua nhan vien can xoa: ')
            nhanvien.XoaNhanVien(socmnd_nvcanxoa)
while True:
    quyentruycap=CapQuyenTruyCap()
    if quyentruycap=='nhanvien': QuyenNhanVien()
    elif quyentruycap=='quanly':QuyenQuanLy()
    luachon=input('\33[36mban co muon thoat khong( bam "c" de ket thuc): ')
    if luachon=='c':break
#thaotacfile.GhiFileLoaiHangHoa(danhsachloaihanghoa)
#thaotacfile.GhiFileNhanVien(danhsachnhanvien)
