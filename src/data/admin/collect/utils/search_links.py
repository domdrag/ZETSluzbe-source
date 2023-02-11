import requests
from bs4 import BeautifulSoup, SoupStrainer

def searchLinks():
    workDayURL = ''
    saturdayURL = ''
    sundayURL = ''

    payload = {
        'pojam': 'zetovci'
    }

    with requests.Session() as s:
        p = s.post('https://www.zet.hr/interno/default.aspx?a=login',
                   data=payload)
        r = s.get('https://www.zet.hr/interno/default.aspx?id=1041')
        content = r.content

        for link in BeautifulSoup(content, parse_only=SoupStrainer('a')):
            if hasattr(link, "href"):
                link = link['href']
                if('RD' in link):
                    workDayURL = link
                if('SUB' in link):
                    saturdayURL = link
                if('NED' in link):
                    sundayURL = link

    return {'workDay': workDayURL,
            'saturday': saturdayURL,
            'sunday': sundayURL}
