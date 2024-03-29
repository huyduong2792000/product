import json,thaotacfile,thaotackhachhang,thaotachanghoa,khohang
danhsachhanghoa=thaotacfile.XuLyFileHangHoa.LoadDsHangHoa()
danhsachhangtrongkho=thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
def TongTien(danhsach_hanghoa_tronghoadon,thue):
    tongtientruocthue=0
    tongtiensauthue=0
    for thanhtien in danhsach_hanghoa_tronghoadon:
        tongtientruocthue+=thanhtien['thanhtien']
    tongtiensauthue=tongtientruocthue+tongtientruocthue*thue/100
    return tongtientruocthue,tongtiensauthue

def Them1HoaDon(danhsachhanghoa,danhsachhangtrongkho,listhoadon):
    khachhang={}
    thaotackhachhang.NhapKhachhang(khachhang)
    hanghoa={}
    danhsach_hanghoa_tronghoadon=[]
    while True:
        NhapHangHoa(hanghoa,danhsachhanghoa,danhsachhangtrongkho)
        danhsach_hanghoa_tronghoadon.append(hanghoa.copy())
        khachhang['hangdamua'] = danhsach_hanghoa_tronghoadon * 1
        khachhang['tongtientruocthue'],khachhang['tongtiensauthue']=TongTien(danhsach_hanghoa_tronghoadon,khachhang['thue'])
        print('\33[92mban co muon nhap nua khong( an k de thoat)')
        chon = input()
        if chon == 'k':
            listhoadon.append(khachhang)
            opject=thaotacfile.XuLyFileHoaDon(khachhang)
            opject.MakeFileJson()
            return khachhang

def XemHoaDon(sohoadoncanxem):
    thongtinhoadon = {}
    with open('dirtree/thang1/danhsachhoadon/'+sohoadoncanxem+'.json') as rfile:
        thongtinhoadon = json.load(rfile)
    STT=0
    try:
        print('\33[93mso hoa don: '+str(thongtinhoadon['sohoadon']))
    except:return
    print('ngay hoa don: '+str(thongtinhoadon['ngayhoadon']))
    print('ten khach hang: '+str(thongtinhoadon['tenkhachhang']))
    print('+-----+--------------+----------+---------+---------------+------------+')
    print('| STT | TEN HANG HOA | SO LUONG | DON GIA | LOAI HANG HOA | THANH TIEN |')
    print('+-----+--------------+----------+---------+---------------+------------+')
    for hanghoa in thongtinhoadon['hangdamua']:
        STT+=1
        print('|'+str(STT).rjust(5,' ')+'|'+str(hanghoa['ID']).rjust(14,' ')+'|'+str(hanghoa['soluong']).rjust(10,' ')+'|'+str(hanghoa['dongia']).rjust(9,' ')+'|'+str(hanghoa['loaihanghoa']).rjust(len('---------------'),' ')+'|'+str(hanghoa['thanhtien']).rjust(12,' ')+'|')
        print('+-----+--------------+----------+---------+---------------+------------+')
    print('|                                    TONG TIEN TRUOC THUE |'+str(thongtinhoadon['tongtientruocthue']).rjust(12,' ')+'|')
    print('+-----+--------------+----------+---------+---------------+------------+')
    print('|                                      TONG TIEN SAU THUE |'+str(thongtinhoadon['tongtiensauthue']).rjust(12,' ')+'|')
    print('+-----+--------------+----------+---------+---------------+------------+')
    print('                        -- design by huy duong --                       ')
def NhapHangHoa(hanghoa,danhsachhanghoa,danhsachhangtrongkho):
    while True:
        idhanghoa=input('nhap id hang hoa can them: ')
        check_id=thaotachanghoa.KiemTraIDHangHoa(idhanghoa,danhsachhanghoa)
        if check_id==False:
            break
        else:
            print('khong tin thay ID nay xin moi nhap lai ')

    for idxhanghoa in danhsachhanghoa:
        if idxhanghoa['ID']==idhanghoa:
            break
    hanghoa['ID'] = idhanghoa
    hanghoa['dongia']=float(idxhanghoa['PRICE'])
    hanghoa['loaihanghoa']=idxhanghoa['loaihanghoa']
    while True:
        soluong=input('nhap so luong hang hoa ')
        try:
            soluong=int(soluong)
            hanghoa['soluong']=soluong
            break
        except:
            print('xin moi nhap lai so luong ')
    khohang.HoaDonXuatKho(idhanghoa, soluong, danhsachhangtrongkho)
    hanghoa['thanhtien'] = hanghoa['dongia'] * hanghoa['soluong']
def KiemTraSoHoaDon(sohoadoncankiemtra,listhoadon):
    for idx in range(len(listhoadon)):
        if listhoadon[idx]['sohoadon']==sohoadoncankiemtra:
            return listhoadon[idx]
    return False
def XuaHoaDon(sohoadoncanxua,danhsachhanghoa,danhsachhangtrongkho,listhoadon):
    XoaHoaDon(sohoadoncanxua,listhoadon)
    print('\33[33mNHAP THONG TIN HOA DON MOI')
    Them1HoaDon(danhsachhanghoa,danhsachhangtrongkho,listhoadon)
    return

def XoaHoaDon(sohoadoncanxoa,listhoadon):
    check=KiemTraSoHoaDon(sohoadoncanxoa,listhoadon)
    if check!=False:
        listhoadon.remove(check)
        opject = thaotacfile.XuLyFileHoaDon(filename=sohoadoncanxoa)
        opject.RemoveFile()
        print('da xoa xong ')
    else:
        print('khong tim thay so hoa don nay ')
    return

if __name__=='__main__':
    Them1HoaDon(danhsachhanghoa,danhsachhangtrongkho)