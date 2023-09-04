"""
`Global ve yerel terimleri, bir komut dosyası veya program içindeki bir değişkenin erişimine karşılık gelir.
Global bir değişken, herhangi bir yerden erişilebilen bir değişkendir.

Yerel bir değişkene yalnızca çerçevesi içinde erişilebilir. Yerel bir değişkene global olarak erişilemez.
Global değişkenler, bir fonksiyonun dışında tanımlanan ve bildirilen ve herhangi bir yerde kullanılabilen değişkenlerdir.
Bir fonksiyon kapsamında aynı isimde bir değişken tanımlanırsa, global değeri değil, sadece fonksiyon içinde verilen değeri yazdırır.
Verilen kod, yazdir() fonksiyonunun hem içinde hem de dışında global değişkene nasıl erişildiğini göstermek için yeniden yazılmıştır.

Örnek:
Python
 
# k değişkeni global olarak oluşturuldu.
k = "Python Örnekleri"
def yazdir():
    print(k) #Global değişkene fonksiyon içinden erişildi.
yazdir()
print(k) #Global değişkene fonksiyon dışından erişildi.
"""

# global scope
x = 'global x'

def function(): 
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)

####################

# global
name = 'Çınar'

def changeName(new_name):
    # local 
    global name
    name = new_name
    print(name)

changeName('Ada')
print(name)

####################

name = 'global string'

def greeting():
    # name = 'Çınar'

    def hello():
        # name = 'Ada'
        print('hello '+ name)

    hello()

greeting()

####################

x = 50
def test(): 
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)