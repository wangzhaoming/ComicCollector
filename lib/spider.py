import requests

def get(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.text

def getJson(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.json()

if __name__ == '__main__':
    print(get('https://manhua.163.com/source/4724499322570095355'))
