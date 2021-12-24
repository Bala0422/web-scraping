from bs4 import BeautifulSoup

import urllib.request as ur
language_heading = ['C', 'C++', 'Java', 'Python', 'C#', 'Javascript']


def extract_code(text_container):
    ALL_text = text_container.find_all('div')
    for text in ALL_text:
        final_code = text.find_all('code')

        for item in final_code:
            print(item.text, end='')

        print()


link = input("Paste the link where you have to extract code from geeks for geeks  ")
with ur.urlopen(link) as url:
    content = url.read()
    soup = BeautifulSoup(content, 'lxml')
    Code_block = soup.find_all('div', class_="code-container")
    heading = soup.find_all('h2')
    final_heading_list = []
    for i in heading:
        if i.text in language_heading:
            final_heading_list.append(i.text)

    try:
        for i in range(len(Code_block)):
            text_container = Code_block[i].find('div', class_="container")
            print(final_heading_list[i] + '  CODE')
            extract_code(text_container)

            print('_________________________________________________________________________________')
            print()

    except IndexError:
        pass





