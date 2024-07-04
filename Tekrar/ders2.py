class Account():
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    
    def hesapBilgileri(self):
        print("İsim : ",self.isim)
        print("Numara : ",self.numara)
        print("Bakiye : ",self.bakiye)
    
    def parCek(self,miktar):
        if(self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli değil...")
        else:
            self.bakiye -= miktar
            print("Yeni bakiye: ",self.bakiye)
    
    def paraYatir(self,miktar):
        self.bakiye += miktar
        print("Yeni bakiye : ",self.bakiye)

account = Account("Hakan Akıncı",21410051038,1000)

account.hesapBilgileri()
account.parCek(800)
account.hesapBilgileri()
account.paraYatir(2000)
account.hesapBilgileri()