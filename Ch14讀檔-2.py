#read()可讀取檔案並以字串傳回

fn1='大一上必修.txt'#因為記事本和現在的.py檔在同一資料夾，所以可不用絕對路徑
file_Obj=open(fn1)
data=file_Obj.read()
file_Obj.close()#每次開啟檔案完一定要記得close()保護檔案
print(data)
print()

with open(fn1) as file_Obj:
    data=file_Obj.read()
    new_data=data.replace('(i)','(一)')
    print(new_data)
print()

fn2='大一下必修.txt'
with open(fn2) as file_Obj:#用with就不需要close()
    #可用 for line in file_Obj: print(line)，但readlines()可直接做到
    obj_list=file_Obj.readlines()#readlines()每次讀一行再轉串列元素，最終印出串列
print(obj_list)#txt檔換行字元\n會被印出
print()
for line in obj_list:
    print(line.rstrip())#rstrip()解決\n的問題
print()

#數據組合，將前述obj_list以&連接
str_Obj='&'
str=''
length=len(obj_list)-1#len=4,但迴圈i從0開始，只需0,1,2 最後一個不要& 所以length=3
i=0
for line in obj_list:
    if i<length:
        str=line.rstrip()+str_Obj
        i+=1
        print(str,end='')
    else:
        str=line.rstrip()
        print(str,end='')
print()

#在特定txt檔找關鍵字
with open(fn1) as file_Obj:
    obj_list=file_Obj.readlines()
str_Obj=''
for line in obj_list:
    str_Obj+=line.rstrip()
findstr=input("請輸入輸入欲搜尋字串: ")
if findstr in str_Obj:
    print("%s字串存在於%s檔案中"%(findstr,fn1))
else:
    print("%s字串不存在於%s檔案中"%(findstr,fn1))
    
#用find()尋找檔案內關鍵字
with open(fn2) as file_Obj:
    obj_list2=file_Obj.readlines()
str_Obj2=''
for line in obj_list2:
    str_Obj2+=line.rstrip()
findstr2=input("請輸入輸入欲搜尋字串: ")
index=str_Obj2.find(findstr2)
if index>=0:
    print("%s字串存在於%s檔案中"%(findstr2,fn2))
    print("在index=%s處出現"%index)
else:
    print("%s字串不存在於%s檔案中"%(findstr2,fn2))

#write()寫檔
fn3='forWriteIn.txt'#執行時就會自動在資料夾內建txt檔
string='Learning Python right now'
with open(fn3,'a') as file_Obj:#原本讀檔預設為'r','w': 若已經with open()...過檔案存在的話，下一次with open()會洗掉之前write()的,'a'則不會洗掉
    file_Obj.write(string)
'''
#write()只可寫入字串，寫入數值要用str()轉字串
x=100

#str_x=str(x)會出錯 無解
'''
with open(fn3,'a') as file_Obj:
    file_Obj.write('100')

#write()寫入多個字串會寫在同一行 換行還是要\n
string2='Learning Japanese right now'
string3='Learning Guitar right now'
with open(fn3,'a') as file_Obj:
    file_Obj.write(string2+'\n')
    file_Obj.write(string3+'\n')

#shutil模組
import shutil
shutil.copy('大一上必修.txt','大一上必修copy.txt')#複製大一上必修.txt內容，自動在目前資料夾建立大一上必修copy.txt
#shutil.copy()
#shutil.copy()

#copytree(),rmtree()

#move()

#send2trash()

#壓縮 解壓縮

#編碼格式
