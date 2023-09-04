# 1-100 e kadar

x = 1

while x < 100:
    if (x % 2 == 0):
        print(f"sayı çift: {x}")
    else:
        print(f"sayı tek: {x}")
    x += 1

print('bitti...')



print()
name = '' # False
while  not name.strip():    #not name.strip():
    name = input('isminizi giriniz: ')

print(f'Merhaba, {name}')