import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
import time

EMAIL ="Gray24.Bulby37@gmail.com"
PASSWORD= "S3V4fZ(Tfo"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
AMAZON_URL = "https://www.amazon.com/adidas-Grand-Court-Sneaker-Active/dp/B07S72PWNN/ref=pd_di_sccai_1?pd_rd_w=xRzML&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=T5FS91SCY3Q37SDCZ393&pd_rd_r=d145c138-bff2-4572-889a-db1294419038&pd_rd_wg=nSMG7&pd_rd_i=B07KTWQ5MG&th=1&psc=1"
while True:
    response=requests.get(AMAZON_URL, headers={"User-Agent":USER_AGENT, "Accept-Language":ACCEPT_LANGUAGE})
    amazon_site = response.text
    soup= BeautifulSoup(amazon_site, 'lxml')
    priceline= soup.find(name='span', id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
    split_price = priceline.getText().split("$")
    price = split_price[1]

    if 50.00 >= float(price):

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="jrlewis84@gmail.com",
                                msg=f"Shoes on sale\n\nThe Grand Court shoes in the gray colorway are {price}. {AMAZON_URL}")
    time.sleep(21600)