# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# **************************
# "w": (Write) yazma modu. Dosyayı konumda oluşturur. 
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
# ***************************


# 1)
# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 

# file = open("newfile.txt","w")
# file = open("C:/users/Hakan Akıncı/deskop/newfile.txt","w")
# file.close()   # bu işlem açtığın dosyayı kapatır

# file = open("newfile.txt","w",encoding="utf-8")    // txt'in içine yazı yazır
# file.write("Hakan Akıncı")
# file.close()


# 2)
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nEvren Akıncı")
# file.write("Evren Akıncı\n")
# file.close()


# 3)
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding='utf-8')


# 4)
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
