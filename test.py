import os
listmonth=os.listdir('dirtree')
def Load(thang)
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
def 