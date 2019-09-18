import thaotacfile
danhsachloaihanghoa=thaotacfile.XuLyFileLoaiHangHoa.LoadDsLoaiHangHoa()
def KiemTraIDLoaiHangHoa(id,danhsachloaihanghoa):
    for loaihanghoa in danhsachloaihanghoa:
        if id==loaihanghoa['ID']:
            return False
    return True
#main start
def TaoLoaiHangHoa (danhsachloaihanghoa):
    while True:
        id=input('nhap id loai hang hoa can them: ')
        check_id=KiemTraIDLoaiHangHoa(id,danhsachloaihanghoa)
        if check_id==False:
            print('ID nay da duoc su dung vui long nhap ID khac ')
        elif check_id==True:
            loai_hanghoa_canthem = {}
            loai_hanghoa_canthem['ID']=id
            loai_hanghoa_canthem['NAME']=input('nhap ten loai hang hoa can them ')
            opject=thaotacfile.XuLyFileLoaiHangHoa(loai_hanghoa_canthem)
            opject.AppendFileCsv()
            danhsachloaihanghoa.append(loai_hanghoa_canthem)
            print('da them loai hang hoa xong')
            break
def XemLoaiHangHoa(danhsachloaihanghoa):
    for idx in danhsachloaihanghoa:
        print ('\033[0;33m'+idx['ID']+'\033[0;35m '+idx['NAME'])
#main end
if __name__ == '__main__':
    XemLoaiHangHoa(danhsachloaihanghoa)