html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
<h1 id="header">
        Python Kursu
      </h1>

    <hr>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

     <div class="grup3">
        <h2>
            Djengo
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")  # analiz işlemi

result = soup.prettify() # karışık olarak verilen döküman düzeltilmiş olarak verilir
result = soup.title  # title'yi verir.
result = soup.head  # head verir
result = soup.body

result = soup.title.name  # title etiketinin ismi gelir
result = soup.title.string  # title içindeki stringi verir.

result = soup.h1  # h1 etiketini verir
result = soup.h2
result = soup.h2.name   # h2 etiketinin ismini verir
result = soup.h2.string   # h2 içindeki stringi verir.
result = soup.h1.string

result = soup.find_all("h2")  # sayfada bulduğu bütün h2 etiketini gösterir.
result = soup.find_all('h2')[0]  # 0. indexsi getirir
result = soup.find_all('h2')[1]  # 1. indexsi getirir

result = soup.div
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()  # div altındaki bütün alt etiketleri getirir

result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()    #next = bir sonraki  ,  previ = bir önceki

# print(result)

result = soup.find_all('a')

for link in result:
    print(link.get("href"))

# print(result)

