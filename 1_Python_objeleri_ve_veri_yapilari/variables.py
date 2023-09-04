"""
- Değişken adı bir harf veya alt çizgi karakteri ile başlamalıdır.
- Bir değişken adı bir sayı ile başlayamaz
- Değişken adı yalnızca alfasayısal karakterler ve alt çizgiler (Az, 0-9 ve _ ) içerebilir
- Değişken adları büyük/küçük harfe duyarlıdır (yaş, Yaş ve YAŞ üç farklı değişkendir)
- Bir değişken adı, Python anahtar sözcüklerinden herhangi biri olamaz .
"""
maasAli = 5000
maasAhmet = 3000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))


# Değişken Tanımlama Kuralları

# 1) Rakam ile başlayamaz

# 2myvar => hatalı
# my-var => hatalı
# my var => hatalı
# 1yas => hatalı
# yas1 => geçerli
# _yas => geçerli

number1 = 10
print(number1)

number1 = 20        # number1 içinde bulunan 10 değeri silinir ve 20 değeri aktarılır.
print(number1)

number1 += 30       # number1 değişkeni üzerine 30 değerini eklemiş oluruz ve 50 olur.
print(number1)


print()
# 2) Büyük küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)


print()
# 3) Türkçe karekter kullanmayalım

yas = 30
_age = 50

x = 1               # int
y = 2.3             # float
name = "Çınar"      # string
isStudent = True    # bool

# x, y, name, isStudent = 1, 2, "Çınar", True  # Tek satırda da tanımlana bilir

a = 10
b = 50
print(a+b)   # a+b=60   toplar

c = "40"
d = "60"
print(c+d)   # c+d=4060  string olduğu için yan yana yazar

firstName = "Hakan"
lastName = " Akıncı"

print(firstName + lastName)
