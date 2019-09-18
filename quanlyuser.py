import os,thaotacfile
danhsachuser=[]
def KiemTraAccount(taikhoancantim,danhsachuser):
    for user in danhsachuser:
        if user['acc']==taikhoancantim:
            return user
    return False
def KiemTraIdUser(idcantim,danhsachuser):
    for iduser in danhsachuser:
        if iduser['id']==idcantim:
            return iduser
    return False
def ResertFileUser(data):
    opject = thaotacfile.XuLyFileUser(data)
    opject.ResertFileUser()
def LoadUser(danhsachuser):
    opject=thaotacfile.XuLyFileUser()
    opject.TidyFile()
    danhsachuser=thaotacfile.XuLyFileUser.LoadDsUser()
    return danhsachuser
def ReadUser(danhsachuser):
    LoadUser()
    while True:
        account = input('nhap tai khoan can tim ')
        user = KiemTraAccount(account,danhsachuser)
        if user==False:
            print('khong tim thay tai khoan nay')
        else:
            print(user['pass'])
            break
def CreateUser(danhsachuser,iduser=None):
    def ThongBao(iduser=None):
        if iduser==None:
                print('tao tai khoan thanh cong ')
        elif iduser!=None:
                print('da sua tai khoan ')
    dk_thongbao=iduser
    while True:
        if iduser==None:
            iduser=input('nhap id user: ')
            check_id=KiemTraIdUser(iduser,danhsachuser)
            if check_id!=False:
                print('id nay da duoc su dung xin moi nhap id khac ')
                continue

        account = input('nhap tai khoan moi: ')
        if KiemTraAccount(account,danhsachuser) != False:
            print('ten tai khoan nay da ton tai xin moi nhap tai khoan khac')
        else:
            usercreate={}
            usercreate['acc']=account
            usercreate['id']=iduser
            matkhau=input('nhap mat khau: ')
            matkhaunhaplai=input('xac nhan mat khau: ')
            if matkhau==matkhaunhaplai:
                usercreate['pass']=matkhau
                danhsachuser.append(usercreate)
                opject = thaotacfile.XuLyFileUser(usercreate)
                opject.AppendFileCsv()
                ThongBao(dk_thongbao)
                return usercreate
            else:
                print('xac nhan mat khau sai ')
                continue
def EditUser(danhsachuser):
    danhsachuser=LoadUser(danhsachuser)
    acc_edit=input('nhap account can eidt: ')
    check_acc=KiemTraAccount(acc_edit,danhsachuser)
    if check_acc==False:
        print('khong tim thay ten tai khoan nay ')
    else:
        danhsachuser.remove(check_acc)
        CreateUser(danhsachuser,check_acc['id'])
        ResertFileUser(danhsachuser)
def DeleteUser(danhsachuser):
    danhsachuser = LoadUser(danhsachuser)
    id_delete=input('nhap id user ban muon xoa: ')
    user_delete=KiemTraIdUser(id_delete,danhsachuser)
    if user_delete==False:
        print('khong tim thay id user nay')
    else:
        danhsachuser.remove(user_delete)
        ResertFileUser(danhsachuser)
        print('xoa user thanh cong ')
def LogIn(danhsachuser):
    danhsachuser = LoadUser(danhsachuser)
    acc_log=input('nhap ten tai khoan ')
    check_acc=KiemTraAccount(acc_log,danhsachuser)
    while True:
        if acc_log==False:
            print('khong tim thay tai khoan nay')
        elif:
            password=input('nhap password: ')
            if password==check_acc['pass']:
                return True
            else:
                print('sai thongtin tai khoan hoac mat khau ')
def LogUot():
    chon=input('ban co that su muon dang xuat khong( an c de dang xuat): ')
    if chon=='c':
        return True
    else:
        return False
if __name__=='__main__':
    print(LoadUser(danhsachuser))
    DeleteUser(danhsachuser)
