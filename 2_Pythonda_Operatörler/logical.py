x = 5

hak = 0
devam = 'e'

result = 5 < x < 10


# and
# Python and operatörü ile belirtilen koşulların hepsi doğru ise True, en az bir tanesinin yanlış olduğu durumda ise False değer üretir.
# iki koşuluda sağlaması gerekiyor

# True, True => True
# True, False => False


result = (x > 5) and (x < 10)  
result = (hak > 0) and (devam == 'e') 



# or
# Python or operatörü ile belirtilen koşulların sadece birinin doğru olması sonucun True olması için yeterlidir. 
# Hepsi yanlış ise sonuç da False olur.
# Tek koşulu sağlaması yeterli

result = (x > 0) or (x % 2 == 0)

# True, False => True
# True, True => True
# False, False => False



# not
# Python not operatörü ile koşulların tersi alınır. Örneğin bir koşul False üretiyorsa not operatörü ile True bilgisine çevrilir.

result = not(x > 0)

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2==0)

print(result)