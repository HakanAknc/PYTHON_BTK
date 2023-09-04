fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')    # => Set listesine tek bir eleman eklemek için add() metodunu,       
fruits.update(['mango','grape','apple'])    # => birden fazla eleman eklemek için ise update() metodunu kullanabiliriz.

fruits.remove('mango')     # => Set' den bir eleman silmek için remove() ya da discard() metodu kullanılabilir.
fruits.discard('apple')
fruits.pop()

fruits.clear()         # => clear() metodu ile set elemanlarının hepsini silebiliriz.

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))