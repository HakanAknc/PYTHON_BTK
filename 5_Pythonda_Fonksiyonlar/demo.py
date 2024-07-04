"""
def yasHesapla(dogumYili):
    return 2024 - dogumYili

hakan = yasHesapla(2001)
print(hakan)

def EmekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emekli oldunuz.")

EmekliligeKacYilKaldi(2001, "Hakan")

print(EmekliligeKacYilKaldi)
"""


# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("Hakan\n", 10)

print("**********************************")

def yazdir(kel, adet):
    return kel * adet

print(yazdir("Ahmet\n" ,10))