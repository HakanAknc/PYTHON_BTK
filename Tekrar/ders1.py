# open()  = dosyayı açmak için kullanılır
# w = dosya oluşturmak ve yazdrırmak için kullanılır
# a = dosya oluşturma ve yazdrımak için kullanılır  = aralarındaki fark yukardaki yeniden yazar altaki üstüne yazar
# r = dosyayı okumamızı sağlar
 

# file = open("hakan.txt","a")

# file.write("Naber Python\n")
# file.write("Naber Java\n")
# file.write("Naber C#")

# file.close()

file = open("hakan.txt","r")

for oku in file:
    print(oku)

file.close()