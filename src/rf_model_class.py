#!/usr/bin/env python3

"""
Class for the Random Forest model on São José real estate data - Predicting house pricing
"""

# Load the packages
import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

import joblib

import logging

# Log config
LOG_FORMAT = "%(asctime)-24s [%(filename)s:%(lineno)d] \
    %(levelname)-6s %(message)s"

logging.basicConfig(filename='logs/logs.log',
                    filemode='a',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)


# RF class
class RF():
    """
    Class to model the Viva Real Real Estate data through the Random Forest Model
    """
    def __init__(self, df_address):
        self.df = pd.read_csv(df_address)
        logging.info('Object RF created successfully')
    
    def transform_df(self):
        self.df = self.df[['price', 'area', 'bedrooms', 'bathrooms', 'garages']]
        self.df = self.df.loc[self.df['price'] != 'partir']
        self.df.bathrooms = self.df.bathrooms.replace({"--": 0})
        self.df.bathrooms = self.df.bathrooms.replace({"1-2": 1.5}) # replace for something that works anyway
        self.df.bathrooms = self.df.bathrooms.replace({"2-3": 2.5})
        self.df.garages = self.df.garages.replace({"--": 0})
        self.df.garages = self.df.garages.replace({"1-2": 1.5})
        self.df.garages = self.df.garages.replace({"2-3": 2.5})
        self.df = self.df.apply(pd.to_numeric)
        logging.info('Data transformed')
    
    def set_label(self):
        self.labels = np.array(self.df.price)
        logging.info('label set')

    def set_feature(self):
        self.features = np.array(self.df[['area', 'bedrooms', 'bathrooms', 'garages']])
        logging.info('features set')

    def fit_model(self):
        self.rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
        self.rf.fit(self.features, self.labels)
        self.r2 = self.rf.score(self.features, self.labels)
        logging.info(f'Model scored {self.r2} R2')

    def make_prediction(self, pred_feat):
        self.prediction = self.rf.predict(np.array([pred_feat]))[0].astype(int)
        self.prediction_txt = f'{self.prediction} reais'
        logging.info(f'For parameters {pred_feat}, model predicted {self.prediction} reais for this home')

    def make_pickle(self):
        joblib.dump(self.rf, 'data/rf_vr_model.pkl')

    def run(self):
        """
        run() method applies methods in an orderlly manner
        """
        self.transform_df()
        self.set_label()
        self.set_feature()
        self.fit_model()
        logging.info('Method run() completed')


# RFtry1 = RF(df_address='data/sj_imoveis_scraped.csv')
# RFtry1.run()
# RFtry1.make_pickle()
# RFtry1.make_prediction([80, 1, 1, 1])
