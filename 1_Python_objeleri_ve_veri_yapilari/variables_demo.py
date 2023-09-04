"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""

""""
BU BENİM ÇÖZÜMÜM

musteriAd = "Hakan"
musteriSoyad = " Akıncı"
print(musteriAd + musteriSoyad)

musteriCinsiyet = "Erkek"
print(musteriCinsiyet)
musteriTC = "123456789"
print(musteriTC)
musteriDogum = "20.10.2001"
print(musteriDogum)
musteriAdres = "Antalya / Kumluca"
print(musteriAdres)
musteriYas = "21"
print(musteriYas)
"""


musteriAdi = "Hakan"
musteriSoyad = "Akıncı"
musteriAdSoyad = musteriAdi + " " + musteriSoyad
musteriCinsiyet = True  #>Erkek
musteriTC = "1234567890"
musteriDogum = 2001
musteriAdres = "Antalya / Kumluca"
musteriYas = 2023 - musteriDogum
print(musteriYas)





print()
"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""
siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95

toplam = siparis1 + siparis2 + siparis3
print("Topalm = " , toplam)
