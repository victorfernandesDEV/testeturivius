from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup


def get_pagina(query):
    data = requests.post('https://wiki.archlinux.org/', data={'search': query})
    return data


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('query', help='Informe a query desejada')

    arg = parser.parse_args()

    html_soup = BeautifulSoup(get_pagina(arg.query).text, 'html.parser')

    if html_soup.findAll('p', {'class': 'mw-search-nonefound'}):
        print('Dados não encontrados')
    else:
        site_container = html_soup.find_all(id='content')
        for t in site_container:
            print(t.text)
