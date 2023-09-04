
try:
    a = 5
    b = 4
    c = a / b
    x = 4
    d = x
    isim = "Ali"
    karekter = isim[2]

except ZeroDivisionError:
    print("Payda sıfır olmamalı.")
except NameError:
    print("Bu değişken daha önce tanımlanmamış.")
except IndexError:
    print("Böyle bir index bulunmuyor.")
except Exception:
    print("Bilinmeyen bir hata oluştu.")

else:
    print("Else bloğu çalışıyor.")
    print(c)
    print(karekter)
finally:
    print("finally bloğu çalışıyor.")