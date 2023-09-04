
'''
Soru: Girilen bir sayının asal olup olmadığını bulun.

** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''

sayi = int(input("Sayı giriniz: "))
asalMi = True

if (sayi == 1):    # Özel bi durum 
    asalMi = False

for i in range(2,sayi):    # 2'den başlayıp seçtiğmiz sayıya kadar
    if (sayi % i == 0):    # sayi eğer i'ye tam bölünüyorsa asal değildir ve break ile döngüyü durdur.
        asalMi = False
        break

if asalMi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")