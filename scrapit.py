import requests
from bs4 import BeautifulSoup


# noinspection SpellCheckingInspection
html_main = requests.get(
	'https://www.otodom.pl/wynajem/mieszkanie/warszawa/?search%5Bfilter_'
	'float_price%3Ato%5D=1750&search%5Bcity_id%5D=26&page=2')
bs_html = BeautifulSoup(html_main.content, 'html.parser')
# raw_content = bs.find_all('div', class_="listing")
offers = bs_html.find_all('div', class_="offer-item-details")


def list_offers(res_set):
	"""
	Scraps relevant data and order in list of offers
	:type
	:param res_set: ResultSet
	:return: ResultSet
	"""

	i = 1
	for offer in res_set:

		link = offer.find('a')['href']
		print("link:", link, end='\n')

		item_title = offer.find('span', class_="offer-item-title")
		print(f" {i}. OFFER:", f'"{item_title.text}"', sep='\n')
		# description = offer.find('span', class_="hidden-xs")
		description = offer.find('p', class_="text-nowrap")
		print("Short info:", description.text)
		params = offer.find('ul', class_="params")
		# for attr in params:
		#     print("attr:", attr)
		rooms = params.find('li', class_="offer-item-rooms hidden-xs")
		price = params.find('li', class_="offer-item-price")
		# prices = list(price.stripped_strings)
		# prize = "\n\n".join(prices) if prices else ""
		print("rooms:", rooms.text)
		# print("price:", prize, price, prices)
		# price2 = pri
		print("price:", price.text.replace(" ", "").replace("\n", ""))
		print("price:", next(price.stripped_strings).replace(" ", ""))

		size = offer.find('strong', class_="visible-xs-block")
		print("size:", size.text)
		i += 1


def paginate(parsed_soup):
	"""
	Returns dictionary for pagination mapping
	May be rewritten for a generator to invoke pagination by next() method
	"""

	pages = parsed_soup.find('ul', class_="pager")

	current_page = pages.find('a', attrs={"class": "active"})['href']
	prev_page = pages.find('a', attrs={"data-dir": "previous"})['href']
	next_page = pages.find('a', attrs={"data-dir": "next"})['href']

	return {"current": current_page, "previous": prev_page, "next": next_page}


# print(paginate(bs_html)['current'])

print(list_offers(offers))
