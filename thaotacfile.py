import json,os,csv
class XuLyFile():
    link=None
    filename=None
    format={}
    month=0
    dirname=None
    data=None
    def __init__(self):
        pass
    def MakeFileJson(self):
        try:
            if self.format=='json':
                with open(self.link, 'w') as wfile:
                    json.dump(self.data, wfile)
        except:
            print('khong the tao file ',self.filename)
    def AppendFileCsv(self):
        try:
            with open(self.link, 'a') as wfile:
                str_to_save = '#'.join(list(self.data.values())) + '\n'
                wfile.write(str_to_save)
            wfile.close()
        except:
            print('khong the append file ',self.filename)
    def RemoveFile(self):
        try:
            os.remove(self.link)
            print('\33[32mthanh cong')
        except:
            print('loi khi xoa file')
    def ResertFile(self):
        try:
            if self.format == 'json':
                with open(self.link, 'w') as wfile:
                    json.dump(self.data, wfile)
            else:
                with open(self.link, 'w') as wfile:
                    str_to_save = '#'.join(list(self.data.values()))
                wfile.write(str_to_save)
            wfile.close()
        except:
            print('khong the resert file ', self.filename)
    def TidyFile(self):   #lam cho file gon hon
        with open(self.link, "r") as f:
            lines = f.readlines()
        with open(self.link, "w") as f:
            for line in lines:
                if line.strip("\n") != "\n":
                    f.write(line)
class XuLyFileHoaDon(XuLyFile):
    def __init__(self,month=None,dirname=None,filename=None,format=None,data=None):
        self.month = month
        self.dirname = dirname
        self.filename = filename
        self.format = format
        self.data=data
        self.link = 'dirtree/' + str(self.month) + '/' + str(self.dirname) + '/' + str(self.filename) + '.' + str(
            self.format)
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
        self.month = month
        self.dirname = dirname
        self.filename = filename
        self.format = format
        self.data = data
        self.link = 'dirtree/' + str(self.month) + '/' + str(self.dirname) + '/' + str(self.filename) + '.' + str(
            self.format)
    def ResertFile(self):
        try:
            with open(self.link, 'w') as wfile:
                wfile.write('ID#NAME\n')
            wfile.close()
            with open(self.link, 'a') as wfile:
                for loaihanghoa in self.data:
                    str_to_save = '#'.join(list(loaihanghoa.values()))+'\n'
                    wfile.write(str_to_save)
            wfile.close()
        except:
            print('khong the resert file ', self.filename)
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
        self.month = month
        self.dirname = dirname
        self.filename = filename
        self.format = format
        self.data = data
        self.link = 'dirtree/' + str(self.month) + '/' + str(self.dirname) + '/' + str(self.filename) + '.' + str(
            self.format)
    def LoadDsHangHoa(self):
        danhsachhanghoa = []
        csv.register_dialect('xulyfilehanghoa', delimiter='#', skipinitialspace=True)
        try:
            with open(self.link, 'r') as rfile:
                rowlist = csv.DictReader(rfile, dialect='xulyfilehanghoa')
                for row in rowlist:
                    danhsachhanghoa.append(dict(row))
            return danhsachhanghoa
        except:
            print('load danh sach loai hang hoa khong thang cong')
class XuLyFileNhanVien(XuLyFile):
    def __init__(self, data=None, filename=None,month='thang1', dirname='danhsachnhanvien',format='json'):
        self.month = month
        self.dirname = dirname
        self.filename = filename if data is None else data['socmnd']
        self.format = format
        self.data = data
        self.link = 'dirtree/' + str(self.month) + '/' + str(self.dirname) + '/' + str(self.filename) + '.' + str(
            self.format)
    def LoadDsNhanVien():
        danhsachnhanvien = []
        try:
            danhsach_cmndnhanvien = os.listdir('dirtree/thang1/danhsachnhanvien')
        except:
            print('khong tim thay file danhsachnhanvien')
            return
        for socmnd in danhsach_cmndnhanvien:
            with open('dirtree/thang1/danhsachnhanvien/' + str(socmnd), 'r') as rfile:
                f = json.load(rfile)
                danhsachnhanvien.append(f)
        return danhsachnhanvien
if __name__ == '__main__':
    b=XuLyFileHangHoa()
    print(b.LoadDsHangHoa())