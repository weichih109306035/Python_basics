def greeting1():
    print("Good Morning!")
greeting1()
print(type(greeting1()))#回傳NoneType

def greeting2(name):#可在idle處輸入想要的name
    print(name,",Good Morning!")#也可用(name+"Good Morning")
greeting2('Tom')

def minus1(x1,x2):
    print(x1-x2)#可改成return x1-x2
print("相減的函數")
a=int(input("a= "))
b=int(input("b= "))
print("a-b= ",end="")#end=""即不換行
minus1(a,b)

#參數可預設，例:def minus(x1,x2=5)
#print()處也可以預設，例:def greeting(name1,name2):
                             #print(name2="steve",name1="tiff")

def guest_info(firstname,lastname,gender,middlename=''):#可能有人沒middlename所以預設為''
    if gender=="M":
        welcome=lastname+middlename+firstname+'先生歡迎'
    elif gender=='F':
        welcome=lastname+middlename+firstname+'小姐歡迎'
    else:
        welcome=lastname+middlename+firstname+'歡迎'
    return welcome
guest1=guest_info('明','王','M','小')
guest2=guest_info('美','王','F')
guest3=guest_info('?','?','?','?')
print(guest1)
print(guest2)
print(guest3)

#建立一個字典函數
def build_vip(id,name,tel=''):
    vip_dict={'VIP_ID':id,'Name':name}
    if tel:#解釋:如果有tel資訊，則視tel=true
        vip_dict['Tel']=tel
    return vip_dict
while True:
    print("建立VIP帳號")
    idnum=input("請輸入ID: ")
    name=input("請輸入姓名: ")
    tel=input("請輸入電話（不強制）: ")#原本預設空值，可按enter鍵跳過
    member=build_vip(idnum,name,tel)
    print(member,'\n')
    repeat=input("是否繼續?(y)")
    if repeat != 'y':
        break
print("謝謝光臨!")
print()

#參數是串列時
def uberpanda(ordered,delivered):
    print("---外送平台---")
    while ordered:#orderlist(ordered)還有元素就是True
        current_meal=ordered.pop()
        print("待運送: ",current_meal)
        delivered.append(current_meal)
def show_ordered(ordered):
    print("---單子內容---")
    if not ordered:
        print("沒接到單!","\n")
    for ordered_meal in ordered:
        print(ordered_meal)
def show_delivered(delivered):
    print("---已送達---")
    if not delivered:
        print("沒有已送達的!")
    for delivered_meal in delivered:
        print(delivered_meal)
orderlist=['麥當勞','肯德基','漢堡王','摩斯']
deliverlist=[]
show_ordered(orderlist)
show_delivered(deliverlist)
uberpanda(orderlist[:],deliverlist)#orderlist[:]\是shallow copy,避免後面orderlist有變動
print()
print("---運送中---","\n")
show_ordered(orderlist)#有shallow copy回傳的orderlist即原本的
show_delivered(deliverlist)
print()

#任意數量的參數
def make_icecream(icecream_type,*toppings):#*toppings代表可將一或多個參數傳入
    print("這個 ",icecream_type," 冰淇淋配料如下")
    for topping in toppings:
        print("--",topping)
make_icecream('香草','巧克力')
make_icecream('芒果','煉乳','碎片','布丁')
print()

#任意數量的關鍵字參數做出字典
def nba_dict(player,*age,**other_info):#**other_info可接受一或多個關鍵字參數
    info={}
    info['Player']=player
    info['Age']=age
    for key,value in other_info.items():
        info[key]=value
    return info
kobe_dict=nba_dict('Kobe','8','24',Team='Lakers',City='LA')
print(kobe_dict,"\n")

#遞迴函數 階乘
def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
value=10
print(value,"的階乘=",factorial(value))
print()

#local variable影響某一函數，global variable影響整個程式
def printmsg():
    msg='local variable'
    print("函數列印: ",msg)
msg='global variable'
print("主程式列印: ",msg)
printmsg()
print()

#匿名函數lambda，可有許多參數，可讓程式更簡潔
square=lambda x:x**2
print(square(10))
product=lambda x,y:x*y
print(product(9,9))

def oddfn(x):
    return x if (x%2==1)else None
mylist=[5,10,15,20,25,30]
filter_object=filter(oddfn,mylist)#filter(function,iterable)可依次將iterable的item(list,tuple,string...)傳入function，傳出的值隨iterable型態展示
print("奇數串列by 原本: ",[item for item in filter_object])

oddlist=list(filter(lambda x:(x%2==1),mylist))
print("奇數串列by lambda: ",oddlist)

#map()和filter()差別:map()必傳回list型態

#pass 不執行直接跳過 對於規劃多函數的程式時有利
def forfun(arg):
    pass
