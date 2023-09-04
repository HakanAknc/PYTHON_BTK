from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime  # modül içindeki bütün classları import eder.

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()  # saat ve tarih bilgisini verir
result = datetime.now().month  # ayı gösterir
result = datetime.now().year  # yılı gösterir
result = simdi.day
result = simdi.hour  # saati gösyerir
result = simdi.minute  # dk gösterir
result = simdi.second  # sn gösterir

result = datetime.ctime(simdi)  # daha açıklayıcı bir tarih verir
result = datetime.strftime(simdi,'%Y')  # sadece yıl bigisini verir
result = datetime.strftime(simdi,'%X')  # sadece saat bigisini verir
result = datetime.strftime(simdi, "%d")  # sadece gün bigisini verir
result = datetime.strftime(simdi, "%A")  # gün bigisini string olarak verir
result = datetime.strftime(simdi,'%B')  # ay bigisini string olarak verir
result = datetime.strftime(simdi,'%Y %B %A')  # birden fazla kullanılabilir

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0)  # bilgisiyarlar için kullanılan milat bilgisi 

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days = 10)

print(result)