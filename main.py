from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup


# metodo que consulta a url de busca e envia um post para o field de name 'search' com as informações passadas
# no atributo 'query

def get_pagina(query):
    data = requests.post('https://wiki.archlinux.org/', data={'search': query})
    return data


# metodo main para start da aplicação

if __name__ == '__main__':

    # variavel que armazena a query informada na CLI com a ajuda da lib argparse

    parser = ArgumentParser()
    parser.add_argument('query', help='Informe a query desejada')

    arg = parser.parse_args()

    # variavel que instancia a lib BeautifulSoup e armazena os dados da requisição feita no metodo get_pagina

    html_soup = BeautifulSoup(get_pagina(arg.query).text, 'html.parser')

    # condicional que valida se há dados na consulta, retorna uma mensagem padrão em caso negativo e, em caso positivo
    # retorna os dados em texto plano

    if html_soup.findAll('p', {'class': 'mw-search-nonefound'}):
        print('Dados não encontrados')
    else:
        site_container = html_soup.find_all(id='content')
        for t in site_container:
            print(t.text)
