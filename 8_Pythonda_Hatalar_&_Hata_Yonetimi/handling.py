# error handling => hata yönetimi


# 1 try
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:   # sıfıra bölme hatası
#     print("y için 0 girilemez.")
# except ValueError:        # strıng girme hatası
#     print("x ve y için sayısal değer giriniz.")



# 2 try
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError, ValueError):
#     print("Yanlış değer girdiniz.")
    


# 3 try
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except:                 // -- hata bilinmiyor bu koda
#     print("Yanlış değer girdiniz.")
    


# 4 try
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError, ValueError):
#     print("Yanlış değer girdiniz.")
# else:
#     print("Her şey yolunda :)")
    

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Yanlış değer girdiniz.", ex)
    else:
        break
    finally:                                     # nolursa olsun çalışır
        print("try except sonlandı.")
    