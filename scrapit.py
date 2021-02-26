import requests
from bs4 import BeautifulSoup
import json

class Scrapper:
	pass


# noinspection SpellCheckingInspection
get_page = requests.get(
	"https://www.otodom.pl/wynajem/mieszkanie/warszawa/?search"
	"%5Bfilter_float_price%3Ato%5D=1750&search%5Bcity_id%5D=26&page=2")
bs_page = BeautifulSoup(get_page.content, 'html.parser')
offers = bs_page.find_all('div', class_="offer-item-details")


def list_offers(res_set):
	"""
	Scraps relevant data and order in list of offers
	:type
	:param res_set: ResultSet
	:return: ResultSet
	"""
	offers_mapper = {}

	next_example = 1
	for offer in res_set:
		offer_mapper = {}

		item_title = offer.find('span', class_="offer-item-title")
		description = offer.find('p', class_="text-nowrap")
		link = offer.find('a')['href']
		params = offer.find('ul', class_="params")

		rooms = params.find('li', class_="offer-item-rooms hidden-xs")
		price = params.find('li', class_="offer-item-price")
		area = params.find('li', class_="hidden-xs offer-item-area")

		print(f"\n{next_example}. OFFER:", description.text, sep='\n')
		print("subtitle:", item_title.text)
		print("link:", link, end='\n')
		print("price:", price.text.replace(" ", "").replace("\n", ""))
		print("price:", next(price.stripped_strings).replace(" ", ""))
		print("area:", area.text)
		print("rooms:", rooms.text)
		next_example += 1
		offer_mapper[item_title.text] = description.text
		print(json.dumps(offer_mapper, indent=2))
		print(offer_mapper)


def pagination_mapper(parsed_soup):
	"""
	Returns dictionary for pagination mapping
	May be rewritten for a generator to invoke pagination by next() method
	"""

	pages = parsed_soup.find('ul', class_="pager")

	# current_page = pages.find('a', attrs={"class": "active"})['href']
	prev_page = pages.find('a', attrs={"data-dir": "previous"})['href']
	next_page = pages.find('a', attrs={"data-dir": "next"})['href']

	return {
		"current": pages.find('a', attrs={"class": "active"})['href'],
		"previous": prev_page,
		"next": next_page
		}


print(pagination_mapper(bs_page))  # ['current'],
# paginate(
# bs_page)[
# 'previous'])

print(list_offers(offers))
