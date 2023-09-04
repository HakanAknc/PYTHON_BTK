# Ders 1
"""
class calisan:   # class oluşturuldu
    def __init__(self,name,surname,age):  # değişkenler oluşturuldu

        self.name = name
        self.surname = surname
        self.age = age
    
    def show_info(self):
        print(f"Ad:{self.name}  Soyad:{self.surname}  Yaş:{self.age}")

calisan1 = calisan("Hakan","Akıncı",22)   # çağırıldı
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2 = calisan("Evre","Akıncı",5)
print(calisan2.name,calisan2.surname,calisan2.age)

calisan3 = calisan("Eyüpcan","Akıncı",12)
print(calisan3.name,calisan3.surname,calisan3.age)

print()

calisan1.show_info()
calisan2.show_info()
calisan3.show_info()
"""



# Ders 2
"""
class calisan:
    def __init__(self,name,wage):
        self.name = name
        self.wage = wage

calisan1 = calisan("Ali",5000)
calisan2 = calisan("Caner",8000)

# print(calisan1.__dict__)  # -- çalişan1'in verileirini sözlük gibi ekrana yazar
"""




# Ders 3
"""
class kisi:
    def __init__(self,name,age):
        self.name = name
        self.age = age

kisi1 = kisi("Atıf",22)
kisi2 = kisi("Adnan",24)

print(kisi1.name,kisi1.age)
"""




# Ders 4 -- Inheritance | Kalıtım -1   -- miras alma
"""
class Calisan:
    zam_orani = 1.1
    def __init__(self,name,surname,wage):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.email = name + surname + "@sirket.com"
    
    def bilgileri_goster(self):
        return "Ad: {}  Soyad: {}  Maaş: {}  E-mail: {}".format(self.name,self.surname,self.wage,self.email)


calisan1 = Calisan("Ali","Çalışkan",5000)
calisan2 = Calisan("Mehmet","Yıldız",6000)

print(calisan1.name,calisan1.surname,calisan1.wage,calisan1.email)

class Yazilimci(Calisan):
    def __init__(self, name, surname, wage, bildigi_dil):
        super().__init__(name,surname,wage)       # -- yukardaki değişknelerin hepsi super() değişkenin içinde var
        # self.name = name
        # self.surname = surname
        # self.wage = wage
        # self.email = name + surname + "@sirket.com"
        self.bildigi_dil = bildigi_dil            # -- bu fonksiyon yukarda olmadığı için super()'in içine yazıldı

    zam_orani = 1.2
    def bilgileri_goster(self):
        return "Ad: {}  Soyad: {}  Maaş: {}  E-mail: {}  Dil: {}".format(self.name,self.surname,self.wage,self.email,self.bildigi_dil)

yazilimci1 = Yazilimci("Ayşe","Yılmaz",7000,"Python")
yazilimci2 = Yazilimci("Berna","Atıcı",8000,"Java")

print()

print(calisan2.bilgileri_goster())
print(yazilimci1.bilgileri_goster())
"""





# Ders 5 -- Inheritance | Kalıtım - 2  -- miras alma
class Calisan:
    zam_orani = 1.1
    def __init__(self,name,surname,wage):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.email = name + surname + "@sirket.com"
    
    def bilgileri_goster(self):
        return "Ad: {}  Soyad: {}  Maaş: {}  E-mail: {}".format(self.name,self.surname,self.wage,self.email)


calisan1 = Calisan("Ali","Çalışkan",5000)
calisan2 = Calisan("Mehmet","Yıldız",6000)

print(calisan1.name,calisan1.surname,calisan1.wage,calisan1.email)

class Yazilimci(Calisan):
    def __init__(self, name, surname, wage, bildigi_dil):
        super().__init__(name,surname,wage)       # -- yukardaki değişknelerin hepsi super() değişkenin içinde var
        # self.name = name
        # self.surname = surname
        # self.wage = wage
        # self.email = name + surname + "@sirket.com"
        self.bildigi_dil = bildigi_dil            # -- bu fonksiyon yukarda olmadığı için super()'in içine yazıldı

    zam_orani = 1.2
    def bilgileri_goster(self):
        return "Ad: {}  Soyad: {}  Maaş: {}  E-mail: {}  Dil: {}".format(self.name,self.surname,self.wage,self.email,self.bildigi_dil)

class Yonetici(Calisan):
    def __init__(self,name,surname,wage,calisanlar = None):
        super().__init__(name,surname,wage)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisanlari_goster(self,calisan):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())


yazilimci1 = Yazilimci("Ayşe","Yılmaz",7000,"Python")
yazilimci2 = Yazilimci("Berna","Atıcı",8000,"Java")


yonetici1 = Yonetici("Metin","Ali",10000)

yonetici1.calisan_ekle(calisan1)
yonetici1.calisan_ekle(yazilimci1)
yonetici1.calisanlari_goster(calisan1)