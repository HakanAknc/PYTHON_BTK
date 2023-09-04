# Aynı şeyi tekrar tekrar yazmamızın önünne geçiyor.
# def fonksiyonun anahtar kelimesi


# def bilgi_ver():
#     print("Hakan!")

# bilgi_ver()
# bilgi_ver()
# bilgi_ver()
# bilgi_ver()
# bilgi_ver()
# bilgi_ver()

# print("-*"*20)
# print("Hakan!")
# print("Hakan.")
# print("Hakan.")
# print("Hakan.")
# print("Hakan.")
# print("Hakan.")
# print("Hakan.")

# print("-*"*20)


# Ekrana sadece merhaba yazdırır
def selamla():
    print("Merhaba")
    
selamla()

print("-*"*20)



# Parametre alıyor bir değer girilmeli
def selamla(isim):
    print("Merhaba " + isim)
    
selamla("Hakan")

print("-*"*20)



# İki parametre alıyor değerleri toplar
def topla(x,y):
    print(f"x + y: {x + y}")

topla(25,27)

print("-*"*20)



# farklı stringler kullanılarak fonksiyona eklendi
def ortalama_hesapla(liste):
    toplam = sum(liste)  # listedeki sayıların toplamını verir
    adet = len(liste)   # eleman sayısını verir
    ortalama = toplam / adet
    print(f"Girilen sayıların ortalaması: {ortalama}")

ortalama_hesapla([1,2,3,4,5,6,7])

print("-*"*20)



def buyuk_harfe_cevir(metin):
    metin = metin.upper()  # upper fonksiyonu ile metine girilecek harfler buyuk harfe çevrildi 
    print(metin)           # ve metin değişkeninin içine eklendi burda metin yerine başka bişeyde yazılabilier

buyuk_harfe_cevir("hAkAn AkIncI")

print("-*"*20)



# Eğer ikinci parametreye her hangi bir değer girilmediyese bu varsayılan olarak admin yazar  ### merhaba Admin
# ama değer girilirse girilen isim ekranda gözükür ### merhaba Evren
def selamla(mesaj,isim = "Admin"):
    print(f"{mesaj} {isim}")

selamla("Merhaba")  # ("Merhaba",Evren) şekinde

print("-*"*20)


# Yukardaki işlemin benzeri
def indirim_yap(fiyat,yuzde = 20):
    indirimliMiktar = fiyat * (yuzde / 100)
    indirimliFiyat = fiyat - indirimliMiktar
    print(f"İndirimli tutar: {indirimliFiyat}")

indirim_yap(50,10)

print("-*"*20)


# Return işlemleri

def ortalama_hesaplama(x,y):
    return (x + y) / 2

a = ortalama_hesaplama(6,2)
b = ortalama_hesaplama(10,6)
print(a+b)

print("-*"*20)


def buyuk_harfler(metin):
    return metin.upper()

h = buyuk_harfler("aSdFghJKlşpel")
print(h)