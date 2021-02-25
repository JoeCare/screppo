# from bs4 import BeautifulSoup
#
# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     print("!!!!!!!RAW CODE!!\nPrint content: ", content)
#
#     soup = BeautifulSoup(content, 'lxml')
#     print("!!!!!!!PRETTYFIED WHOLE SITE CODE\nPrint content BS4 prettyfied with 'lxml'", soup.prettify())
#
#     site_columns = soup.find_all('div', class_='column')
#     site_cards = soup.find_all('div', class_='card')
#
#     for n, col in enumerate(site_columns):
#         print(n+1," of ", len(site_columns), "columns on site. Example:\n", col)
#
#     for n, card in enumerate(site_cards):
#         print(n+1, " of ", len(site_cards), "cards on site. divs only Example:\n", card.div)
#
#     for n, card in enumerate(site_cards):
#         print(n+1, " of ", len(site_cards), "cards on site. divs text only Example:\n", card.div.text)
#
#

import requests
from bs4 import BeautifulSoup
from typing import (TypedDict, Literal, Pattern, Match, NamedTuple, Union,
                    List, Callable, Sequence)


# class Apartment(NamedTuple):
#     price: str
#     offer: NamedTuple('offer', [price, rooms])
#     rooms: int

fo, ta, fl, ti = '1', '2' , 4 , 6
offer = NamedTuple('offer', [(fo, ta), (fl, ti)])
# >>>TypeError: NamedTuple('Name', [(f0, t0), (f1, t1), ...]);
# each t must be a type Got 110.

print(offer)
