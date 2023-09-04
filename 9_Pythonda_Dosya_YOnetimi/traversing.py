with open("newfile.txt","r",encoding="utf-8") as file:  # with dersen close demene gerek kalmaz
    content = file.read()
    print(content)
    print(file.tell())
    file.seek(0)
    print(file.tell())   # kürsünün konumunu verir
    content2 = file.read(10)
    print(content2)