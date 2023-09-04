# 1- Girilen 2 sayıdan hangisi büyüktür ?
a = int(input("a: "))
b = int(input("b: "))

result = (a > b)
print(f"a: {a} b: {b} den büyüktür. {result}")


# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2)*0.6) + (final * 0.4)
print("Ortalama: ", ortalama)

print(f"Not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>50}")


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
x = int(input("Sayı giriniz: "))

tekcift = (x % 2 == 0)

print(f"Girilen sayı çift olma durumu {tekcift}")


# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
y = int(input("Sayı giriniz: "))

pozneg = (y > 0)

print(f"Girilen sayı pozitif olma durumu {pozneg}")


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email = "email@hakanakinci.com"
pasword = "abc123"

girilenEmail = input("email: ")
girilemPasword = input("pasword: ")

isEmail = (email == girilenEmail.lower().split())
isPasword = (pasword == girilemPasword.lower())

print(f"Girilen email bilgisi doğrumu {isEmail}, ve girilen pasword doğrumu {isPasword}")
