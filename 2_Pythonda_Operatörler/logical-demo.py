# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
a = int(input("Sayı girin: "))
val = (0 < a) and (a <= 100)
print(f'sayı 0-100 arasındamı: {val}')



# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
b = int(input("Sayı girin: "))
val = (b > 0) and (b % 2 == 0)
print(f'sayı pozitif çift sayı mı: {val}')



# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
email = 'email@hakanakinci.com'
password = 'abc123'

email = "email@hakanakinci.com"
password = "abc123"

girilenEmail = input("email: ")
girilenPassword = input("password: ")

giris = (email == girilenEmail) and (password == girilenPassword)
print(f"Girilen email {girilenEmail} ve password {girilenPassword} doğru mu: {giris}")



# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

siralama = (x > y) and (x > z)
print(f"x en büyükdür: {siralama}")

siralama = (y > x) and (y > z)
print(f"y en büyükdür: {siralama}")

siralama = (z > x) and (z > y)
print(f"z en büyükdür: {siralama}")



# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input("Vize1: "))
vize2 = float(input("Vize2: "))
final = float(input("Final: "))

ortalama = ((vize1 + vize2) / 2)*0.6 + (final * 0.4)
print("Ortalama: ", ortalama)

val = (ortalama >= 50) and (final >= 50)
val = (ortalama >= 50) or (final >= 70)

print(f"Öğrencinin ortalaması: {ortalama} geçme durumu {val}")



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
name = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))

index = ( kg ) / ( hg**2 )
print("İndeks: ",index)

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index < 24.9)
kilolu = (index > 24.9) and (index < 29.9)
obez = (index >= 29.9 ) and (index <= 34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")
