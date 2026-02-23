from bs4 import BeautifulSoup
import requests
#1. Title and h1
html = '''
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
print(soup.h1.text)

#2.Extract All Paragraphs
print(soup.find_all("p"))

#3.Extract All Links and Count
url = "http://books.toscrape.com"
headers = {
    # user - agent - who is making the request and from where
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, features="html.parser")

links = soup.find_all("a")
print(links)
print("Count:", len(links))

#4. Extract Attributes
link = soup.find("a")
print(link.attrs)        # all attributes
print(link.get("href"))  # Specific attribute

#5.Extract First h2
print(soup.find("h2"))

#6.Extract Bold Text
print(soup.find_all("b"))

#7.Extract All href Values
for link in soup.find_all("a"):
    print(link.get("href"))

#8.Get All Text Without Tags
print(soup.get_text())

#9.Extract Title from Website
print(soup.title.text)

#10.Extract All Headings (h1–h6)
for heading in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
    print(heading.text)

#12.Extract Images
images = soup.find_all("img")
for i in images:
    print(i.get("src"))

#11.Extract Table Data
html = '''
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
<table>
<tr>
    <th>Name</th>
    <th>Age</th>
</tr>
<tr>
    <td>John</td>
    <td>25</td>
</tr>
<tr>
    <td>Mary</td>
    <td>30</td>
</tr>
</table>
</body>
</html>
'''
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")
for row in table.find_all("tr"):
    cols = row.find_all("td")
    for i in cols:
        print(i.text)
