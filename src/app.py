import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/black/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip()  # 129.00

price_without_symbol = string_price[1:]  # 129.00 grabbing everything from the start and end of the string

price = float(price_without_symbol)

if price < 200:
    print("Buy!")
    print("The current price is {}".format(string_price))
else:
    print("Don't buy.")




