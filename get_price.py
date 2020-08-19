"""
this file contain a function which fetch all prices from www.tgju.org and return it as a string

"""

import bs4
import requests

url = "https://www.tgju.org/"

titles = ["بورس", "انس طلا", "مثقال طلا", "طلا 18", "سکه", "دلار", "یورو", "نفت برنت", "بیت کوین"]


def get_price():
    result = []  # all prices will save in this list after each function call
    try:
        res = requests.get(url)
    except Exception as e:
        print(f"Error :\n{e}")
    else:
        soup = bs4.BeautifulSoup(res.content, "html5lib")
        table = soup.select(".info-bar.mobile-hide")[0]  # first table at top of the site
        prices = table.select(".info-value")  # get all boxes from table(gold, dollar etc)
        changes = table.select(".info-change")
        for title, price, change in zip(titles, prices, changes):
            c_price = price.select(".info-price")[0].text  # current price
            c_change = change.text  # change rate
            result.append(f" {title}: {c_price}\nمیزان تغییر از اول امروز: {c_change}\n\n")
    return "".join(result)  # result as a string


if __name__ == "__main__":
    print(get_price())
