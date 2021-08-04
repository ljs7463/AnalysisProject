import time
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://events.interpark.com/exhibition?exhibitionCode=201215006')
page = browser.page_source
soup = BeautifulSoup(page, 'html.parser')

discounts = soup.find('div', attrs={'class':'inner'}).find_all('a')
for discount in discounts:
    print(discount.find('img').attrs['src'])
    print(discount['gtm-label'].split('>')[2])
    print(discount.find('div', attrs={'class':'contentWrap'}).find_all('li'))
    # string추출 작업 해야함.
    


