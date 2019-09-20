import os
def Load(thang):
    loadfile_hangbanduoc=[]
    rfile=open('dirtree/'+thang+'/khohang/hangbanduoc.csv','r')
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
def TinhTongSLHangTheoThang(danhsachhangbanduoc):
    sum=0
    for hangbanduoc in danhsachhangbanduoc:
        sum+=hangbanduoc['soluong']
    return sum
def XuLyTongSoLuong():
    thongkesoluong=[]
    listmonth = os.listdir('dirtree')
    for thang in listmonth:
        danhsachhangbanduoc= Load(thang)
        soluongtheothang={}
        soluongtheothang['thang']=thang
        soluongtheothang['soluong']=TinhTongSLHangTheoThang(danhsachhangbanduoc)
        thongkesoluong.append(soluongtheothang)
    return thongkesoluong
def TimThangMax():
    thongkesoluong=XuLyTongSoLuong()
    slmax=['',0]
    for thongke in thongkesoluong:
        if thongke['soluong']>slmax[1]:
            slmax[1]=thongke['soluong']
            slmax[0]=thongke['thang']
    return slmax
def lineprint(slmax,soluongtrongthang):
    if soluongtrongthang<slmax:
        return '      '
    else:
        return '\33[31m------'

def sapxepthang(val):
    return val['thang']
def display():
    slmax = TimThangMax()
    thongkesoluong = XuLyTongSoLuong()
    thongkesoluong.sort(key=sapxepthang)
    print(thongkesoluong)
    for sl in range(slmax[1],0,-1000):
        print('\n')
        print('\33[34m'+str(sl).rjust(5,' '),end='')
        for i in range(7):
            print('       '+lineprint(sl,thongkesoluong[i]['soluong']),end='')
    print('\n  0________________________________________________________________________________________________>')
    print('\n\33[33m           THANG1       THANG2       THANG3       THANG4       THANG5       THANG6       THANG7')