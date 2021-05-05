'''
Class for the Random Forest model on São José real estate data - Predicting house pricing
'''

# Load the packages
import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

import logging

# Log config
LOG_FORMAT = "%(asctime)-24s [%(filename)s:%(lineno)d] \
    %(levelname)-6s %(message)s"

logging.basicConfig(filename='logs/logs.log',
                    filemode='a',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)

# Load the data
df = pd.read_csv('data/sj_imoveis_scraped2.csv')
df = df[['price', 'area', 'bedrooms', 'bathrooms', 'garages']]


class RF():
    def __init__(self, df_address):
        self.df = pd.read_csv(df_address)
        # logging.info('Object RF created successfully')
    
    def transform_df(self): # Better name
        self.df = self.df[['price', 'area', 'bedrooms', 'bathrooms', 'garages']]
        self.df = self.df.loc[df['price'] != 'partir']
        self.df = self.df.garages.replace({"--": 0})
        self.df = self.df.bathrooms.replace({"1-2": 1.5})
        self.df = self.df.garages.replace({"1-2": 1.5})
        self.df = self.df.garages.replace({"2-3": 2.5})
        self.df = self.df.apply(pd.to_numeric)
        # logging.info(f'DF transformed')
    
    def set_label(self):
        self.labels = np.array(self.df.price)

    def set_feature(self):
        self.feature = self.df[['area', 'bedrooms', 'bathrooms', 'garages']]
        self.feature_list = list(self.features.columns)
        self.features = np.array(self.features)

    # def measure_fit(self):
    #     self.train_features, self.test_features, self.train_labels, self.test_labels = train_test_split(self.features, self.labels, test_size = 0.25, random_state = 42)
    #     self.rft = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    #     self.rft.fit(self.train_features, self.train_labels)
    #     self.r2 = self.rft.score(self.train_features, self.train_labels)
    #     logging.info(f'R2 {self.r2} scored') # melhorar

    def fit_model(self):
        self.rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
        self.rf.fit(self.features, self.labels)
        self.r2 = self.rf.score(self.features, self.labels)
        logging.info(f'R2 {self.r2} scored') # melhorar

    def prediction(self):
        self.predictions = self.rf.predict(self.test_features) # input the parameters here

    def shape_df(self):
        self.shape_df = self.df.shape
        # logging.info(f'DF {self.df.shape} shaped')

    def corr_df(self):
        self.corr_df = self.df.corr().price
        # logging.info(f'asasasas')

    def run(self):
        self.transform_df()
        self.shape_df()
        self.corr_df()







RFtry1 = RF(df_address='data/sj_imoveis_scraped.csv')
RFtry1.shape_df()