# Miras alma Inheritance

class Calisan:  # Bu class hiçbir yerden miras almıyor

    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"

    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Maas: {} email: {}".format(self.isim,self.soyisim,self.maas,self.email)

calisan1 = Calisan("Hakan","Akıncı",5000)
calisan2 = Calisan("Evren","Akıncı",6000)


class Yazilimci(Calisan):   # Ama bu class Calisan classından miras alıyor o yuzden parantez var
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)   # miras aldığın kılasın adı super() olur  ama aşağdaki şekilde yazılabilier
        # self.isim = isim
        # self.soyisim = soyisim
        # self.maas = maas
        # self.email = isim + soyisim + "@sirket.com"
        self.bildigi_dil = bildigi_dil
    
    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Maas: {} email: {} Bildiği dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)

yazilimci1 = Yazilimci("Ayşe","Yıldız",7000,"Python")
yazilimci2 = Yazilimci("Eyüpcan","Akıncı",8000,"Java")

print(calisan2.bilgileri_goster())
print(yazilimci1.bilgileri_goster())
