import thaotacfile,os
def TaoDanhSachKhachHangThanThiet(sotienyeucau,listhoadon):
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
    return danhsach_kh_thanthiet
def XemDanhSachKhachHang(listhoadon):
    danhsachkhachhang=TaoDanhSachKhachHangThanThiet(0,listhoadon)
    return danhsachkhachhang
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
    while True:
        ngayhoadon=input('nhap ngay hoa don(phai la so) ')
        thue=input('nhap thue( phai la so) ')
        try:
            ngayhoadon=int(ngayhoadon)
            thue=float(thue)
            break
        except:
            print('\33[91mxin moi nhap lai: ')
    khachhang['thue']=thue
    khachhang['ngayhoadon']=ngayhoadon
    print('\33[92m')
if __name__=='__main__':
    listhoadon = thaotacfile.XuLyFileHoaDon.LoadDsHoaDon()
    print(XemDanhSachKhachHang(listhoadon))