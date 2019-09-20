import json,os,csv
class XuLyFile():
    def __init__(self, data, filename, month, dirname, format):
        self.month = month
        self.dirname = dirname
        self.filename = filename
        self.format = format
        self.data = data
        self.link = 'dirtree/' + str(self.month) + '/' + str(self.dirname) + '/' + str(self.filename) + '.' + str(
            self.format)
    def MakeFileJson(self):
        print(self.link)
        try:
            if self.format=='json':
                with open(self.link, 'w') as wfile:
                    json.dump(self.data, wfile)
        except:
            print('khong the tao file ',self.filename)
    def AppendFileCsv(self):
        # try:
        with open(self.link, 'a') as wfile:
            str_to_save = '#'.join(list(self.data.values())) + '\n'
            wfile.write(str_to_save)
        wfile.close()
        # except:
        #     print('khong the append file ',self.filename)
    def RemoveFile(self):
        try:
            os.remove(self.link)
            print('\33[32mthanh cong')
        except:
            print('loi khi xoa file')
    def TidyFile(self):   #lam cho file gon hon
        with open(self.link, "r") as f:
            lines = f.readlines()
            f.close()
        with open(self.link, "w") as f:
            for line in lines:
                if (line.strip("\n") != "\n"):
                    f.write(line)
class XuLyFileHoaDon(XuLyFile):
    def __init__(self,data=None,filename=None,month='thang1',dirname='danhsachhoadon',format='json'):
        filename = filename if data is None else data['sohoadon']
        super().__init__(data,filename,month,dirname,format)
    
    @staticmethod
    def LoadDsHoaDon():
        listhoadon=[]
        danhsachtenhoadon=os.listdir('dirtree/thang1/danhsachhoadon')
        for tenhoadon in danhsachtenhoadon:
            with open('dirtree/thang1/danhsachhoadon/'+str(tenhoadon),'r') as rfile:
                f=json.load(rfile)
                listhoadon.append(f)
        return listhoadon
class XuLyFileLoaiHangHoa(XuLyFile):
    def __init__(self,data=None,filename='danhsachloaihanghoa',month='thang1', dirname='danhsachloaihanghoa',format='csv'):
        super().__init__(data,filename,month,dirname,format)
    @staticmethod
    def LoadDsLoaiHangHoa():
        danhsachloaihanghoa = []
        csv.register_dialect('xulyfileloaihanghoa', delimiter='#', skipinitialspace=False)
        try:
            with open('dirtree/thang1/danhsachloaihanghoa/danhsachloaihanghoa.csv', 'r') as rfile:
                rowlist = csv.DictReader(rfile, dialect='xulyfileloaihanghoa')
                for row in rowlist:
                    danhsachloaihanghoa.append(dict(row))
            return danhsachloaihanghoa
        except:
            print('load danh sach loai hang hoa khong thang cong')
class XuLyFileHangHoa(XuLyFileLoaiHangHoa):
    def __init__(self,data=None,filename='danhsachhanghoa',month='thang1', dirname='danhsachhanghoa',format='csv'):
        super().__init__(data,filename,month,dirname,format)
    def ResertFileSauKhiSuaHoacXoa(self):
        try:
            with open(self.link, 'w') as wfile:
                wfile.write('ID#NAME#PRICE#id_loaihanghoa\n')
            wfile.close()
            with open(self.link, 'a') as wfile:
                for loaihanghoa in self.data:
                    str_to_save = '#'.join(list(loaihanghoa.values()))+'\n'
                    wfile.write(str_to_save)
            wfile.close()
        except:
            print('khong the resert file ', self.filename)
    @staticmethod
    def LoadDsHangHoa():
        danhsachhanghoa = []
        csv.register_dialect('xulyfilehanghoa', delimiter='#', skipinitialspace=True)
        # try:
        with open('dirtree/thang1/danhsachhanghoa/danhsachhanghoa.csv', 'r') as rfile:
            rowlist = csv.reader(rfile, dialect='xulyfilehanghoa')
            for row in rowlist:
                hanghoa={}
                hanghoa['ID']=row[0]
                hanghoa['NAME']=row[1]
                hanghoa['PRICE']=row[2]
                hanghoa['PRICE'] = float(hanghoa['PRICE'])
                hanghoa['soluong']=row[3]
                hanghoa['soluong']=int(hanghoa['soluong'])
                hanghoa['loaihanghoa']=row[4]
                danhsachhanghoa.append(hanghoa)
        return danhsachhanghoa
        # except:
        #     print('load danh sach loai hang hoa khong thang cong')
