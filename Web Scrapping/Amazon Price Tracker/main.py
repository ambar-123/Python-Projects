from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "YOUR_EMAIL_ID"
MY_PASSWORD = "YOUR_PASSWORD"

# Enter your desired product url
response = requests.get("https://www.amazon.in/Sony-HT-S500RF-Digital-Soundbar-Theatre/dp/B07G1QPS6H/ref=sr_1_6?crid"
                        "=1OGZC791MNFF3&dchild=1&keywords=home+theatre+5.1+surround+system&qid=1627543308&refinements"
                        "=p_36%3A1318507031&rnid=1318502031&s=electronics&sprefix=home+theat%2Caps%2C-1&sr=1-6",
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                               "like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                                 "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"})
response.raise_for_status()

data = response.text
soup = BeautifulSoup(data, "html.parser")

item_price = 0
price = soup.select(".priceBlockBuyingPriceString")
for item in price:
    item_price = item.getText()

price_value = float(item_price.split("₹")[1].replace(',', ''))

par_price = 32000.0     # Your desired Price
if price_value <= par_price:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Amazon Price Alert \n\n The Price of the Product has went down to ₹ {price_value}\n Book the item"
            f"now.".encode("utf8")
    )
