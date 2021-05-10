'''
Scrap of VR
'''

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import datetime
import logging

# Log config
LOG_FORMAT = "%(asctime)-24s [%(filename)s:%(lineno)d] \
    %(levelname)-6s %(message)s"

logging.basicConfig(filename='logs/logs.log',
                    filemode='a',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)


class VR:
    """
    Class to scrap Viva Real real estate data

    Atributes:
        primeira_pagina:
        browser:
        dd:
        df:
        html:
        soup:
        shape:

    Methods:
        __init__():
        scraper():
        next_page():
        uniques():
        save():
        adddate():
        filter():
        shape():
        exit():
        run():

    """
    def __init__(self, primeira_pagina):
        self.primeira_pagina = primeira_pagina
        self.browser = Firefox()
        self.browser.get(primeira_pagina)
        sleep(2)
        self.df = pd.DataFrame()
        logging.info('Class VR created successfully')
    
    def scraper(self, ngroup):
        """
        asdasdasdasd
        """
        self.html = self.browser.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        lista = list()
        for i in self.soup.find_all('div', {'data-type' : 'property'}):
            lista.append([
                'vivareal.com'+i.find('a')['href'],
                i.find('span', {'class' : 'property-card__address'}).string,
                i.find('h2', {'class' : 'property-card__header'}).text.strip().split('    ')[0],
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-area'}).span.text.strip(),
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).span.text.strip(),
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).span.text.strip(),
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).span.text.strip(),
                i.find('div', {'class' : 'property-card__price js-property-card-prices js-property-card__price-small'}).text.strip().split(' ')[1].replace('.', '')
                
            ])
        self.dd = pd.DataFrame(lista, columns=['url', 'address', 'title', 'area', 'bedrooms', 'bathrooms', 'garages', 'price'])
        self.df = pd.concat([self.df, self.dd], ignore_index=True)
        logging.info(f'Page {ngroup} scraped')

    def next_page(self):
        """
        asdasdasdasd
        """
        self.nextpage = self.browser.find_elements_by_class_name('js-change-page')
        self.nextpage[-1].send_keys(Keys.RETURN)
        sleep(15)
        logging.info('Next page')

    def uniques(self):
        """
        asdasdasdasd
        """
        self.df = self.df.drop_duplicates()
        logging.info(f'{len(self.df.url.drop_duplicates())} unique links ')

    def save(self):
        """
        asdasdasdasd
        """
        self.df.to_csv(r'data/vr_imoveis.csv')
        logging.info('CSV saved')
    
    def adddate(self):
        """
        asdasdasdasd
        """
        self.df['date'] = '{:%Y-%m-%d }'.format(datetime.datetime.now())
        logging.info('Date added')

    def filter(self):
        """
        asdasdasdasd
        """
        self.df = self.df[-self.df['price'].isin(['Consulta'])] # minimum filters during the scrap phase, aftwards I can filter and treat it better
        # self.df = self.df[-self.df.area.str.contains("-", na=False)]
        # self.df = self.df[-self.df.bedrooms.str.contains("--", na=False)]
        # self.df = self.df[self.df.title.str.contains("Apartamento", na=False)]
        logging.info('DF filtered')

    def shape(self):
        """
        asdasdasdasd
        """
        # self.shapedf = self.df.shape
        logging.info(f'DF {self.df.shape} shaped')

    def exit(self):
        """
        asdasdasdasd
        """
        sleep(1)
        self.browser.quit()
        logging.info('Exiting')
        
    def run(self, qpages):
        """
        asdasdasdasd
        """
        logging.info('Running method .run()')
        for page in range(1, qpages):
            self.scraper(page)
            self.next_page()
        self.adddate()
        self.uniques()
        self.filter()
        self.shape()
        self.save()
        self.exit()


