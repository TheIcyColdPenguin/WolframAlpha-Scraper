import requests
from bs4 import BeautifulSoup


def get_equation():
    eq = input('Enter an equation to calculate-')
    formatting_dict = {
        '^': '%5E', '+': '%2B', '(': '%2', ')': '%29', ' ': '+',
    }
    for i, v in formatting_dict.items():
        eq = eq.replace(i, v)
    return eq


def get_url(eq):
    return 0


def main():
    eq = get_equation()
    url = get_url(eq)


if __name__ == '__main__':
    main()
