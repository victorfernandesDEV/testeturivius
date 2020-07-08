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


