# with open("newfile.txt","r+", encoding="utf-8") as file:   // r+ hem okuma hem yazma modu
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

# ***** Sayfa sonunda güncelleme *****

# with open("newfile.txt","a", encoding="utf-8") as file:   // a dosya açma modu
#     file.write("\nEmel Turan")

# ***** Sayfa başında güncelleme *****

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Turan\n" + content
#     file.seek(0)
#     file.write(content)



# ***** Sayfa ortasında güncelleme *****

with open("newfile.txt","r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())