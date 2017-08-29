---
title: Statstidende
description: så du kan programmere for din arbejdsgiver
layout: default
---

# HOW TO GET STATSTIDENDE PÅ DANSK

Statstidende har et REST interface, som kan aflevere filer i XML eller JSON format, men som med alt andet offentlig IT er det noget lort. Derfor dropper vi at bruge den, og scraper i stedet deres hjemmeside. Til det skal vi bruge to pakker som kan interagerer med hjemmesider, nemlig `beautifulSoup4` og `requests`

```
pip install bs4
pip install requests
```

Begynd med at importere de nye pakker

```python
import bs4 as bs
import requests
```

## At bygge en scraper

Statstidendes hjemmeside er bygget af lort, så den er lidt bakset at navigere rundt på. Det betyder også at de URL'er der leder hen til vores data har en latterligt uintuitiv struktur - anyways vi begynder med at lave en funktion der kan generere sånogen URL'er:

``` python
def link_list(date, n = 10, lookup = 'proklama'):
    # lollern converter fordi statstidende henviser til forskellige kategorier med et skod talsystem i stedet for noget der giver mening
    converter = {
    'proklama': '36.1.3.791106',
    'arveproklama': '36.1.3.791215',
    'proklama (færøerne og grønland)': '36.1.3.9634921',
    'proklama (gl. udg.)': '36.1.3.2190916',
    'indkaldelse til bomøde': '36.1.3.791171',
    'andre meddelelser': '36.1.3.2190845'
    }
    link_list = []

    # Formatter vores link sådan at lårtet funker og returner det
    for i in range(1,n + 1):
        link_list.append('https://www.statstidende.dk/default.aspx?pg={}&date={}&mode=1&page={}#pnlAnnouncementStart'.format(converter[lookup], date, i))

    return link_list
```
Hvad gør den funktion? jo den returnerer en list på _n_ links, som leder til side _1,2,3,...n_ af dødsbosopslag på statstidendes hjemmeside. Med den i vinkel kan vi lave en funktion der downloader og behandler en enkelt html, og producerer et læsbart resultat med cpr-nummer etc.

```python
def scrape_page(link):
    html = requests.get(link)
    content_soup = bs.BeautifulSoup(html.text, 'html.parser').find(id = 'ctl00_plhMain_ctl00_tblAnnouncements')
    raw = content_soup.find_all('td', {'class': 'content_text'})

    page = {}

    for person in raw:
        outperson = {}
        person_list = person.find_all('span')[0].contents

        outperson['cpr'] = person_list[2]
        outperson['DOD'] = person_list[6]
        outperson['name'] = person_list[8]
        outperson['addr'] = person_list[10]
        outperson['city'] = person_list[12]

        page[person_list[2]] = outperson

    return page
```
Til sidst skal vi bare bruge en funktion der kan køre `scrape_page` på alle de links `link_list` har lavet:

```python
def scrape_multiple(link_list):
    out = {}
    for i in range(0,len(link_list)):
        out['page ' + str(i+1)] = scrape_page(link_list[i])

    return out
```
Nu kan vi downloade data fra statstidende på en given dato ved fx at køre

```python
scrape_multiple(link_list(date = '29.08.2017', n = 5))
```
