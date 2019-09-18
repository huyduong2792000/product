import thaotacfile,loaihanghoa
danhsachhanghoa=thaotacfile.XuLyFileHangHoa.LoadDsHangHoa()
print(danhsachhanghoa)
def KiemTraIDHangHoa(id,danhsachhanghoa):
    for hanghoa in danhsachhanghoa:
        if id==hanghoa['ID']:
            return False
    return True
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
            while True:
                gia_hanghoa=input('nhap gia hang hoa: ')
                try:
                    gia_hanghoa=float(gia_hanghoa)
                    hanghoa_canthem['PRICE']=gia_hanghoa
                    break
                except:
                    print('nhap lai gia hang hoa')
            danhsachloaihanghoa=thaotacfile.XuLyFileLoaiHangHoa.LoadDsLoaiHangHoa()
            while True:
                IDGENERIC=input('nhap id loai hang hoa ')
                check_id=loaihanghoa.KiemTraIDLoaiHangHoa(IDGENERIC,danhsachloaihanghoa)
                if check_id==False:
                    for idxloaihanghoa in danhsachloaihanghoa:
                        if idxloaihanghoa['ID']==IDGENERIC:
                            hanghoa_canthem['GENERIC']=idxloaihanghoa['NAME']
                    break
                else:
                    print('khong tim thay id loai hang hoa nay xin moi nhap lai ')
                    loaihanghoa.XemLoaiHangHoa(danhsachloaihanghoa)
            opject=thaotacfile.XuLyFileHangHoa(hanghoa_canthem)
            opject.AppendFileCsv()
            danhsachhanghoa.append(hanghoa_canthem)
            print('da them hang hoa xong')
            break
    return hanghoa_canthem
def XemHangHoa(danhsachhanghoa):

    print('\033[0;35m+---------------+----------------+------------+-----------+')
    print('|\033[92m \033[1m ID HANG HOA  |  TEN HANG HOA  |  GIA TIEN  |    LOAI   |')
    print('+\033[0;35m---------------+----------------+------------+-----------+')
    for hanghoa in danhsachhanghoa:
        print('|\033[0;33m'+hanghoa['ID'].rjust(len('--------------'),' '),end=' |')
        print(hanghoa['NAME'].rjust(len('---------------'),' '),end=' |')
        print(hanghoa['PRICE'].rjust(len('-----------'),' '),end=' |')
        print(hanghoa['GENERIC'].rjust(len('----------'),' '),end=' |')
        print('\n\033[0;35m+---------------+----------------+------------+-----------+')


