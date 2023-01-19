from bs4 import BeautifulSoup
import requests


class ApartmentSearch:
    def __init__(self):
        url = 'https://www.zillow.com/salt-lake-city-ut/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Salt%20Lake%20City%2C%20UT%22%2C%22mapBounds%22%3A%7B%22west%22%3A-112.28440711914062%2C%22east%22%3A-111.55656288085937%2C%22south%22%3A40.54434063573144%2C%22north%22%3A41.008153590775585%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6909%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22price%22%3A%7B%22max%22%3A564357%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2400%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/94.0.4606.71 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

        html_file = requests.get(url=url, headers=headers).text
        self.soup = BeautifulSoup(html_file, 'html.parser')

    def get_info(self):
        info = []
        property_cards = self.soup.select('.property-card')
        for card in property_cards:
            link = card.findChild(class_='property-card-link')['href']
            if 'zillow' not in link:
                link = 'https://www.zillow.com/b/argenta-san-francisco-ca-5Xj7m7/' + link

            data = {'price': card.findChild('span').text,
                    'link': link,
                    'address': card.findChild('address').text}
            info.append(data)
        return info
