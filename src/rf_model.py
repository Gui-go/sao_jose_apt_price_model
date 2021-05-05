'''
Random Forest on São José real estate data - Predicting house pricing
'''

# Load the packages
import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/sj_imoveis_scraped2.csv')
df = df[['price', 'area', 'bedrooms', 'bathrooms', 'garages']]

# Filter and replace some data
df = df.loc[df['price'] != 'partir']
df.garages = df.garages.replace({"--": 0})
df.bathrooms = df.bathrooms.replace({"1-2": 1.5})
df.garages = df.garages.replace({"1-2": 1.5})
df.garages = df.garages.replace({"2-3": 2.5})

# Turn the all into numeric
df = df.apply(pd.to_numeric)

# Check their correlation
df.corr().price

# Prepare the data for the RF model
labels = np.array(df['price'])
features = df[['area', 'bedrooms', 'bathrooms', 'garages']]
feature_list = list(features.columns)
features = np.array(features)

# Split the data
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

# Fit the model
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(train_features, train_labels)

rf.score(train_features, train_labels) # r2
# Make predictions
predictions = rf.predict(test_features)

# Estimate the error
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

mape = 100 * (errors / test_labels)
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

# Get the Feature importance
importances = list(rf.feature_importances_)
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]
rf_most_important = RandomForestRegressor(n_estimators= 1000, random_state=42)

important_indices = [feature_list.index('area'), feature_list.index('garages')]  # corrigir
train_important = train_features[:, important_indices]
test_important = test_features[:, important_indices]

# Fit the model considering the feature importance
rf_most_important.fit(train_important, train_labels)
predictions = rf_most_important.predict(test_important)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
mape = np.mean(100 * (errors / test_labels))
accuracy = 100 - mape
print('Accuracy:', round(accuracy, 2), '%.')

# Some plots
plt.style.use('fivethirtyeight')
x_values = list(range(len(importances)))
plt.bar(x_values, importances, orientation = 'vertical')
plt.xticks(x_values, feature_list, rotation = 'vertical')
plt.ylabel('Importance')
plt.xlabel('Variable')
plt.title('Variable Importances')
plt.plot()




