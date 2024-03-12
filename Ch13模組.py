#意義和java中 import "package"同

import makefood#同from makefood import *(全部)
makefood.make_icecream('玉米片','焦糖','oreo')
makefood.make_drink('large','coke')

#只要引特定函數 例:from makefood import make_icecream,make_drink

#as指定替代名稱
import makefood as mf
mf.make_icecream('草莓醬')
mf.make_drink('small','fanta')
print()
from makefood import make_drink as m_d
m_d('medium','mountain dew')
print()

#若兩模組有父子類別，有子類別的模組記得導入繼承父類別
from TPBank import TPbank
from SSBankfromTPBank import SSbank
hisbank=TPbank('he')
print("his bank= ",hisbank.bank_title())
hisbank.save_money(500)
hisbank.get_balance()
herbank=SSbank('she')
print("her bank= ",herbank.bank_title())

#random模組
import random
#randint(min,max)在指定區間產生隨機數值
n=3
for i in range(n):
    print("1-100隨機產生一個數字: ",random.randint(1,100))

min,max=1,10
ans=random.randint(min,max)
while True:
    yourNum=int(input("請猜1-10之間數字: "))
    if yourNum==ans:
        print("答對了!")
        break
    elif yourNum<ans:
        print("太小!")
    elif yourNum>ans:
        print("太大!")

#choice(list)從指定list隨機回傳一個元素
fruits=['apple','orange','banana','strawberry','peach']
print("從fruits中隨機挑一個: ",random.choice(fruits))
#shuffle(list)將指定list內元素打亂
print("fruits原本排列: ",fruits)
random.shuffle(fruits)
print("fruits用shuffle()打亂後: ",fruits)

#time模組
import time

#time()印出1970/1/1至今的秒數
print("從1970/1/1 00:00:00至今的秒數: ",int(time.time()))

#asctime()得到現在電腦時間
print(time.asctime())

#localtime()得到有結構的現在電腦時間
xtime=time.localtime()
print(xtime)
print(xtime[0]," 年")
print(xtime[1]," 月")
print(xtime[2]," 日")
print(xtime[3]," 時")
print(xtime[4]," 分")
print(xtime[5]," 秒")
print("星期 ",xtime[6])
print("今年的第 ",xtime[7]," 天")
print("是否為夏令時間?(0不是1是) ",xtime[8])

#sleep(int)可暫停程式執行int秒，可用在迴圈

#重作可計時的猜數字系統
min1,max1=1,20
ans1=random.randint(min1,max1)
starttime=int(time.time())
while True:
    yourNum1=int(input("請猜1-20之間數字: "))
    if yourNum1==ans1:
        print("答對了!")
        endtime=int(time.time())
        print("所花時間: ",endtime-starttime," 秒")
        break
    elif yourNum1<ans1:
        print("太小!")
    elif yourNum1>ans1:
        print("太大!")

#sys模組
import sys
print("目前python版本是: ",sys.version)#得到目前電腦上python版本
print("請隨意輸入超過8個字元的字串: ",end="")
msg=sys.stdin.readline(8)#stdin=standard input,可想成從python shell視窗輸入,搭配readline(int)決定讀取多少的螢幕輸入值
print("只取前8個字元: ",msg)
sys.stdout.write("Hello Python\n")#stdout=standard output，可想成在python shell視窗輸出,搭配write()輸出資料

#keyword模組
import keyword
print(keyword.kwlist)#列出python所有關鍵字
keywordlist=['as','while','break','java']
for x in keywordlist:
    print(x,keyword.iskeyword(x))#判斷是否為關鍵字回傳True,False
