# Liste ile Tuple tamammen aynı mantık sadace tuple atadığmız her hangi bir değeri başka bir değer ile değiştiremiyoruz
# Tek bir eleman üzerine değişiklik yapmamıza izin vermiyor tuple

list = [1, 2, 3]
tuple = (1, "iki", 3) 

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])


# print(len(list))
# print(len(tuple))


list = ['ali','veli']
tuple = ('damla','ayşe','ayşe')
names = ('demet','emel','ayşe') + tuple

print(names)

list[0] = 'ahmet'
# tuple[0] = 'deniz'   # hata alırsın

print(tuple.count('ayşe'))    # kaç kere ayşe var
print(tuple.index('ayşe'))    # index numarasını bulur

print(list)
print(tuple)