import requests
from bs4 import BeautifulSoup

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    }

inp = input()
def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q
    r = s.get(url, headers=headers_Get)
    soup = BeautifulSoup(r.text, "html.parser")
    output = []
    for search in soup.find_all('div', {'class':'r'}):
        url = search.find('a')["href"]
        result = url
        output.append(result)
    if len(output) < 10:
        url + '&start=10'
        for search in soup.find_all('div', {'class': 'r'}):
            while len(output) < 10:
                url = search.find('a')["href"]
                result = url
                output.append(result)
        return output
    else:
        return output


print(len(google(inp)))