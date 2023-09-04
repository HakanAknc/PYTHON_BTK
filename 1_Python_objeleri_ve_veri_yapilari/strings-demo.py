website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
resualt = len(course)
lenght = len(website)
# print(resualt)
# print(website)


# 2- 'website' içinden www karakterlerini alın.
resualt = website[7:10]
# print(resualt)


# 3- 'website' içinden com karakterlerini alın.
resualt = website[22:25]
resualt1 = website[-3:]
resualt2 = website[lenght-3:lenght]
# print(resualt)
# print(resualt1)
# print(resualt2)


# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
lenght = course[:15]
lenght1 = course[-15:]
# print(lenght)
# print(lenght1)


# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
lenght = course[::-1]    #  => [::] büütün karekterleri alır     => [::-1] bütün karekterleri tersten yazdırır
# print(lenght)


# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

tanitim = "Benim adım {0} {1}, yaşım {2} ve mesleğim {3}.".format(name, surname, age, job)
tanitim1 = "Benim adım "+ name +" "+ surname +" " + "yaşım " + str(age) + " mesleğim " + job 
tanitim2 = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
# print(tanitim)
# print(tanitim1)
# print(tanitim2)


# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
# print(s)


# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
harf = "abc " * 3
print(harf)