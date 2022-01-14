import requests
from bs4 import BeautifulSoup
import glob 
from pprint import pprint
import re

# + => 1 -> n
# * => 0 -> n
# ? => 0 -> 1
# {3} => 3
# {3,5} => 3 -> 5

def main():
    logs = glob.glob("ch10/*.log")
    logs= sorted(logs)
    err = False
    for log_file in logs:
        with open(log_file) as f:
            for i,line in enumerate(f):
                # result = re.findall(r'((\d{1,3}\.){3}\d{1,3})',line.strip())
                # result = re.findall(r'(^.+?)\s',line.strip())
                result = re.findall(r'"\s(\d{3})',line.strip())
                if '404' in result:
                    print('erreur',log_file,i+1)

                if len(result) ==0:
                    err =True
                # print(result)
    
    print(err)
def main_1():
    # url = "http://logs.eolem.com/"
    # r = requests.get(url)
    # print(r.text)

    with open('./ch10/index.html') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
            print(link['href'])

if __name__ == '__main__':
    main()