def sayHello(name = "user"):
    return "Hello "+ name

msg = sayHello("Hakan")
msg = sayHello("Evren")
msg = sayHello()   # Hello user

print(msg)


def total(num1,num2):
    return num1 + num2

result = total(10,26)
result = total(45,78)

print(result)


def yasHesapla(dogumYil):
    return 2023 - dogumYil

hakan = yasHesapla(2001)
evren = yasHesapla(2019)
eyup = yasHesapla(2013)

print(hakan, evren, eyup)


def EmekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(1983, "Adnan")
EmekliligeKacYilKaldi(2001, "Hakan")
EmekliligeKacYilKaldi(1986, "Atıf")

print(help(EmekliligeKacYilKaldi))


list = [1,2,3]

print(help(list.append))