import thaotacfile,loaihanghoa,khohang
def KiemTraIDHangHoa(id,danhsachhanghoa):
    for hanghoa in danhsachhanghoa:
        if id==hanghoa['ID']:
            return False
    return True
def ThemHangHoaVaoFile(data,danhsachhanghoa):
    data['PRICE'] = str(data['PRICE'])
    data['soluong']=str(data['soluong'])
    opject = thaotacfile.XuLyFileHangHoa(data)
    opject.AppendFileCsv()
    danhsachhanghoa.append(data)
    print('da them hang hoa xong')
def KhaiBaoGiaHangHoa():
    while True:
        gia_hanghoa = input('nhap gia hang hoa: ')
        try:
            gia_hanghoa = float(gia_hanghoa)
            break
        except:
            print('nhap lai gia hang hoa')

    return gia_hanghoa
def KhaiBaoSLHangHoa():
    while True:
        soluong_hanghoa = input('nhap so luong hang hoa nay: ')
        try:
            soluong_hanghoa = int(soluong_hanghoa)
            break
        except:
            print('nhap lai so luong them vao kho')
    return soluong_hanghoa
def KhaiBaoLoaiHangHoa(danhsachhanghoa):
    danhsachloaihanghoa = thaotacfile.XuLyFileLoaiHangHoa.LoadDsLoaiHangHoa()
    while True:
        id_loaihanghoa = input('nhap id loai hang hoa ')
        check_id = loaihanghoa.KiemTraIDLoaiHangHoa(id_loaihanghoa, danhsachloaihanghoa)
        if check_id == False:
            for idxloaihanghoa in danhsachloaihanghoa:
                if idxloaihanghoa['ID'] == id_loaihanghoa:
                    return idxloaihanghoa['NAME']
        else:
            print('khong tim thay id loai hang hoa nay xin moi nhap lai ')
            loaihanghoa.XemLoaiHangHoa(danhsachloaihanghoa)

def TaoHangHoa(danhsachhanghoa):
    while True:
        id=input('nhap id hang hoa can them: ')
        check_id=KiemTraIDHangHoa(id,danhsachhanghoa)
        if check_id==False:
            print('ID nay da duoc su dung vui long nhap ID khac ')
        elif check_id==True:
            hanghoa_canthem = {}
            hanghoa_canthem['ID']=id
            hanghoa_canthem['NAME']=input('nhap ten hang hoa can them ')
            hanghoa_canthem['PRICE']=KhaiBaoGiaHangHoa()
            hanghoa_canthem['soluong']=KhaiBaoSLHangHoa()
            hanghoa_canthem['loaihanghoa']=KhaiBaoLoaiHangHoa(danhsachhanghoa)
            danhsachhanghoa.append(hanghoa_canthem)
            ThemHangHoaVaoFile(hanghoa_canthem,danhsachhanghoa)
            danhsachhangtrongkho = thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
            khohang.NhapKho(danhsachhangtrongkho,hanghoa_canthem['ID'],hanghoa_canthem['soluong'])
            break
    return hanghoa_canthem
def XemHangHoa(danhsachhanghoa):
    danhsachhanghoa=thaotacfile.XuLyFileHangHoa.LoadDsHangHoa()
    print('\033[0;35m+---------------+----------------+------------+-----------+')
    print('|\033[92m \033[1m ID HANG HOA  |  TEN HANG HOA  |  GIA TIEN  |    LOAI   |')
    print('+\033[0;35m---------------+----------------+------------+-----------+')
    for hanghoa in danhsachhanghoa:
        print('|\033[0;33m'+hanghoa['ID'].rjust(len('--------------'),' '),end=' |')
        print(hanghoa['NAME'].rjust(len('---------------'),' '),end=' |')
        print(str(hanghoa['PRICE']).rjust(len('-----------'),' '),end=' |')
        print(hanghoa['loaihanghoa'].rjust(len('----------'),' '),end=' |')
        print('\n\033[0;35m+---------------+----------------+------------+-----------+')
def TimHangBanChayTheoSoLuong():
    danhsachhangbanduoc=thaotacfile.LoadFileHangBanDuoc()
    soluongmax=['',0]
    for hangbanduoc in danhsachhangbanduoc:
        if hangbanduoc['soluong']>soluongmax[1]:
            soluongmax[1]=hangbanduoc['soluong']
            soluongmax[0]=hangbanduoc['ID']
    print('hang ban duoc so luong nhieu nhat la: ',soluongmax[0])
    print('so luong hang hoa nay da ban duoc la: ',soluongmax[1])
    return soluongmax
def TimGiaHangHoa(id,danhsachhanghoa):
    for hanghoa in danhsachhanghoa:
        if id==hanghoa['ID']:
            return hanghoa['PRICE']
def TimHangBanChayTheoDoanhThu():
    danhsachhanghoa=thaotacfile.XuLyFileHangHoa.LoadDsHangHoa()
    danhsachhangbanduoc = thaotacfile.LoadFileHangBanDuoc()
    doanhthumax=['',0]
    for hangbanduoc in danhsachhangbanduoc:
        price=TimGiaHangHoa(hangbanduoc['ID'],danhsachhanghoa)
        if price*hangbanduoc['soluong']>doanhthumax[1]:
            doanhthumax[1]=price*hangbanduoc['soluong']
            doanhthumax[0]=hangbanduoc['ID']
    print('doanh thu cua hang hoa lon nhat la ',doanhthumax[0])
    print('tong doanh thu cua hang hoa nay la: ',doanhthumax[1])
    return doanhthumax
if __name__=='__main__':
    TimHangBanChayTheoDoanhThu()
    TimHangBanChayTheoSoLuong()

