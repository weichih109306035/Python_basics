#字典
fruits={'蘋果':20,'香蕉':59,'西瓜':299}#''內是鍵,:後是值
print(type(fruits))
print("西瓜一顆",fruits['西瓜'],"元")
#更改字典內容
fruits['西瓜']=309
print(fruits)
fruits['橘子']=25
print(fruits)
del fruits['香蕉']
print(fruits)
fruits.clear()#清空變{}
print(fruits)
del fruits#殺掉變未定義

#複製字典
fruits={'蘋果':20,'香蕉':59,'西瓜':299}
print("原本的",fruits)
cfruits=fruits.copy()
print("複製的",cfruits)

#字典也可以用len()找元素個數

#驗證元素存在
key=input("請輸入水果=")
value=input("請輸入價格=")
if key in fruits:
    print("%s有了"%key)
    if value!=fruits[key]:
        fruits[key]=value
else:
    print("%s原本沒有"%key)
    fruits[key]=value
    print("新的",fruits)

#印出鍵、值->.items()
for name,price in fruits.items():
    print("\n水果: ",name)
    print("價格: ",price)
#只要印出鍵->.keys()
for name in fruits.keys():
    print("\n水果: ",name)
#只要印出值->.values()
for price in fruits.values():
    print("\n價格: ",price)
    
#可用sorted()
players={'Lebron':'Heat','Kobe':'Lakes','Jordan':'Bull','Curry':'GS'}
for name in sorted(players.keys()):
    print(name)

#字典可組成串列

#字典內含串列
music={'indie':['JADE','vast&hazy'],
       'hippop':['snoopy dog','two pac'],
       'edm':['dj faded','alan walker']}
for kind,singer in music.items():
    print("%s有: "%kind)
    for sing in singer:
        print(sing)

#字典內含字典
home={'me':{
    'city':'Taipei',
    'district':'Songshan'},
      'grandma':{
          'city':'Taichung',
          'district':'West'}}
for user,info in home.items():
    print("使用者: ",user)
    print("城市: ",info)

#while在字典的應用
survey={}
market=True
while market:
    country=input("\n請輸入國家: ")
    site=input("請輸入景點: ")
    survey[country]=site
    repeat=input("還有嗎?(y/n)")
    if repeat !='y':
        market=False
print("\n市調結果: ")
for cou,sit in survey.items():
    print(cou," 的 ",sit)

#字典的方法
print("人數",len(home),"city數",len(home['me']),"district數",len(home['grandma']))
