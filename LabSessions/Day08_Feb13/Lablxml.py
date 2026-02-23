from bs4 import BeautifulSoup
import requests

html_doc1 = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
"""
#parse HTML string
soup = BeautifulSoup(html_doc1, features="html.parser")
#title
print(soup.title.text)
#h1 text
print(soup.h1.text)
#paragraph text
print(soup.find("p"))

html_doc2 = """
<html>
  <body>
    <a href="http://books.toscrape.com">Click Here</a>
  </body>
</html>
"""
soup = BeautifulSoup(html_doc2, "html.parser")

#link
link = soup.find("a")
print(link.get("href"))

#find <a> tag
print(soup.find_all("a"))

#use prettify
print(soup.prettify())

#2.Scrap product details
url = "http://books.toscrape.com"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find  products
products = soup.find_all("article", class_="product_pod")
for product in products:
    # Product Name
    name = product.find("h3").find("a")["title"]
    # Price
    price = product.find("p", class_="price_color").text
    # Rating
    rating = product.find("p", class_="star-rating")["class"][1]
    # Availability
    availability = product.find_next("p", class_="instock availability")
    if availability:
        availability = availability.text.strip()
    # Image URL
    image = product.find("img")["src"]
    image_url = "http://books.toscrape.com/" + image

    print("Product Name:", name)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)
    print("Image URL:", image_url)
    print("-" * 40)
