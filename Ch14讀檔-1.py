#os模組 取得路徑
import os
print(os.getcwd())#得到目前檔案的目錄
print()
#os.path模組在os模組內，引os模組即可

#abspath()取得絕對路徑
print(os.path.abspath('.'))#.代表此檔案目前所在的資料夾(C:到Python入門)
print(os.path.abspath('..'))#..代表此檔案目前所在的資料夾的上一個資料夾(Desktop)
print(os.path.abspath('Ch14讀檔-1.py'))#全部

#relpath()取得相對路徑
print(os.path.relpath('C:\\'))#印出..\..\..\.. 代表Users\\thomas\\Desktop\\Python入門 即目前資料夾(Python入門)至C:\的相對路徑
print(os.path.relpath('C:\\Users\\thomas\\Desktop\\Python入門'))#印出.
print(os.path.relpath('C:\\','Ch14讀檔-1.py'))#印出..\..\..\..\.. 代表Users\\thomas\\Desktop\\Python入門\\Ch14讀檔-1.py 即Ch14讀檔-1.py至C:\\的相對路徑

#檢查路徑 exists()檢查檔案or資料夾存在 isabs檢查是否為絕對路徑 isdir()檢查是否為資料夾 isfile()檢查是否為檔案
print("Ch14讀檔-1此檔案或資料夾存在? ",os.path.exists('Ch14讀檔-1'))#要有.py才是正確的檔名
print("Ch14讀檔-1.py此檔案或資料夾存在? ",os.path.exists('Ch14讀檔-1.py'))
print("Desktop此檔案或資料夾存在? ",os.path.exists('C:\\Users\\thomas\\Desktop'))
print("---")

print("Ch14讀檔-1.py是絕對路徑? ",os.path.isabs('Ch14讀檔-1.py'))
print("C:\\Users\\thomas是絕對路徑? ",os.path.isabs('C:\\Users\\thomas'))
print("---")

print("Desktop是資料夾嗎? ",os.path.isdir('C:\\Users\\thomas\\Desktop'))
print("---")

print("Ch14讀檔-1.py是檔案嗎? ",os.path.isfile('C:\\Users\\thomas\\Desktop\\Python入門\\Ch14讀檔-1.py'))
print("---")

#檔案和資料夾的操作 mkdir()建立新資料夾or檔案 rmdir()移除資料夾or檔案(必須是空的) remove()刪除檔案 chdir(path)把目前資料夾改到path(換資料夾)
mydir='Ch14testdir'
if os.path.exists(mydir):#要建立資料夾之前最好都用exists()檢查一遍
    print("已經存在%s"%mydir)
else:
    os.mkdir(mydir)
    print("建立%s資料夾成功"%mydir)#會建立在Python入門資料夾裡

if os.path.exists(mydir):
    os.rmdir(mydir)
    print("刪除%s資料夾成功"%mydir)
else:
    print("%s資料夾不存在"%mydir)

myfile='Ch14testfile.py'
if os.path.exists(myfile):#要建立資料夾之前最好都用exists()檢查一遍
    print("已經存在%s"%myfile)
else:
    os.mkdir(myfile)
    print("建立%s檔案成功"%myfile)#會建立在Python入門資料夾裡

if os.path.exists(myfile):
    os.rmdir(myfile)
    print("刪除%s檔案成功"%myfile)
else:
    print("%s檔案不存在"%myfile)

#os.path.join()將字串以檔案路徑的樣子傳回 os.path.getsize()取得檔案大小 os.listdir()以串列形式傳回所有資料夾內容
files=['ch14_1.py','ch14_2.py','ch14_3.py']
for file in files:
    print(os.path.join('C:\\','Python','ch14',file))

print("Ch14讀檔-1.py的大小是: ",os.path.getsize("Ch14讀檔-1.py")," 位元組")

print("目前工作資料夾(Python入門)裡面有: ",os.listdir("."))
print()

totalnum=0
totalsize=0
print("列印目前工作目錄的所有檔案:")
for file in os.listdir("."):
    print(file,os.path.getsize(file))
    totalsize+=os.path.getsize(file)
    totalnum+=1
print("一共有: ",totalnum," 個, 總共大小為: ",totalsize," 位元組\n")

#glob.glob()找目前資料夾內含特定字的檔案
import glob
print("glob方法1: 列出\\Users\\thomas\\Desktop\\Python入門 資料夾的所有檔案")
for file in glob.glob('C:\\Users\\thomas\\Desktop\\Python入門\*.*'):
    print(file)
print()

print("glob方法2: 列出目前資料夾(Python入門)內有特定字(Ch)的所有.py檔案")
for file in glob.glob('Ch*.py'):
    print(file)
print()

print("glob方法3: 列出目前資料夾(Python入門)內有特定字(Ch1)的所有檔案")
for file in glob.glob('Ch1*.*'):
    print(file)

#os.walk()可遍歷資料夾，順序為: 目前資料夾->子資料夾->檔案(見課本)
