#for迴圈
alphabet=['a','b','c','d']
for ab in alphabet:
    print(ab)
for ab in alphabet: print(ab)
print('\n')
for ab in alphabet[:3]: print(ab)#前3個
print('\n')
for ab in alphabet[-3:]: print(ab)#後3個

#range()，形成整數串列
n=7
rangen=list(range(n))
print(rangen)#長度為7，印出0,1,2,3,4,5,6
number1=list(range(2,6))#2印到5(6-1)
print(number1)
number2=list(range(-2,3))#-2印到3-1=2
print(number2)
print('\n')
for number in range(-5,1):#-5開始，1-1=0結束
    print(number)
number3=list(range(2,10,2))#2開始，10-1=9結束，每次跳+2(2,4,6,8)所以不會到9
print(number3)

#range()求總和
n=int(input("請輸入整數:"))
number=list(range(n+1))
total=sum(number)
print("1到%d總和:"%n,total)
#用for求總和
total=0
for i in number:
    total+=i
print("1到%d總和:"%n,total)

#平方串列
squares=[]
sq=int(input("請輸入整數: "))
if sq<=10:
    for num in range(1,sq+1):
        value=num*num
        squares.append(value)
print(squares)
#更簡便平方串列
squares2=[]
sq2=int(input("請輸入整數: "))
if sq2<=10:
    squares2=[num2**2 for num2 in range(1,sq2+1)]
print(squares2)

#巢狀迴圈:99乘法表
for i in range(1,10):
    for j in range(1,10):
       result=i*j
       print("%d*%d=%-3d"%(i,j,result),end="")
    print()#換行(1*1...換到2*1...)

#巢狀迴圈:直角三角形
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print("a",end="")
    print()

#break
for digit in range(1,11):
    if digit==6:
        print("斷")
        break
    print(digit,end=', ')
    
#continue
scores=[11,22,33,44,0,55,60,66,77]
for score in scores:
    if score>60:
        print("大於60")#score>60印這個(true)
        continue
    print(score)#score<=60印這個(false)

#for else
num=int(input("質數測試 輸入:"))
if num == 2:
    print("%d是質數"%num)
else:
    for n in range(2,num):
        if num % n == 0:
            print("%d不是質數"%num)
            break
    else:
        print("%d是質數"%num)
#while迴圈
msg1='人機對話'
msg2='輸入 不要 可以結束對話'
msg=msg1+'\n'+msg2+'\n'+'= '
input_msg=''
while input_msg != '不要':
    input_msg=input(msg)
    print(input_msg)
    if input_msg !='不要':
        print(input_msg)

#巢狀while 99乘法表
i=1
while i<=9:
    j=1
    while j<=9:
        result=i*j
        print("%d*%d=%d"%(i,j,result), end=" ")
        j+=1
    print()
    i+=1
#enumerate
drinks=["coffee","tea","wine"]
for drink in enumerate(drinks):
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("*********************")
for drink in enumerate(drinks,10):
    print(drink)
for count, drink in enumerate(drinks,10):
    print(count, drink)

#元組tuple 用() 元素是固定的!!!
print()
numbers1=(1,2,3,4,5)
print(numbers1[2])
#可用for迴圈遍歷元組的元素
identity=('wei','MIS',109306035)
for id in identity:
    print(id)
#只能重新定義元組來改元素
numbers1=(1,6,7,8,9)
print(numbers1)

#如果不會改動元組，串列的method可用(例如len()，但append(),insert(),pop()不行)
#串列和元組可互換，例:list_numbers1=list(numbers1)

#zip 如有3對2情況只列兩個
fields=['lesson','credit','score']
info=['myth','3','80']
zipData=zip(fields,info)
student=list(zipData)
print(student)
#unzip
f,i=zip(*student)
print("fields = ",f)
print("info = ",i)
