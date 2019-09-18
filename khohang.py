import thaotacfile,os
danhsachhangtrongkho=thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
def CheckIdTrongKho(id,danhsachhangtrongkho):
    for hanghoa in danhsachhangtrongkho:
        if hanghoa['ID']==str(id):
            return True
    return False
def PhieuNhapKho(danhsachhangthemvaokho):
    print('+-------+------+------------+')
    print('|  STT  |  ID  |  SO LUONG  |')
    print('+-------+------+------------+')
    stt=0
    for hanghoa in danhsachhangthemvaokho:
        stt+=1
        print('|'+str(stt).rjust(len('-------'),' '),end='|')
        print(str(hanghoa['ID']).rjust(len('------'),' '),end='|')
        print(str(hanghoa['soluong']).rjust(len('------------'),' '),end='|')
        print('\n+-------+------+------------+')
def NhapKho(danhsachhangtrongkho):
    danhsachhangthemvaokho = []
    while True:
        while True:
            id=input('nhap ID hang hoa can them ')
            if CheckIdTrongKho(id,danhsachhangtrongkho)==False:
                print('khong tim thay ID nay trong kho ')
            elif CheckIdTrongKho(id,danhsachhangtrongkho)==True:
                hangthemvao={}
                soluong=int(input('nhap so luong hang hoa nhap kho '))
                for idx in range(len(danhsachhangtrongkho)):
                    if danhsachhangtrongkho[idx]['ID']==id:
                        danhsachhangtrongkho[idx]['soluong']+=soluong
                        hangthemvao['ID']=id
                        hangthemvao['soluong']=soluong
                        danhsachhangthemvaokho.append(hangthemvao.copy())
                break
        choose=input('ban co muon them hang hoa vao kho nua khong( bam k de thoat) ')
        if choose.lower()=='k':break
    PhieuNhapKho(danhsachhangthemvaokho)
    opject=thaotacfile.XuLyFileKhoHang(danhsachhangtrongkho)
    opject.ResertFileSauKhiSuaHoacXoa()
def XuatKho(danhsachhangtrongkho):
    danhsachhanglayra=[]
    while True:
        while True:
            id=input('nhap ID cua hang hoa can lay ra ')
            chek_id=CheckIdTrongKho(id,danhsachhangtrongkho)
            if chek_id==False:
                print('khong tim thay ID nay trong kho ')
            else:
                soluonglayra=int(input('nhap so luong lay ra cua hang hoa nay '))
                for idx in range(len(danhsachhangtrongkho)):
                    if danhsachhangtrongkho[idx]['ID']==id:
                        if danhsachhangtrongkho[idx]['soluong']>soluonglayra:
                            danhsachhangtrongkho[idx]['soluong']-=soluonglayra
                            danhsachhanglayra.append({
                                'ID':id,
                                'soluong':soluonglayra
                            })
                        else:
                            print('hang hoa loai nay chi con',danhsachhangtrongkho[idx]['soluong'])
                break
        choose = input('ban co muon lay hang hoa ra khoi kho nua khong( bam k de thoat) ')
        if choose.lower() == 'k': break
    PhieuNhapKho(danhsachhanglayra)
    opject=thaotacfile.XuLyFileKhoHang(danhsachhangtrongkho)
    opject.ResertFileSauKhiSuaHoacXoa()
def HoaDonXuatKho(id,soluonglayra,danhsachhanghoatrongkho):
    chek_id = CheckIdTrongKho(id, danhsachhangtrongkho)
    if chek_id == False:
        print('khong tim thay ID nay trong kho ')
    else:
        for idx in range(len(danhsachhangtrongkho)):
            if danhsachhangtrongkho[idx]['ID'] == id:
                danhsachhangtrongkho[idx]['soluong']=int(danhsachhangtrongkho[idx]['soluong'])
                if danhsachhangtrongkho[idx]['soluong'] > soluonglayra:
                    danhsachhangtrongkho[idx]['soluong'] -= soluonglayra
                else:
                    print('hang hoa loai nay chi con ', danhsachhangtrongkho[idx]['soluong'])
                    break
    opject = thaotacfile.XuLyFileKhoHang(danhsachhangtrongkho)
    opject.ResertFileSauKhiSuaHoacXoa()
if __name__=='__main__':
    NhapKho(danhsachhangtrongkho)