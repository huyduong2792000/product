import thaotacfile,os
def TaoDanhSachKhachHangThanThiet(sotienyeucau,listhoadon):
    listhoadon=thaotacfile.LoadDsHoaDon()
    danhsach_kh_thanthiet=[]
    for khachhang in listhoadon:
        if khachhang['tongtiensauthue'] >= sotienyeucau:
            danhsach_kh_thanthiet.append({
                'tenkhachhang':khachhang['tenkhachhang'],
                'sotiendatra':str(khachhang['tongtiensauthue'])
                })
    #in ra
    print('+'+'+'.rjust(31,'-')+'+'.rjust(17,'-'))
    print('|'+'DANH SACH '.rjust(15,' ')+'KHACH HANG'.ljust(15,' ')+'|'+'SO TIEN DA TRA'.rjust(15,' ')+' |')
    print('+'+'+'.rjust(31,'-')+'+'.rjust(17,'-'))
    for idx in danhsach_kh_thanthiet:
        print('|'+idx['tenkhachhang'].ljust(30,' ')+'|'+idx['sotiendatra'].rjust(15,' ')+' |')
        print('+'+'+'.rjust(31,'-')+'+'.rjust(17,'-'))

def XemDanhSachKhachHang(listhoadon):
    TaoDanhSachKhachHangThanThiet(0,listhoadon)

def KiemTraSoHoaDon(sohoadon):
    kiemtra=os.listdir('dirtree/thang1/danhsachhoadon')
    if (sohoadon+'.json') in kiemtra:
        return False
    return True
def NhapKhachhang(khachhang):
    while True:
        sohoadon=input('nhap so hoa don: ')
        if KiemTraSoHoaDon(sohoadon) ==True:break
        else:print('so hoa don nay da ton tai ')
    khachhang['sohoadon']=sohoadon
    khachhang['tenkhachhang']=input('nhap ten khach hang ')
    khachhang['ngayhoadon']=int(input('nhap ngay hoa don( nhap so) '))
    while True:
        thue=input('nhap thue')
        try:
            thue=int(thue)
            break
        except:
            print('\33[91mxin moi nhap lai thue: ')
    khachhang['thue']=thue
    print('\33[92m')
