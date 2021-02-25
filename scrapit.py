import requests
from bs4 import BeautifulSoup

# print("price:", next(price.stripped_strings).replace(" ", ""))

# noinspection SpellCheckingInspection
html_dom = requests.get(
	'https://www.otodom.pl/wynajem/mieszkanie/warszawa/?search%5Bfilter_'
	'float_price%3Ato%5D=1750&search%5Bcity_id%5D=26&page=2')
print(html_dom.text)
bs = BeautifulSoup(html_dom.content, 'html.parser')
print(bs)
offers = bs.find_all('div', class_="offer-item-details")
listing = bs.find_all('div', class_="listing")
pagination = bs.find('ul', class_="pager")

# def list_the_offer
for lis in listing:
	offers = lis.find_all('div', class_="offer-item-details")
	# pagination = bs.find('ul', class_="pager")
	for offer in offers:
		# offer = offer.prettify()
		print("\n!!!!!OFFER!!!!!!:")
		link = offer.find('a')['href']
		print("link:", link)  # ['href']
		size = offer.find('strong', class_="visible-xs-block")
		print("size:", size.text)
		item_title = offer.find('span', class_="offer-item-title")
		print("name:", item_title.text)
		# description = offer.find('span', class_="hidden-xs")
		description = offer.find('p', class_="text-nowrap")
		print("description:", description.text)
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


def change_page(parsed_soup):
	"""
	Returns dictionary for pagination mapping
	May be rewritten for a generator to invoke pagination by next() method
	"""

	pages = parsed_soup.find('ul', class_="pager")

	current_page = pages.find('a', attrs={"class": "active"})['href']
	prev_page = pages.find('a', attrs={"data-dir": "previous"})['href']
	next_page = pages.find('a', attrs={"data-dir": "next"})['href']

	return {"current": current_page, "previous": prev_page, "next": next_page}


print(change_page(bs))
