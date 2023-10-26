from yandex_geocoder import Client
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

def main():
    headers = requests.utils.default_headers()

    client = Client("603aef28-cf3e-45ff-9f66-042f6159441d")
    a, b = map(float, input('введите долготу и широту:\n').split(', '))
    # 131.887845, 43.026438
    a, b = b, a
    ad = client.address(Decimal(a), Decimal(b))
    print(ad)
    place = ad
    headers.update({
        'User-Agent': 'My User Agent 1.0',
    })

    adr = requests.post(f'https://egrnrstr.ru/search?query={place}', headers=headers)
    soup = BeautifulSoup(adr.json()["data"], "html.parser")
    a = soup.select("div.results__text")
    all_dat = []
    dta = []
    for i in a:
        i1 = i["title"]
        dta.append(i1)
        req = requests.post(f"https://egrp365.org/reestr?egrp={i1}", headers=headers)
        f = req.text
        strt = f.find("<!--sse-->")
        end = f.find("<!--/sse-->")
        if strt != -1:
            k = f[strt + 10:end]
            nchk = ncht = False
            ans = ''
            for i in k:
                if not ncht and not nchk:
                    if i == "(":
                        nchk = True
                    elif i == '<':
                        ncht = True
                    else:
                        ans += i
                elif nchk:
                    if i == ")":
                        nchk = False
                    elif i == '<':
                        ncht = True
                elif ncht:
                    if i == "(":
                        nchk = True
                    elif i == '>':
                        ncht = False
                else:
                    if i == ")":
                        nchk = False
                    elif i == '>':
                        ncht = False
            all_dat.append(ans)
    # край Приморский, г. Владивосток, ул. Радужная, дом 20
    print(*all_dat, sep="\n------------------------------------")


if __name__ == '__main__' or __name__ == 'parse':
    main()
