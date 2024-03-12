#集合 元素唯一不重複
coding={'Python','Java','C','Python','Java','C'}
print(coding)#集合元素重複只保第一個，所以只有'Python','Java','C'(順序不定)
print(type(coding))

#串列不可當集合元素({'Python',[2,5,10]})，因為串列可變

#空集合?空字典?
x={}
print(type(x))#空字典!
y=set()
print(type(y))#空集合!

#字串變集合
z=set('DeepStone mean Deep Learing')
print(z)#會依序印出隨機但不重複的字母

#串列變集合
fruits=['apple','orange','apple','banana','banana']
setfruits=set(fruits)
print(setfruits)

#元組變集合
cities=('Taipei','Taichung','Taipei','Tainan','Taichung','Tainan','Tainan')
setcities=set(cities)
print(setcities)

print()

num1={1,2,3,4,5,6,7}
num2={2,4,6,7,8,9}

#交集
both1=num1 & num2
print("用&的交集為",both1)
both2=num1.intersection(num2)#和反過來num2.intersection(num1)一樣
print("用.intersection()的交集為",both2)

#聯集
all1=num1 | num2
print("用 | 的聯集為",all1)
all2=num1.union(num2)
print("用.union()的聯集為",all2)

#差集(兩者其一減重複)
num1_only1=num1-num2
print("用-的num1差集為",num1_only1)
num1_only2=num1.difference(num2)
print("用.difference()的num1差集為",num1_only2)
num1_only2_2=num2.difference(num1)
print("用.difference()的num2差集為",num1_only2_2)

#對稱差集(兩者減重複)
sydi1=num1^num2
print("用^的差集為",sydi1)
sydi2=num1.symmetric_difference(num2)
print("用.symmetric_difference()的差集為",sydi2)

#in、not in檢查元素是否屬於集合
print(1 in num1)
print(1 not in num1)
print()

#.add()，某個元素加入集合
cities={'Taipei','Taichung','Tainan'}
cities.add('Kaoshiung')
print(cities)
cities.add('Taipei')
print('加Taipei，重複所以不變:',cities)
tup=(1,2,3)
cities.add(tup)
print('加元組:',cities)

#.update()，某個集合裡的元素加入集合
cars1={'toyota','honda','bmw'}
cars2={'benz','audi'}
cars1.update(cars2)
print(cars1)

#.copy()也有deep copy,shallow copy之分

#.remove()即正常移除，.discard()也是移除但會傳回None，.pop()隨機移除並傳回移除的元素
animals={'dog','cat','cow','horse','sheep'}
animals.remove('dog')
print('remove dog:',animals)
animals.discard('cat')
print('discard cat:',animals,' 傳回',animals.discard('cat'))
popwhat=animals.pop()
print('隨機pop出:',popwhat,' 剩:',animals)
animals.clear()
print()

#.difference_update()用某集合刪另一個集合裡跟他重複的元素
birds1={'chicken','duck','rockstar'}
birds2={'duck','goose'}
birds1.difference_update(birds2)
print('difference_update: ',birds1)
print()

#isdisjoint()驗證有無交集、issubset()驗證是否為子集、issuperset()驗證是否為父集合
A={'a','b','c'}
B={'a','b','c','d','e','f'}
C={'f','g','h'}
print("A和B有交集傳回False:",A.isdisjoint(B)," A和C無交集傳回True:",A.isdisjoint(C))
print("A是B的子集傳回True:",A.issubset(B))
print("B是A的父集傳回True:",B.issuperset(A))
print("更多驗證:交集")
ret_value=A.intersection_update(B)
print(ret_value)
print(A)

#.symmetric_difference_update() 找(對稱)差集
motor1={'sym','duccati','mitsubishi','redgaton'}
motor2={'redgaton','gogoro','wemo'}
motor1.symmetric_difference_update(motor2)
print('對稱差集:',motor1)#上面執行完motor1就變了

#集合的函數
