import requests
from lxml import html

url = "https://news.ycombinator.com"
response = requests.get(url)
data = html.fromstring(response.content)
title = data.find(".//title").text
print(title)

#links
links = data.xpath(".//a/@href")
print(links)

#links + url
links = data.xpath(".//a")
for link in links:
    print(link.text)
    print(link.get("href"))