'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('sayı: '))

if (sayi > 0) and (sayi<=100):
    print('sayı 0-100 arasında.')            
else:
    print('sayı 0-100 arasında değildir.')
'''

x = int(input("Sayı girin: "))        # Kendi çözümüm

if 0 < x < 100:
    print("X bu aralıkta")
else:
    print("uçtunuz")




'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
if (sayi > 0):
    if (sayi % 2 ==0):
        print('girilen sayı pozitif çift sayıdır.')
    else:
        print('girilen sayı pozitif ancak sayı tek.')
else:
    print('girilen sayı negatif sayı.')
'''

a = int(input("Sayı girin: "))

if (a > 0):
    if (a % 2 == 0):
        print("sayı pozitif çift sayıdır.")
    else:
        print("Sayı çift değildir.")
else:
    print("Sayı pozitif değildri")




'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('password: ')
if (girilenEmail == email):
    if (girilenPassword == password): 
        print('uygulamaya giriş başarılı.')
    else:
        print('parolanız yanlış')
else:
    print('email bilginiz yanlış')
'''

email = input("email girin: ")
password = input("password girin: ")

istenilenEmail = "hakanakinci@gmail.com"
istenilenPassword = "123456"

if (email == istenilenEmail):
    if (password == istenilenPassword):
        print("Giriş BAŞARILI ")
    else:
        print("Password hatalı")
else:
    print("Email hatalı")




'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if (a > b) and  (a > c):
    print(f'a en büyük sayıdır.')
elif (b > a) and (b > c):
    print(f'b en büyük sayıdır.')
elif (c > a) and (c > b):
    print(f'c en büyük sayıdır.')
'''

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if (x > y) and (x > z):
    print("x büyüktür")
elif (y > x) and (y > z):
    print("y büyüktür")
else:
    print("z büyüktür")




'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
   
vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))
ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
result = (ortalama>=50) and (final>=50)
result = (ortalama >=50) or (final>=70)
** durum-1
if (ortalama>=50):
    if (final>=50):  
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız. Finalden en az 50 almalısınız.')
else:
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')
** durum-2
if (ortalama >=50):
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
else:
    if (final>=70):
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')
'''

vize1 = int(input("Vize 1: "))
vize2 = int(input("Vize 2: "))
final = int(input("Finla: "))

ortalama = (((vize1 + vize2)/2)*0.6 + (final * 0.4))
print("Ortalama: ",ortalama)

val = (ortalama >= 50) and (final >= 50)
val = (ortalama >= 50) or (final >= 70)


# 1.durum
if (ortalama > 50):
    if (final >= 50):
        print(f"Öğrencinin ortalaması {ortalama} geçme durumu: başarılı")
    else:
        print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu: başarısız finalden en az 50 almalısınız")
else:
    print(f"Öğrencinin ortalaması {ortalama} geçme durumu: başarısız")

# 2.durum
if (ortalama >= 50):
    print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı")
else:
    if (final >= 70):
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')





"""
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4    => Zayıf 
   18.5-24.9 => Normal  
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman (Obez)
"""

isim = input("İsminizi girin: ")
kilo = float(input("Kilonuzu girin: "))
boy = float(input("Boyunuzu girin :"))

index = (kilo / boy **2)
print("İndex: ", index)

if (index >= 0) and (index <= 18.4):
     print(f'{isim} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
elif (index > 18.5) and (index <= 24.9):
    print(f'{isim} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index > 25.0) and (index <= 29.9):
    print(f'{isim} kilo indeksin: {index} ve kilo değerlendirmen fazla kilolu.')
elif (index > 30.0) and (index <= 34.9):
    print(f'{isim} kilo indeksin: {index} ve kilo değerlendirmen şişman (obez).')
else:
    print("Yanlış değer girdiniz")