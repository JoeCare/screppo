from bs4 import BeautifulSoup
import requests
import bs4

# html_text = requests.get('https://www.praca.pl/s-python,developer.html?p=python+developer')
# print(html_text, type(html_text), type(html_text.text))
# print(html_text.text)
#
# soup = BeautifulSoup(html_text.text, 'lxml')
# site_buttons_jobs = soup.find_all('button', class_="listing__offer-title job-id listing__region-toggler")
#
# for n, col in enumerate(site_buttons_jobs):
#     print(n + 1, " of ", len(site_buttons_jobs), "columns on site. Example:\n", col.text)

html_dom = requests.get('https://www.otodom.pl/wynajem/mieszkanie/warszawa/?search%5Bfilter_float_price%3Ato%5D=1750&search%5Bcity_id%5D=26&page=2')
print(html_dom.text)
bs = BeautifulSoup(html_dom.content, 'html.parser')
print(bs)
offers = bs.find_all('div', class_="offer-item-details")
listing = bs.find_all('div', class_="listing")
pagination = bs.find_all('ul', class_="pager")
# with open('site.txt', 'w+') as site:
#     site.write(bs.text)
# for offer in offers:
#     # offer = offer.prettify()
#     print("\n!!!!!NEW!!!!!!:")
#     link = offer.find('a')
#     print("link:", link['href'])  # ['href'])
#     size = offer.find('strong', class_="visible-xs-block")
#     print("size:", size.text)
#     item_title = offer.find('span', class_="offer-item-title")
#     print("item:", item_title.text)

    # next_page = offer.find('form', id="pagerForm")
    # print(next_page.parent())
    # next_page = offer.find('a')
    # print("next page:", next_page['href'])



for l in listing:
    offers = l.find_all('div', class_="offer-item-details")
    pagination = bs.find_all('ul', class_="pager")
    for offer in offers:
        # offer = offer.prettify()
        print("\n!!!!!NEW!!!!!!:")
        link = offer.find('a')['href']
        print("link:", link)  # ['href'])
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
        print("price:", price.text.replace(" ","").replace("\n",""))
        print("price:", next(price.stripped_strings).replace(" ",""))

    for page in pagination:
        # current = page.find('li', class_="page-counter")
        # print("current:", current, pagination)
        print(page.find_all('li'))

    for page in pagination:
        # print("p", page)
        for p in page:
            print(p)
        # print("!!!!!!!!!!!!!!!!", p.find('li', class_="pager-prev").a['href'])
        # print("!!!!!!!!!!!!!!!!active?", p.find('li').a['href'])
        # print("!!!!!!!!!!!!!!!!active?", p.find('li').a['href'])
        # print("!!!!!!!!!!!!!!!!", p.find('li', class_="pager-next").a['href'])
# for item in listing:
#     print(item)