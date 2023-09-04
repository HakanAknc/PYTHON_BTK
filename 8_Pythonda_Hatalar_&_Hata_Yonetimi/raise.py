# x = 10

# if x > 10:
#     raise Exception("x 5'den büyük değer alamaz.")


# fonksiyon
# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parolanız en az 7 karekter oluşmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parolanız küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("parola alpha numeric karakter içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("parola boşluk içermemelidir.")
#     else:
#         print("Geçerli parola")

# password = "1234567aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli parola : else")
# finally:
#     print("validation tamamlandı")




#class
class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiii", 1989)
