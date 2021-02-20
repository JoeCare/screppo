from bs4 import BeautifulSoup


with open('home.html', 'r') as html_file:
    content = html_file.read()
    print("!!!!!!!RAW CODE!!\nPrint content: ", content)

    soup = BeautifulSoup(content, 'lxml')
    print("!!!!!!!PRETTYFIED WHOLE SITE CODE\nPrint content BS4 prettyfied with 'lxml'", soup.prettify())

    site_columns = soup.find_all('div', class_='column')
    site_cards = soup.find_all('div', class_='card')

    for n, col in enumerate(site_columns):
        print(n+1," of ", len(site_columns), "columns on site. Example:\n", col)

    for n, card in enumerate(site_cards):
        print(n+1, " of ", len(site_cards), "cards on site. divs only Example:\n", card.div)
    for n, card in enumerate(site_cards):
        print(n+1, " of ", len(site_cards), "cards on site. divs text only Example:\n", card.div.text)
