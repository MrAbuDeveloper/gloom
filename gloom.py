from bs4 import BeautifulSoup
import requests


class OpenShopParser:
    def __init__(self, category):
        if category == 'phones' or category == '-C7V2C':
            self.URL = 'https://openshop.uz/shop/subcategory/'
        elif category == 'appliances':
            self.URL = 'https://openshop.uz/shop/category/'
        else:
            self.URL = 'https://openshop.uz/shop/subsubcategory/'
        self.category = category
        self.HEADERS = {
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }

    def get_soup(self):
        response = requests.get(self.URL + self.category, headers=self.HEADERS).text
        soup = BeautifulSoup(response, 'html.parser')
        return soup

    def get_info(self):
        try:
            data = []
            soup = self.get_soup()
            box = soup.find('div', class_='product-wrapper row cols-lg-4 cols-md-3 cols-sm-2 cols-2')
            products = box.find_all('div', class_='product-wrap')
            for product in products:
                title = product.find('h3').get_text(strip=True)
                link = product.find('a')['href']
                price = product.find('ins').get_text(strip=True)
                image = product.find('img')['src']

                data.append({
                    'title': title,
                    'link': link,
                    'price': price,
                    'image': image
                })
            return data
        except Exception as e:
            print(e)
            print('Error 404')
