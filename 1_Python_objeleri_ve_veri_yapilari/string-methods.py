message = "Hello There. My name is Hakan Akıncı"

# message = message.upper()       # => upper metodu, karakterleri büyük harfe çevirir.

# message = message.lower()       # => lower metodu, karakterleri küçük harfe çevirir.

# message = message.title()       # =>  title methodu, karakter dizisindeki her kelimenin baş harfini büyük harfe çevirir.

# message = message.capitalize()    # => capitalize methodu, karakter dizisindeki sadece ilk kelimenin baş harfini büyük harfe çevirir.

# message = message.strip()      # => strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler.   

# message = message.split()       # => split metodu, karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar. 

# message= '---'.join(message)     # => join metodu, parça parça olan bilgileri birleştiricek ve aralara çizgi koyucak

# index = message.find('Sadık')      # => Find metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa exception döndürür.

# isFound = message.startswith('H')     # "H" harfi ile mi başlıyor bu kelime

# isFound = message.endswith('n')        # "n" karekteri ile mi bitiyor

# message = message.replace('Sadık','Çınar')   # => "Hakan" yerine "Akıncı" yazar güncelleme yapar
# message = message.replace('ç','c').replace('ö','o').replace(' ','-')  # güncelleme yapar

#message = message.center(100)     # => 100 adım boşluk bırakır
message = message.center(50,"*")   # başına ve sonuna 50 yıldız ekledi

print(message)
# print(isFound)