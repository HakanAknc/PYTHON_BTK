numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = max(numbers)        # => Bir liste içerisindeki minimum ve maksimum değeri ister sayısal ister alfabetik olarak alabiliriz.
val = min(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

print(val)


numbers[4] = 40

numbers.append(49)    # => Python listelerinin sonuna bir eleman eklemek için append() metodu kullanılır.
numbers.append(59)

numbers.insert(3,78)    # => Python listelerinde belirtilen bir indeks'e eleman eklemek için insert() metodu kullanılır.
numbers.insert(-1,52)


numbers.pop()            #  =>Python listelerinde belirtilen bir indeks' deki elemanı silmek için pop() metodu kullanılır. Eğer indeks numarası belirtmezsek listenin son elemanı silinir.
numbers.pop(0)
numbers.pop(-1)
numbers.remove(16)        #  => Listeden bir eleman silmek için remove() metodunu kullanabiliriz.

print(numbers)

liste = ["banana", "grape", "cherry"]   # => del() metodu ile her hangi bir indeks numarasındaki elemanı silebiliriz.
del liste[2]
print(liste) # ["banana", "grape"]


numbers.sort()         # => Liste elemanlarını sıralamak için sort() metodu kullanılır.
letters.sort()

numbers.reverse()      # => Liste elemanlarını reverse() metodu ile tersten yazdırabiliriz.
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))         # => Eleman sayısını verir
print(len(letters))


print(numbers.count(10))      #  => Bir liste içerisindeki tekrarlayan elemanların sayısını almak için count() metodunu kullanırız.
print(letters.count("a"))

numbers.clear()             # => Listeyi temizler
print(numbers)