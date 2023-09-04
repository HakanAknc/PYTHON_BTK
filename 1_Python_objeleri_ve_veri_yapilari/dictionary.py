
# key - value

# 41 => kocaeli 34 => istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34


plakalar = {"Antalya" : 7, "İstanbul" : 34}
print(plakalar)

print(plakalar["Antalya"])
print(plakalar["İstanbul"])


plakalar["Ankara"] = 6
plakalar['Antalya'] = 'new value'
print(plakalar)


users = {
    "hakanakinci": {
        'age': 21,        
        'roles': ['user'],
        'email': 'hakan@gmail.com',
        'address': 'antalya',
        'phone': '1231321'
    },
    "evrenakinci": {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'evren@gmail.com',
        'address': 'istanbul',
        'phone': '1231321'
    }
}

print(users['evrenakinci']['roles'][0])