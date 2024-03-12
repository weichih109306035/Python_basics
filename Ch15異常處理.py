def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("抓到except 除數不可為0!")
'''
也可try:
        x/y
    except ...:
        print(...)
    else:#增加程式可讀性而已
        return x/y
'''     
print(division(10,2))
print(division(10,0))#先印出excpet的訊息 再印出結果為None

fn='大二上必修.txt'
try:
    with open(fn) as file_Obj:
        data=file_Obj.read()
except Exception:#本用FileNotFoundError,但Exception可直接代替一般錯誤
    print("抓到except 找不到 %s 檔案!"%fn)
else:
    print(data)

#data=file_Obj.split()可以將txt檔轉成串列

#raise丟出異常
def password(pwd):
    pwdlen=len(pwd)
    if pwdlen<5:
        raise Exception('密碼長度太短')
    if pwdlen>10:
        raise Exception('密碼長度太長')
    print("密碼長度允許")
for pwd in ('aabbccdd','abc','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'):
    try:
        password(pwd)
    except Exception as err:
        print("不允許: ",str(err))

#traceback模組
import traceback

'''
#assert
class MyBank():
    title='citi bank'
    def __init__(self,uname,money):
        self.name=uname
        self.balance=money
    def save_money(self,money):
        assert money>0, '存款money必須大於0'
        self.balance+=money
        print("存款: ",money," 完成")
    def withdraw_money(self,money):
        assert money>0, '提款money必須大於0'
        assert money<=self.balance, '存款金額不足'
        self.balance-=money
        print("提款 ",money," 完成")
    def get_balance(self):
        print(self.name.title()," 目前餘額: ",self.balance)
mybank=MyBank('wei',100)
mybank.get_balance()
mybank.save_money(300)
mybank.get_balance()
mybank.save_money(-300)
mybank.get_balance()
'''

#logging模組
import logging
