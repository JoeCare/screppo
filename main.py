# This is a sample Python script.
from typing import Any

from bs4 import BeautifulSoup


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def run_task(func):
#     # Use a breakpoint in the code line below to debug your script.
#     func()
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# class Scrappon():
#
#     # Class Const's
#     def __init__(self):
#         self.file_name = 'home.html'
#         self.mode = 'r'
#
#     def local_html(self, file_name='home.html', mode='r') -> Any:
#         # with open('home.html', 'r') as html_file:
#         with open(self.file_name, self.mode) as html_file:
#             content = html_file.read()
#             print(content)


def run_task():

    with open('home.html', 'r') as html_file:
        content = html_file.read()
        print("!!!!!!!RAW CODE!!\nPrint content: ", content)

        soup = BeautifulSoup(content, 'lxml')
        print("!!!!!!!PRETTYFIED WHOLE SITE CODE\nPrint content BS4 prettyfied with 'lxml'", soup.prettify())

        tags = soup.find_all('div')
        print("!!!!!!!UNPRETTYFIED DIVS DIVISION\nPrint all divs: " + str(tags))
        for column in tags:
            print(column.text)


        tags_1 = soup.find_all('p')
        for paragraph in tags_1:
            print("!!!!!!!\nPrint paragraphs text only: ", paragraph.text)

        content_columns = soup.find_all('div', class_="column")
        for column in content_columns:
            print("by CONTENT COLUMNS classes print with tags", "'column':\n'", column, "\n'")

        content_columns_1 = soup.find_all('div', class_="column")
        for column in content_columns_1:
            print("from all class=column divs print just text:\n from divs of class column print column.h3"
                  " to divs which ar not divs but h3 test header tag:\n",
                  column.h3, "\nfrom divs of class column print column.h3 "
                             "to divs which ar not divs but h3 test header tag text only:\n",
                  column.h3, "\nor column.h2:\n", column.h2, "or h4:\n",
                  column.h4, "\nor h4 type:\n", type(column.h4),
                  "\nor a (href):\n", column.a)



    print("Done")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # lets_scrap = Scrappon.local_html(self)
    # run_task(lets_scrap)
    run_task()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
