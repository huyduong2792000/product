import json,os
def TaoFileHoaDon(thongtin_hoadon,tenhoadon):
    with open('dirtree/thang1/danhsachhoadon/'+str(tenhoadon)+'.json','w') as wfile:
        json.dump(thongtin_hoadon,wfile)
#def XuaFileHoaDon(thongtin_hoadon,tenhoadoncu,tenhoadonmoi)
def XoaFileHoaDon(tenhoadon_canxoa):
    try:
        os.remove('dirtree/thang1/danhsachhoadon/'+str(tenhoadon_canxoa)+'.json')
        XapXepFile('dirtree/thang1/danhsachhoadon/'+str(tenhoadon_canxoa)+'.json')
    except:print('khong co hoa don nay')
def XemFileHoaDon(sohoadon_canxem):
    try:
        with open('dirtree/thang1/danhsachhoadon/'+str(sohoadon_canxem)+'.json','r') as rfile:
            thongtinhoadon=json.load(rfile)
    except:
        print('\33[91mkhong co hoa don nay')
        return
    return thongtinhoadon
def LoadDsHoaDon():
    listhoadon=[]
    danhsachtenhoadon=os.listdir('dirtree/thang1/danhsachhoadon')
    for tenhoadon in danhsachtenhoadon:
        with open('dirtree/thang1/danhsachhoadon/'+str(tenhoadon),'r') as rfile:
            f=json.load(rfile)
            listhoadon.append(f)
    return listhoadon


def XapXepFile(tenfile):
    with open(str(tenfile), "r") as f:
        lines = f.readlines()
    with open(str(tenfile), "w") as f:
        for line in lines:
            if line.strip("\n") != "\n":
                f.write(line)


def LoadDsLoaiHangHoa():
    danhsachloaihanghoa=[]
    try:
        with open('dirtree/thang1/danhsachloaihanghoa/danhsachloaihanghoa.json','r') as rfile:
            danhsachloaihanghoa=json.load(rfile)
        return danhsachloaihanghoa
    except:
        print('load danh sach loai hang hoa khong thang cong')
def GhiFileLoaiHangHoa(danhsachloaihanghoa):
    with open('dirtree/thang1/danhsachloaihanghoa/danhsachloaihanghoa.json','w') as wfile:
        json.dump(danhsachloaihanghoa,wfile)

def TaoFileNhanVien(thongtinnhanvien,socmnd):
    with open('dirtree/thang1/danhsachnhanvien/'+str(socmnd)+'.json','w') as wfile:
        json.dump(thongtinnhanvien,wfile)
def LoadDsNhanVien():
    danhsachnhanvien=[]
    try:
        danhsach_cmndnhanvien=os.listdir('dirtree/thang1/danhsachnhanvien')
    except:
        print('khong tim thay file danhsachnhanvien')
        return
    for socmnd in danhsach_cmndnhanvien:
        with open('dirtree/thang1/danhsachnhanvien/'+str(socmnd),'r') as rfile:
            f=json.load(rfile)
            danhsachnhanvien.append(f)
    return danhsachnhanvien
#def XuaFileNhanVien(thongtinnhanvien,so_cmndcu,so_cmndmoi):
#    os.rename('dirtree/thang1/danhsachnhanvien/'+str(so_cmndcu)+'.json','dirtree/thang1/danhsachnhanvien/'+str(so_cmndmoi)+'.json')
#    TaoFileNhanVien(thongtinnhanvien,so_cmndmoi)
def XoaFileNhanVien(so_cmnd_canxoa):
    os.remove('dirtree/thang1/danhsachnhanvien/'+str(so_cmnd_canxoa)+'.json')
