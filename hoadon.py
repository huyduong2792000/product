import os,thaotacfile,thaotackhachhang,loaihanghoa

def TongTien(danhsach_hanghoa_tronghoadon,thue):
    tongtientruocthue=0
    tongtiensauthue=0
    for thanhtien in danhsach_hanghoa_tronghoadon:
        tongtientruocthue+=thanhtien['thanhtien']
    tongtiensauthue=tongtientruocthue+tongtientruocthue*thue/100
    return tongtientruocthue,tongtiensauthue

def Them1HoaDon():
    khachhang={}
    thaotackhachhang.NhapKhachhang(khachhang)
    hanghoa={}
    danhsach_hanghoa_tronghoadon=[]
    while True:
        NhapHangHoa(hanghoa)
        danhsach_hanghoa_tronghoadon.append(hanghoa.copy())
        khachhang['hangdamua'] = danhsach_hanghoa_tronghoadon * 1
        khachhang['tongtientruocthue'],khachhang['tongtiensauthue']=TongTien(danhsach_hanghoa_tronghoadon,khachhang['thue'])
        print('\33[92mban co muon nhap nua khong( an k de thoat)')
        #danhsach_hanghoa_tronghoadon.clear()
        chon = input()
        if chon == 'k':
            thaotacfile.TaoFileHoaDon(khachhang,khachhang['sohoadon'])
            return khachhang
            break

def XemHoaDon(sohoadoncanxem):
    thongtinhoadon=thaotacfile.XemFileHoaDon(sohoadoncanxem)
    STT=0
    try:
        print('\33[93mso hoa don: '+str(thongtinhoadon['sohoadon']))
    except:return
    print('ngay hoa don: '+str(thongtinhoadon['ngayhoadon']))
    print('ten khach hang: '+str(thongtinhoadon['tenkhachhang']))
    print('+-----+--------------+----------+---------+------------+')
    print('| STT | TEN HANG HOA | SO LUONG | DON GIA | THANH TIEN |')
    print('+-----+--------------+----------+---------+------------+')
    for hanghoa in thongtinhoadon['hangdamua']:
        STT+=1
        print('|'+str(STT).rjust(5,' ')+'|'+str(hanghoa['tenhang']).rjust(14,' ')+'|'+str(hanghoa['soluong']).rjust(10,' ')+'|'+str(hanghoa['dongia']).rjust(9,' ')+'|'+str(hanghoa['thanhtien']).rjust(12,' ')+'|')
        print('+-----+--------------+----------+---------+------------+')
    print('|                     TONG TIEN TRUOC THUE|'+str(thongtinhoadon['tongtientruocthue']).rjust(12,' ')+'|')
    print('+-----+--------------+----------+---------+------------+')
    print('|                       TONG TIEN SAU THUE|'+str(thongtinhoadon['tongtiensauthue']).rjust(12,' ')+'|')
    print('+-----+--------------+----------+---------+------------+')
    print('               -- design by huy duong --                ')


def NhapHangHoa(hanghoa):
    danhsachloaihanghoa=thaotacfile.LoadDsLoaiHangHoa()
    hanghoa['tenhang']=input('nhap ten hang ')
    while True:
        dongia=input('nhap don gia( nhap so) ')
        soluong=input('nhap so luong( nhap so) ')
        try:
            dongia=int(dongia)
            soluong=int(soluong)
            break
        except:
            print('don gia va so luong phai la so')
    hanghoa['dongia']=dongia
    hanghoa['soluong']=soluong
    hanghoa['thanhtien']=hanghoa['dongia']*hanghoa['soluong']
    hanghoa['loaihanghoa']=input('nhap loai hang hoa')
    loaihanghoa.TaoLoaiHangHoa(hanghoa['loaihanghoa'],hanghoa['tenhang'],danhsachloaihanghoa)
def XuaHoaDon(sohoadoncanxua):
    XoaHoaDon(sohoadoncanxua)
    print('\33[33mNHAP THONG TIN HOA DON MOI')
    tmp=Them1HoaDon()
    thaotacfile.TaoFileHoaDon(tmp,tmp['sohoadon'])
    return

def XoaHoaDon(sohoadoncanxoa):
    thaotacfile.XoaFileHoaDon(sohoadoncanxoa)
    return

