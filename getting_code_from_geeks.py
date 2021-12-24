# The following code can extract all the code in geeks for geeks website and store as respective files(eg:- Python CODE.py, C++ CODE.CPP)

from bs4 import BeautifulSoup

import urllib.request as ur
language_heading = ['C', 'C++', 'Java', 'Python', 'C#', 'Javascript']


def extract_code(text_container, file_name):
    ALL_text = text_container.find_all('div')
    save_type = ''
    if file_name == 'C':
        save_type = '.c'
    elif file_name == 'C++':
        save_type = '.CPP'
    elif file_name == 'C#':
        save_type = '.cs'
    elif file_name == 'Python':
        save_type = '.py'
    elif file_name == 'Java':
        save_type = '.java'
    elif file_name == 'Javascript':
        save_type = '.js'

    with open(f'codes/{file_name} CODE{save_type}', 'w') as f:
        for text in ALL_text:
            final_code = text.find_all('code')
            for item in final_code:
                if item.text.strip() == '':
                    for i in range(int(len(item.text)/4)):
                        f.write('\t')
                elif item.text.strip() == '=':
                    f.write(f'{item.text.strip()}')
                else:
                    f.write(f'{item.text.strip()} ')
            f.write('\n')


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

    print('Saving to file ....')
    try:
        for i in range(len(Code_block)):
            text_container = Code_block[i].find('div', class_="container")
            extract_code(text_container, final_heading_list[i])

    except IndexError:
        pass





