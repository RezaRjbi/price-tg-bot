"""
this file contain a function which fetch all prices from www.tgju.org and return it as a string

"""

import bs4
import requests

url = "https://www.tgju.org/"


def get_price():
    result = []  # all prices will save in this list after each function call
    try:
        res = requests.get(url)
    except Exception as e:
        print(f"Error :\n{e}")
    else:
        soup = bs4.BeautifulSoup(res.content, "html5lib")
        table = soup.select(".info-bar.mobile-hide")[0]  # first table at top of the site
        prices = table.select(".high")  # get all boxes from table(gold, dollar etc)

        for price in prices:
            title = price.select("h3")[0].text
            c_price = price.select(".info-price")[0].text  # current price
            change = price.select(".info-change")[0].text  # change rate
            result.append(f" {title}: {c_price}\nمیزان تغییر از اول امروز: {change}\n\n")
    return "".join(result)  # result as a string
