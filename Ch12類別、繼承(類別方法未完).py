#預設沒參數的constructor，不用寫
class Bank1():#即class Bank1(object)，所有類別必由object繼承而來
    title='standard'
    def feature(self):
        return 'green and blue'
account_li=Bank1()
print("li的銀行顏色是 ",account_li.feature())
#預設有參數的constructor，即__init__(self,參數,參數,......)
class Bank2():
    def __init__(self,username,money):
        self.name=username#把外面傳進來的username賦給Bank2的name(self.name)
        self.balance=money#也可一開始__init__(self,username)，self.balance=0
        self.__title="union"
    def original_bank_title(self):
        return self.__title#這樣可以已讓繼承的ZhongShan_Bank取得private的title
    def get_balance(self):
        print(self.name.title(),"目前餘額 ",self.balance)#title()返回第一個字為大寫的字串，例:he is good->He Is Good
    def save_money(self,money):
        self.balance+=money
        print("存款 ",money," 完成")
    def withdraw_money(self,money):
        self.balance-=money
        print("提款 ",money," 完成")
account_lu=Bank2('lu',10000)
account_lu.get_balance()
account_lu.save_money(1000)
account_lu.get_balance()
account_lu.withdraw_money(2999)
account_lu.get_balance()
print(account_lu.original_bank_title())
print()

#上面為公有public屬性，類別外可直接更改類別內的值，有安全性問題
print("公有銀行遭駭客入侵!gg!")
account_lu.balance=100
print("經過駭客竄改: ",end="")
account_lu.get_balance()
print()

#私有private屬性 例:self.balance=0->self.__balance=0
class Bank3():
    def __init__(self):
        self.__balance=1000
    def get_balance(self):
        print("an 目前餘額 ",self.__balance)
account_an=Bank3()
account_an.get_balance()
print("私有銀行遭駭客入侵!沒事!")
account_an.balance=100
print("經過駭客竄改: ",end="")
account_an.get_balance()
print()

#私有方法 例:def save_money(self,money)->def __save_money(self,money)

#繼承
class ZhongShan_Bank(Bank2):
    pass
account_zhongshan=ZhongShan_Bank('zs',5000)
account_zhongshan.get_balance()
print("中山分行屬於: ",account_zhongshan.original_bank_title())
print()

class Pet():
    def __init__(self,pet_name,pet_weight):
        self.name=pet_name
        self.weight=pet_weight
    def cute(self):
        print(self.name.title()," is cute.")
class Puppy(Pet):
    def __init__(self,puppy_name,puppy_weight):
        super().__init__('My pet '+puppy_name.title(),puppy_weight)
mypet=Pet('xw',200)
print(mypet.name.title(),' is ',mypet.weight," g.")
mypet.cute()
mypuppy=Puppy('chimmy',100)
print(mypuppy.name.title(),' is ',mypuppy.weight," g.")
mypuppy.cute()

#三代同堂例題:孫子抓祖父屬性+兄弟互抓屬性
class Grandfather():
    def __init__(self):
        self.grandfather_money=1000000
    def get_info1(self):
        print("Grandfather's information")
class Father(Grandfather):
    def __init__(self):
        self.father_money=10000
        super().__init__()
    def get_info2(self):
        print("Father's information")
class Brother(Father):
    def __init__(self):
        self.brother_money=100
        super().__init__()#可抓到祖父
class Boy(Father):
    def __init__(self):
        self.boy_money=0
        super().__init__()
    def get_info3(self):
        print("Boy's information")
    def get_money(self):
        print("\nBoy資產: ",self.boy_money,
              "\nBrother資產: ",Brother().brother_money,#同繼承級別用class抓
              "\nFather資產: ",self.father_money,
              "\nGrandfather資產: ",self.grandfather_money)
boy=Boy()
boy.get_info3()
boy.get_info2()
boy.get_info1()

boy.get_money()

#多型:不同類別有相同方法名稱，由物件判斷類別再判斷哪一方法(java overload override)

#多重繼承
class Grandmother():
    def action1(self):
        print("Granny")
class Mother(Grandmother):
    def action2(self):
        print("Mommy")
class Aunt(Grandmother):
    def action2(self):
        print("Aunty")
class Girl(Mother,Aunt):#有先後之分
    def action3(self):
        print("Girl")
girl=Girl()
girl.action2()#先繼承Mother，所以只執行Mother的action2

#type(),isinstance(),__doc__,__name__,__str__(),__repr__(),__iter__()
grandmother=Grandmother()
mother=Mother()
aunt=Aunt()
print("Grandmother物件類型: ",type(grandmother)," action1方法類型: ",type(grandmother.action1))
print("girl屬於Girl類別所以: ",isinstance(girl,Girl))
print("mother屬於Grandmother類別所以: ",isinstance(mother,Grandmother))
print("grandmother不屬於Aunt類別所以: ",isinstance(grandmother,Aunt))
print("aunt不屬於Mother類別所以: ",isinstance(aunt,Mother))

class Myclass:
    '''Myclass類別的註解'''
    def __init__(self,x):
        self.x=x
    def printMe(self):
        '''Myclass類別內printMe方法的註解'''
        print("HI",self.x)
data=Myclass(666)
data.printMe()
print("data.__doc__沒特別引用方法，得到Myclass的註解: ",data.__doc__)
print("data.printMe.__doc__引用printMe方法，得到printMe的註解: ",data.printMe.__doc__)
