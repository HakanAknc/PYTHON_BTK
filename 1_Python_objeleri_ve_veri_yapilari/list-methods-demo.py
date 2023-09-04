names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]


# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)


# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)


# 3-  "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)
names.pop()   # => Siler


# 4-  "Hakan" isminin indeksi nedir ?
index = names.index("Hakan")
print(index)


# 5-  "Ali" listenin bir elemanı mıdır ?
print("Ali" in names)


# 6-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)


# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)


# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)


# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Daci"
print(str.split(','))


# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(max(years))
print(min(years))


# 11- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))


# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)




# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []                 # => boş liste oluşturuldu

marka = input("marka: ")       # => kullanıcıdan marka alındı
markalar.append(marka)         # => alınan marka, markalara append edildi

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)