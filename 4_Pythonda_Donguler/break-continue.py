name = "Hakan Akıncı"

# break
for val in name:
    if val == "k":
        break          # break komutu döngüyü sonlandırır
    print(val)

print("**********")

# continue
for val in name:
    if val == "a":  
        continue       # ontinue ise döngünün o turunu sonlandırır ve bir sonraki turdan devam eder.
    print(val)

print()

x = 0
#break
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

print()

y = 0
# continue
while y < 5:
    y += 1
    if (y == 3):
        continue
    print(y)

print()

# 1- 100 e kadar sayıların toplamı
x = 0
toplam = 0

while x <= 100:
    toplam += x
    x += 1
print(f"1-100 arası sayıların toplamı: {toplam}")


# 1- 100 e kadar tek sayıların toplamı

x = 0
toplam = 0

while x <= 100:
    x += 1
    if (x % 2 == 1):
        continue
    toplam += x

print(f"1-100 arası tek sayıların toplamı: {toplam}")


# 1- 100 e kadar çift sayıların toplamı

x = 0
toplam = 0

while x <= 100:
    x += 1
    if (x % 2 == 0):
        continue
    toplam += x

print(f"1-100 arası çift sayıların toplamı: {toplam}")
