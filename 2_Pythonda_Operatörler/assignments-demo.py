x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
a = int(input("a: "))
b = int(input("b: "))

carp = a * b
print("Çarpım: ", carp)

toplam = x + y + z
print("Toplam: ", toplam)

fark = carp - toplam
print("Fark: " , fark)

"""
a = int(input('1.sayı: '))
b = int(input('2.sayı: '))

result = (a * b) - (x+y+z)
"""

# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
val = y // x
print(val)


# 3- (x,y,z) toplamının mod 3' ü nedir ?
val = (x+y+z) % 3
print(val)


# 4- y' nin x. kuvvetini hesaplayınız.
val = y ** x
print(val)


# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers = 1, 5, 7, 10, 6

x, *y, z = numbers          # x = 1, *y = 5,7,10, z = 6
result = z ** 3

print(result)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
numbers = 1, 5, 7, 10, 6

x, *y ,z = numbers
result = y[0] + y[1] + y[2]      # => 5 + 7 + 10 = 22

print(result)