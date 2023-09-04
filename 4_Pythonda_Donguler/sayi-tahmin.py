'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)

   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
''' 

# 1.Çözüm
# import random

# sayi = random.randint(1, 10)
# hak = 5
# sayac = 0

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input("Tahmin: "))

#     if sayi == tahmin:
#         print(f"Tebreikler {sayac}. defada bildiniz.")
#         break
#     elif sayi > tahmin:
#         print("Yukarı")
#     else:
#         print("Aşağı")

#     if hak == 0:
#         print(f"Hakkınız bitti. Tutulan sayı: {sayi}")  


# 2.Çözüm
import random

sayi = random.randint(1, 10)
can = int(input("Kaç hak istersinz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == hak:
        print(f"Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1) }")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if sayi == tahmin:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")




