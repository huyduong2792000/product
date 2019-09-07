import thaotacfile
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def TaoLoaiHangHoa(tenloaihanghoa,tenhanghoa,danhsachloaihanghoa):
    danhsachloaihanghoa=thaotacfile.LoadDsLoaiHangHoa()
    for idx in danhsachloaihanghoa:
        if tenloaihanghoa==idx['tenloaihanghoa']:
            if tenhanghoa in idx['danhsachhanghoatrongloai']:
                return
            else:
                idx['danhsachhanghoatrongloai'].append(tenhanghoa)
                return
    loai_hanghoa_canthem={}
    loai_hanghoa_canthem['tenloaihanghoa']=tenloaihanghoa
    loai_hanghoa_canthem['danhsachhanghoatrongloai']=[tenhanghoa]
    danhsachloaihanghoa.append(loai_hanghoa_canthem)
    thaotacfile.GhiFileLoaiHangHoa(danhsachloaihanghoa)
def XemLoaiHangHoa(danhsachloaihanghoa):
    danhsachloaihanghoa=thaotacfile.LoadDsLoaiHangHoa()
    for idx in danhsachloaihanghoa:
        print (bcolors.WARNING+idx['tenloaihanghoa'].upper())
        for hanghoa in idx['danhsachhanghoatrongloai']:
            print('\33[35m'+hanghoa)
def ThemLoaiHangHoaTrucTiep():
    tenloaihanghoa=input('nhap ten loai hang hoa can them ')
    while True:
        ten_hanghoa_trongloai=input('nhap ten loai hang hoa trong loai: ')
        TaoLoaiHangHoa(tenloaihanghoa,ten_hanghoa_trongloai,danhsachloaihanghoa)
        chon=input('ban muon nhap hang hoa trong loai nua khong( bam k de thoat): ')
        if chon=='k':return
