import thaotacfile,os

def CheckIdTrongKho(id,danhsachhangtrongkho):
    for hanghoa in danhsachhangtrongkho:
        if hanghoa['ID']==str(id):
            return True
    return False
def PhieuNhapKho(danhsachhangthemvaokho):
    print('+-------+------+----------------------+')
    print('|  STT  |  ID  |       SO LUONG       |')
    print('+-------+------+----------------------+')
    stt=0
    for hanghoa in danhsachhangthemvaokho:
        stt+=1
        print('|'+str(stt).rjust(len('-------'),' '),end='|')
        print(str(hanghoa['ID']).rjust(len('------'),' '),end='|')
        print(str(hanghoa['soluong']).rjust(len('----------------------'),' '),end='|')
        print('\n+-------+------+----------------------+')
def NhapIDvaSoLuong(danhsachhangtrongkho):
    id = input('nhap ID hang hoa can them ')
    if CheckIdTrongKho(id, danhsachhangtrongkho) == False:
        print('khong tim thay ID nay trong kho ')
    elif CheckIdTrongKho(id, danhsachhangtrongkho) == True:
        while True:
            soluong = input('nhap so luong hang hoa nhap kho ')
            try:
                soluong=int(soluong)
                hangthemvao=ThemVao(id,soluong,danhsachhangtrongkho)
                print(hangthemvao)
                return hangthemvao
            except:
                print('nhap lai so luong: ')
def ThemVao(id,soluong,danhsachhangtrongkho):
    hangthemvao = {}
    for idx in range(len(danhsachhangtrongkho)):
        if danhsachhangtrongkho[idx]['ID'] == id:
            danhsachhangtrongkho[idx]['soluong'] += soluong
    hangthemvao['ID'] = id
    hangthemvao['soluong'] = soluong
    return hangthemvao
def NhapKho(danhsachhangtrongkho,idhangthemvao=None,soluong=None):
    danhsachhangthemvaokho = []
    while True:
        if idhangthemvao==None:
            hangthemvao=NhapIDvaSoLuong(danhsachhangtrongkho)
            danhsachhangthemvaokho.append(hangthemvao)
        else:
            hangthemvao=ThemVao(idhangthemvao,soluong,danhsachhangtrongkho)
            danhsachhangthemvaokho.append(hangthemvao)
            danhsachhangtrongkho.append(hangthemvao)
        choose=input('ban co muon them hang hoa vao kho nua khong( bam k de thoat) ')
        if choose.lower()=='k':break
    PhieuNhapKho(danhsachhangthemvaokho)
    opject=thaotacfile.XuLyFileKhoHang(danhsachhangtrongkho)
    opject.ResertFileSauKhiSuaHoacXoa()
def HoaDonXuatKho(id,soluonglayra,danhsachhangtrongkho):
    danhsachhangtrongkho = thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
    for idx in range(len(danhsachhangtrongkho)):
        if danhsachhangtrongkho[idx]['ID'] == id:
            danhsachhangtrongkho[idx]['soluong']=int(danhsachhangtrongkho[idx]['soluong'])
            if danhsachhangtrongkho[idx]['soluong'] >= soluonglayra:
                danhsachhangtrongkho[idx]['soluong'] -= soluonglayra
                hanglayra={}
                hanglayra['ID']=id
                hanglayra['soluong']=str(soluonglayra)
                opject = thaotacfile.XuLyFileKhoHang(danhsachhangtrongkho)
                opject.ResertFileSauKhiSuaHoacXoa()
                opject1 = thaotacfile.XuLyFileKhoHang(hanglayra, filename='hangbanduoc')
                opject1.AppendFileCsv()
            else:
                print('hang hoa loai nay chi con ', danhsachhangtrongkho[idx]['soluong'])
                break
if __name__=='__main__':
    danhsachhangtrongkho = thaotacfile.XuLyFileKhoHang.LoadDsHangTonKho()
    HoaDonXuatKho('bc',10,danhsachhangtrongkho)