# Yöntem 1
# import math
# import math as islem

# value = dir(math)     # -- math modülü içindeki bütün bileşenleri gösterir
# value = help(math)    # -- math modülü içindeki bileşenlerin kullanımını gösterir.
# value = help(math.factorial)    # -- sadece fonksiyonun kütüphanesini çalıştırdık

# value = math.sqrt(49)  # karekök alır
# value = math.factorial(5)  # faktoriyel hesaplar
# value = math.floor(5.9)   # aşağa yuvarlar
# value = math.ceil(5.9)  # yukarı yuvarlar 

# value = islem.factorial(6)


# Yöntem 2
# from math import *  # bütün kütüphaneleri import et

def sqrt(x):
    print("x: " + str(x))

from math import factorial, sqrt, ceil

# value = factorial(5)
value = sqrt(81)
# value = ceil(8.7)











print(value)