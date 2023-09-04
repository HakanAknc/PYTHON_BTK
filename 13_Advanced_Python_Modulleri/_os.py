# Os modülü Python'da hazır olarak gelen , dosya ve dizinlerde kolaylıkla işlemler yapmamızı sağlayan bir modüldür.

import os

result = dir(os)
result = os.name  # nt demek windows işletim sistemini kullanıyorsun demek
# result = os.getcwd()

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")                 # -- oluşturma
# os.makedirs("newdirectory/yeniklasör")   # -- oluşturma
# os.rename("newdirectory","yeniklasör")   # -- oluşturma
# os.rmdir("newdirectory")                 # -- silme
# os.removedirs("yeniklasör/yeniklasör")   # -- silme

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe")

# path

# result = os.path.abspath("_os.py")
# result = os.path.dirname("C:/python/advanced-modules/_os.py")
# result = os.path.dirname(os.path.abspath("_os.py"))
# result = os.path.exists("C:/python/advanced-modules/_os1.py")
# result = os.path.exists("C:/python/advanced-modules")
# result = os.path.isdir("C:/python/advanced-modules")
# result = os.path.isfile("C:/python/advanced-modules/_os.py")
# result = os.path.join("C:\\","deneme","deneme1")
# result = os.path.split("C:\\deneme")
# result = os.path.splitext("_os.py")
# # result = result[0]
# result = result[1]

print(result)