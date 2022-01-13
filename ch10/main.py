import requests
from bs4 import BeautifulSoup

def main():
    # url = "http://logs.eolem.com/"
    # r = requests.get(url)
    # print(r.text)

    with open('index.html') as f:
        html = f.read()

if __name__ == '__main__':
    main()