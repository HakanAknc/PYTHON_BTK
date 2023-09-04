# Class oluşturma

# class sirket:
#     pass

# sirket1 = sirket()

# sirket1.name = "Evren"
# sirket1.surname = "Akıncı"
# sirket1.age = 5
# print(sirket1.name)
# print(sirket1.surname)

print()
# Bir classa bağlı olan fonksiyonlara metot denir

class calisan:
    def __init__(self,name,surname,age): # (self,a,b,c) de olabilir
        self.name = name   # self.name = a  de olabilir
        self.surname = surname  # oluşturulan nesne demektir
        self.age = age

    def show_info(self):  # selfin içi otamatik olarak calisan1 olucak
        print(f"Ad: {self.name}  Soyad: {self.surname}   Yaş: {self.age}")

calisan1 = calisan("Hakan","Akıncı",22)  # yukardaki self çalışan1 oluyor
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2 = calisan("Evren","Can",5)   # yukardaki self çalışan2 oluyor
print(calisan2.name,calisan2.surname,calisan2.age)

calisan1.show_info()  # içine birşey yazılmicak
calisan2.show_info()

print()
print()


class aylikcilar:
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas

aylikcilar1 = aylikcilar("Caner",5000)
aylikcilar2 = aylikcilar("Eyüpcan",7000)

print(aylikcilar1.__dict__)
print(aylikcilar2.__dict__)