class XuLyFileKhoHang(XuLyFile):
    def __init__(self, data=None, filename='khohang', month='thang1', dirname='khohang', format='csv'):
        super().__init__(data,filename,month,dirname,format)
    def ResertFileSauKhiSuaHoacXoa(self):
        try:
            with open(self.link, 'w') as wfile:
                for hanghoatrongkho in self.data:
                    hanghoatrongkho['soluong'] = str(hanghoatrongkho['soluong'])
                    str_to_save = '#'.join(list(hanghoatrongkho.values())) + '\n'
                    wfile.write(str_to_save)
            wfile.close()
        except:
            print('khong the resert file ', self.filename)
    def LoadDsHangTonKho():
        danhsachhangtonkho=[]
        rfile=open('dirtree/thang1/khohang/khohang.csv','r')
        line=rfile.readline()
        while line:
            list_to_load=line.split('#')
            if len(list_to_load)>1:
                hangtonkho={}
                hangtonkho['ID']=list_to_load[0]
                hangtonkho['soluong']=int(list_to_load[1])
                if str(hangtonkho['soluong']).endswith('\n'):
                    hangtonkho['soluong']=hangtonkho['soluong'][0:len(hangtonkho['soluong'])-1]
                danhsachhangtonkho.append(hangtonkho)
            line=rfile.readline()
        return danhsachhangtonkho

class XuLyFileUser(XuLyFile):
    def __init__(self, data=None, filename='danhsachuser', month='thang1', dirname='danhsachuser', format='csv'):
        super().__init__(data,filename,month,dirname,format)
    def LoadDsUser():
        danhsachuser=[]
        rfile = open('dirtree/thang1/danhsachuser/danhsachuser.csv', 'r')
        line = rfile.readline()
        while line:
            str_to_load = line.split('#')
            user = {}
            user['acc'] = str_to_load[0]
            user['id'] = str_to_load[1]
            user['pass']=str_to_load[2]
            if user['pass'].endswith('\n'):
                user['pass'] = user['pass'][0:len(user['pass']) - 1]
            danhsachuser.append(user)
            line = rfile.readline()
        return danhsachuser
    def ResertFileUser(self):
        try:
            with open(self.link, 'w') as wfile:
                for user in self.data:
                    str_to_save = '#'.join(list(user.values()))+'\n'
                    wfile.write(str_to_save)
            wfile.close()
        except:
            print('khong the resert file ', self.filename)
def LoadFileHangBanDuoc():
    loadfile_hangbanduoc=[]
    rfile=open('dirtree/thang1/khohang/hangbanduoc.csv','r')
    line = rfile.readline()
    while line:
        str_to_load = line.split('#')
        hangbanduoc={}
        hangbanduoc['ID']=str_to_load[0]
        hangbanduoc['soluong']=str_to_load[1]
        if hangbanduoc['soluong'].endswith('\n'):
            hangbanduoc['soluong']= int(hangbanduoc['soluong'][0:len(hangbanduoc['soluong']) - 1])
        loadfile_hangbanduoc.append(hangbanduoc)
        line=rfile.readline()
    solanxuly=len(loadfile_hangbanduoc)
    for i in range(solanxuly):
        for j in range(i+1,solanxuly):
            if (loadfile_hangbanduoc[i]['ID']==loadfile_hangbanduoc[j]['ID'])and(loadfile_hangbanduoc[i]['ID']!=None):
                loadfile_hangbanduoc[i]['soluong']+=loadfile_hangbanduoc[j]['soluong']
                loadfile_hangbanduoc[j]['ID']=None
    danhsachhangbanduoc=[]
    for hang in loadfile_hangbanduoc:
        if hang['ID']!=None:
            danhsachhangbanduoc.append(hang)
    return danhsachhangbanduoc
if __name__ == '__main__':
    a={"sohoadon": "1", "tenkhachhang": "huy duong", "ngayhoadon": 7, "thue": 12, "hangdamua": [{"tenhang": "thit bo", "dongia": 200000, "soluong": 10, "thanhtien": 2000000, "loaihanghoa": "thit"}], "tongtientruocthue": 2000000, "tongtiensauthue": 2240000.0}
    b=XuLyFileHoaDon(a)
    b.MakeFileJson()