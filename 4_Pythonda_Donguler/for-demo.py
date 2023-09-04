sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?

for i in sayilar:
    if (i % 3 == 0):
        print(i)

# 2- Sayilar listesinde sayıların toplamı kaçtır ?

toplam = 0
for i in sayilar:
    toplam += i
print("Toplam: ", toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.

for i in sayilar:
    if (i % 2 == 1):
        print(i**2)



print()
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

for sehir in sehirler:
    if (len(sehir) <= 5):    # Karekter sayısını almış oluruz
        print(sehir)


print()
urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?

toplam = 0

for urun in urunler:
    fiyat = int(urun["price"])         # fiyat listesi integer çevrildi
    toplam += fiyat
print("Toplam ürün fiyatı: ",toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
    fiyat = int(urun["price"])
    if (fiyat <= 5000):
        print(urun["name"])

"""
# 2.Çözüm
for urun in urunler: 
    if (int(urun['price']) <= 5000):
        print(urun['name'])
"""