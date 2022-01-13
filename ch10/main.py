import requests
from bs4 import BeautifulSoup

def main():
    # url = "http://logs.eolem.com/"
    # r = requests.get(url)
    # print(r.text)

    with open('./ch10/index.html') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            print(link)

if __name__ == '__main__':
    main()