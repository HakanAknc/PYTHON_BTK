"""
List: elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Tuple: elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Set: elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.

Dictionary: key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.

sum() = listedeki sayıların toplamını verir
"""

messagge = "Hello There. My name is Hakan Akıncı".split()
# print(messagge[0])

# my_list = [1,2,3]
# my_list = ["bir",2,True,5.6]
# print(my_list)

list1 = ["one","two","there"]
list2 = ["four","five","six"]

numbers = list1 + list2
print(numbers)
print(len(numbers))   #elemean sayısını verir

print(messagge[0])
print(messagge[2])

userA = ["Hakan", 21]
userB = ["Evren", 4]

users = [userA , userB]

print(userA)
print(userB)
print(users)

print(users[1][0])