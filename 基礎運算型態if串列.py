'''
註解方法一
'''
"""
註解方法二
"""

#各種斷句
str1 = 'I can\'t stop.'
print(str1)
str2 = "I \tcan't sto\np"
print(str2)

#一敘述分多行 都是42
a = b = c = 10
x = a + b + c + 12
print(x)
y = a +\
    b +\
    c +\
    12
print(y)
z = ( a +
      b +
      c +
      12 )
print(z)

#餘數、整除
remainder=9 % 5
print(remainder)
quotient=100//3
print(quotient)
print(type(quotient))

#次方
print(pow(2,4))

#二進位
binary=0b1101
print(0b1101)
print(bin(13))

#加r可解除escape效果、字串間強制插東西
string="Hello!\nPython"
print(string)
string2=r"Hello!\nPython"
print(string2,end="\t")#換行改tab鍵分開
print("Hello!","Python",sep="$$$")

#格式化字串
print("%s的第%d次期中成績是%.2f"%("你",1,99.9))
print("{}的第{}次期中成績是{}".format("你",1,99.9))

#輸入
name=input("請輸入姓名:")
print(name)

#邏輯運算子
q=(10>8)and(6>10)
print(q)

#ifelse、elif
num1=input("請輸入num1:")
num2=input("請輸入num2:")
if(num1<num2):
    print("小")
elif(num1>num2):
    print("大")
else:
    print("同")

#串列特殊叫法、取特定區間元素、取個數、最大小總和、串列乘以幾倍、直接刪元素
score=[]
score=[60,70,80,90,100]
score1,score2,score3,score4,score5=score
print(score1,score2,score3,score4,score5)
print(score[0:3])#0到3-1
print(score[2:])#2到最後
print(score[-3:])#最後3個
print(score[-1])#最後一個(-2倒數第二筆，以此類推)
print(len(score))
print(max(score))
print(min(score[1:4]))
print(sum(score))
score3=score*3#變三倍串列
print(score3)
del score3[4]
print(score3)
del score3[0:2]#消除0到(2-1=1)的元素
print(score3)
del score3[0:len(score3):2]#從最前開始消除每次隔一個，消一保二消三.....
print(score3)
del score3#直接刪掉整個串列

#字串更改大小空格
string=" DeepStone "
print(string.upper())
print(string.lower())
print(string.title())
print(string.lstrip())#去掉左邊空格
print("/%s/"%string.rstrip())
print(string.strip())#去掉兩邊空格

#串列各式method
score.append(110)#從最後一個加
print(score)
score.insert(0,50)#決定位置再加
print(score)
score.pop()#從最後一個刪
print(score)
score.pop(0)#刪指定位置
print(score)
score.remove(100)#刪指定元素
print(score)
score.reverse()
print(score)#顛倒
cars=['volkswagen','ford','honda','toyota','bmw']
print(cars)
cars_sorted=sorted(cars)#sort直接改串列，sorted是新增一個改的串列同時保留原串列
print(cars_sorted)
cars_sorted_r=sorted(cars,reverse=True)
print(cars_sorted_r)
cars.sort()#小排到大，英文照字母順序數量所以benz在bmw前面(be<bw)
print(cars)
cars.sort(reverse=True)#大排到小
print(cars)

#串列進階
num=[10,20,20,20,30,40,50,10]
print(num.index(10))#只找第一個先出現的
print(num.count(20))
char='&'#&若改為\n則有換行效果
print(char.join(cars))#連接整個串列為一個字串，元素必須都是str

#串列內有串列
number=[1,2,3,[4,5]]
print(number[3])
print(number[3][0])
number2=[6,7,8]
number.append(number2)#num2加到num1最後
print(number)
number.extend(number2)#將num2中一個一個元素依序插在最後(分解num2串列)
print(number)

#deep copy & shallow copy
mymusic=['indie','metal']
cemusic=mymusic#deep copy兩串列互相影響，必定一樣
mymusic.append('acoustic')
cemusic.append('hippop')
print(mymusic)
print(cemusic)
toomusic=mymusic[:]#shallow copy兩串列不互相影響
mymusic.append('piano')
toomusic.append('gfunk')
print(mymusic)
print(toomusic)

#字串和串列關係
#python中視字串為char組成的串列
str="python"
print(str[0])
print(str[-1])#負值索引，-1即最後一個
print(str[0:3])#第0個到第3-1=2個
print(str[0:5:2])#pto，第0個開始每次跳一個
print(str[-2:])#on，最後兩個
cutstr=list('Deep Stone!')#字串切片，拆成字
print(cutstr)
cutstr[5:]='Mind'#切片同時改字串內容變Deep Mind
print(cutstr)
myuni="National NCCU University"
myunisplit=myuni.split()#拆成詞
print(myunisplit)

#enumerate、in &not in
fruits=['apple','banana','lemon','watermelon']
enumerate_fruits=enumerate(fruits)
print(type(enumerate_fruits))
print(enumerate_fruits)#傳回所在記憶體
print(list(enumerate_fruits))#傳回(0,'apple'),(1,'banana')......
ch=input("新增:")
if ch in fruits:
    print("已有")
else:
    fruits.append(ch)
    print("已新增",fruits)
