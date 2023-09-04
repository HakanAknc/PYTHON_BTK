# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]
print(arabalar)


# 2-  Liste Kaç elemanlıdır ?
print(len(arabalar))


# 3-  Listenin ilk ve son elemanı nedir ?
print(arabalar[0])
print(arabalar[-1])


# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[-1] = "Toyato"
print(arabalar) 


# 5-  Mercedes listenin bir elemanı mıdır ?
print("Mercedes" in arabalar)    # in operatörü istenen değeri arar


# 6-  Listenin -2 indeksindeki değer nedir ?
print(arabalar[-2])


# 7-  Listenin ilk 3 elemanını alın.
print(arabalar[0:3])


# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ['Toyota','Renault']       # Değişiklik yapıldı
print(arabalar)


# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
arabalar = arabalar + ["Auid", "Nissan"]   # Üzerine eklendi
print(arabalar)


# 10- Listenin son elemanını silin.
del arabalar[-1]     # Silme işlemini gerçeklestirir
print(arabalar)


# 11- Liste elemanlarını tersten yazdırınız.
print(arabalar[::-1])   # Tersten yazdırır


# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan  1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90) 
"""
studentA = ["Yiğit Bilgi 2010", "(70,60,70)"]
studentB = ["Sena Turan  1999, (80,80,70)"]            # Kendi Çözümüm 
studentC = ["Ahmet Turan 1998, (80,70,90)"]

studentS = studentA + studentB + studentC
print(studentS)
"""
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

print(studentA)
print(studentB)
print(studentC)


# 13- Liste elemanlarını ekrana yazdırınız.
print(studentA[1])
print(studentB[2])
print(studentC[3])

print()
a = f"{studentA[0]} {studentA[1]} {2019 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(a)
