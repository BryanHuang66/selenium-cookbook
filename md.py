from scripts.kechuangban import kechuangban
from scripts.chuangyeban import chuangyeban
from scripts.xingufaxing import xinggufaxing
import datetime
from settings import location
date = datetime.date.today()

if __name__ == "__main__":
    print("---  正在获取创业板ipo数据  ---")
    chuangyebanipo = chuangyeban("ipo")
    print("---  正在获取创业板ref数据  ---")
    chuangyebanref = chuangyeban("refinance")
    print("---  正在获取创业板rep数据  ---")
    chuangyebanrep = chuangyeban("reproperty")
    print("---  正在获取科创板数据  ---")
    kechuangbanipo,kechuangbanref,kechuangbanrep = kechuangban()
    print("---  正在获取新发行股票  ---")
    huzhubanxfx,shenzhubanxfx,kechuangbanxfx,chuangyebanxfx = xinggufaxing()
    allxfx = huzhubanxfx+shenzhubanxfx
    listxfx = allxfx[0]
    listxfx_name = []
    print("---  正在输出公司信息  ---")
    for i in range(1,int(len(allxfx)/4)):
        listxfx = listxfx+","+allxfx[i*4]
    for i in range(0, int(len(allxfx) / 4)):
        listxfx_name = listxfx_name+[allxfx[i*4+1]]
    print("---  开始进行文件输入  ---")


    f = open(location+str(date)+"_每周简报.md","w",encoding='UTF-8', errors='ignore')
    f.write("# IPO\n## 创业板\n1. 交易所审核通过情况\n")
    for i in range(0,int(len(chuangyebanipo)/4)):
        if chuangyebanipo[4*i+2]=="上市委会议通过":
            f.write("	+ [["+chuangyebanipo[4*i]+"]]\n")
    f.write("2. 交易所审核终止情况\n")
    for i in range(0,int(len(chuangyebanipo)/4)):
        if chuangyebanipo[4*i+2]=="终止(撤回)":
            f.write("	+ [["+chuangyebanipo[4*i]+"]]\n")
    f.write("3. 交易所注册终止情况\n")
    for i in range(0, int(len(chuangyebanipo) / 4)):
        if chuangyebanipo[4 * i + 2] == "终止注册":
            f.write("	+ [[" + chuangyebanipo[4 * i] + "]]\n")

    f.write("## 科创板\n1. 交易所审核通过情况\n")
    for i in range(0,int(len(kechuangbanipo)/4)):
        if kechuangbanipo[4*i+2]=="上市委会议通过":
            f.write("	+ [["+kechuangbanipo[4*i]+"]]\n")
    f.write("2. 交易所审核终止情况\n")
    for i in range(0,int(len(kechuangbanipo)/4)):
        if kechuangbanipo[4*i+2]=="终止":
            f.write("	+ [["+kechuangbanipo[4*i]+"]]\n")
    f.write("3. 交易所注册终止情况\n")
    for i in range(0,int(len(kechuangbanipo)/4)):
        if kechuangbanipo[4*i+2]=="终止注册":
            f.write("	+ [["+kechuangbanipo[4*i]+"]]\n")


    numhuzhuban =int( len(huzhubanxfx)/4)
    numshenzhuban = int(len(shenzhubanxfx) / 4)
    numkechuangban = int(len(kechuangbanxfx) / 4)
    numchuangyeban = int(len(chuangyebanxfx) / 4)
    f.write("## 新发行股票\n  本周新发行股票总共"+str(numhuzhuban+numshenzhuban)+"只新股,包括科创板"+str(numkechuangban)+"只、沪市主板"+str(numhuzhuban-numkechuangban)+"只、创业板"+str(numchuangyeban)+"只、深市主板"+str(numshenzhuban-numchuangyeban)+"只。\n")
    f.write("### 创业板\n")
    for i in range(0,numchuangyeban):
        f.write("+ [[" + chuangyebanxfx[i*4+1] + "]]\n")
    f.write("### 科创板\n")
    for i in range(0,numkechuangban):
        f.write("+ [[" + kechuangbanxfx[i*4+1] + "]]\n")
    f.write("### 主板\n")
    for i in range(0,numshenzhuban):
        f.write("+ [[" + shenzhubanxfx[i*4+1] + "]]\n")
    for i in range(0,numhuzhuban):
        f.write("+ [[" + huzhubanxfx[i*4+1] + "]]\n")




    f.write("---\n")

    f.write("# 再融资\n## 创业板\n1. 交易所审核通过情况\n")
    for i in range(0, int(len(chuangyebanref) / 4)):
        if chuangyebanref[4 * i + 2] == "上市委会议通过":
            f.write("	+ [[" + chuangyebanref[4 * i] + "]]\n")
    f.write("2. 交易所审核终止情况\n")
    for i in range(0, int(len(chuangyebanref) / 4)):
        if chuangyebanref[4 * i + 2] == "终止(撤回)":
            f.write("	+ [[" + chuangyebanref[4 * i] + "]]\n")
    f.write("3. 交易所注册终止情况\n")
    for i in range(0, int(len(chuangyebanref) / 4)):
        if chuangyebanref[4 * i + 2] == "终止注册":
            f.write("	+ [[" + chuangyebanref[4 * i] + "]]\n")

    f.write("## 科创板\n1. 交易所审核通过情况\n")
    for i in range(0, int(len(kechuangbanref) / 4)):
        if kechuangbanref[4 * i + 2] == "通过":
            f.write("	+ [[" + kechuangbanref[4 * i] + "]]\n")
    f.write("2. 交易所审核终止情况\n")
    for i in range(0, int(len(kechuangbanref) / 4)):
        if kechuangbanref[4 * i + 2] == "终止":
            f.write("	+ [[" + kechuangbanref[4 * i] + "]]\n")
    f.write("3. 交易所注册终止情况\n")
    for i in range(0, int(len(kechuangbanref) / 4)):
        if kechuangbanref[4 * i + 2] == "终止注册":
            f.write("	+ [[" + kechuangbanref[4 * i] + "]]\n")

    f.write("---\n")

    f.write("# 并购\n## 创业板\n1. 交易所审核通过情况\n")
    for i in range(0, int(len(chuangyebanrep) / 4)):
        if chuangyebanrep[4 * i + 2] == "上市委会议通过":
            f.write("	+ [[" + chuangyebanrep[4 * i] + "]]\n")
    f.write("2. 交易所审核终止情况\n")
    for i in range(0, int(len(chuangyebanrep) / 4)):
        if chuangyebanrep[4 * i + 2] == "终止(撤回)":
            f.write("	+ [[" + chuangyebanrep[4 * i] + "]]\n")
    f.write("3. 交易所注册终止情况\n")
    for i in range(0, int(len(chuangyebanrep) / 4)):
        if chuangyebanrep[4 * i + 2] == "终止注册":
            f.write("	+ [[" + chuangyebanrep[4 * i] + "]]\n")

    f.write("## 科创板\n1. 交易所审核通过情况\n")
    for i in range(0, int(len(kechuangbanrep) / 4)):
        if kechuangbanrep[4 * i + 2] == "上市委会议通过":
            f.write("	+ [[" + kechuangbanrep[4 * i] + "]]\n")
    f.write("2. 交易所审核终止情况\n")
    for i in range(0, int(len(kechuangbanrep) / 4)):
        if kechuangbanrep[4 * i + 2] == "终止":
            f.write("	+ [[" + kechuangbanrep[4 * i] + "]]\n")
    f.write("3. 交易所注册终止情况\n")
    for i in range(0, int(len(kechuangbanrep) / 4)):
        if kechuangbanrep[4 * i + 2] == "终止注册":
            f.write("	+ [[" + kechuangbanrep[4 * i] + "]]\n")
    f.close()
