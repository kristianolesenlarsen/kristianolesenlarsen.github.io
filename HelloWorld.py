import bs4 as bs
import requests


def link_list(date, n = 10, lookup = 'proklama'):
    converter = {
    'proklama': '36.1.3.791106',
    'arveproklama': '36.1.3.791215',
    'proklama (færøerne og grønland)': '36.1.3.9634921',
    'proklama (gl. udg.)': '36.1.3.2190916',
    'indkaldelse til bomøde': '36.1.3.791171',
    'andre meddelelser': '36.1.3.2190845'
    }
    link_list = []
    for i in range(1,n +1):
        link_list.append('https://www.statstidende.dk/default.aspx?pg={}&date={}&mode=1&page={}#pnlAnnouncementStart'.format(converter[lookup], date, i))

    return link_list


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


def scrape_multiple(link_list):
    out = {}
    for i in range(0,len(link_list)):
        out['page ' + str(i+1)] = scrape_page(link_list[i])

    return out
