#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

## Load the data

# Better Life Index data
bli = pd.read_csv("./data/bli_original.csv", delimiter=',')
life_sat_total = bli[bli["INEQUALITY"] == "TOT"]
life_sat_total = life_sat_total.pivot(index="Country", columns="Indicator", values="Value")
# Export the data (if you want to reason on the data before continue)
life_sat_total.to_csv('./data/life_sat_total.csv')

# International Monetary Fund data
imf = pd.read_csv("./data/imf-original.csv", thousands='.', delimiter=';', na_values="n/a", index_col="Country")
imf.rename(columns={"2015": "GDP per capita"}, inplace=True)
# Export the data (if you want to reason on the data before continue)
imf.to_csv('./data/gdp_per_capita.csv')

# Prepare the data set
country_stats = pd.merge(life_sat_total, imf, on='Country')
# Export the data (if you want to reason on the data before continue)
country_stats.to_csv('./data/country_stats.csv')

# +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
# |L|i|n|e|a|r| |R|e|g|r|e|s|s|i|o|n|
# +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+

# X as an independent variable
X = np.c_[country_stats['GDP per capita']]

# y as a dependent variable - predictor
y = np.c_[country_stats['Life satisfaction']]

## Visualize the data as scatter model to understand the basic correlation between X and y
plt.scatter(X, y)
plt.xlabel('GDP per Capita')
plt.ylabel('Life satisfaction')
plt.show()

# Select a linear model
model = sklearn.linear_model.LinearRegression()
## Train the model
model.fit(X, y)

#Make a prediction for Cyprus
X_new = [[22587]] # Cyprus GDP per capita

print ("Cyprus' Life satisfaction based on a LinearRegression:",model.predict(X_new))

# +-+-+-+-+-+-+-+-+-+-+
# |K|N|e|i|g|h|b|o|r|s|
# +-+-+-+-+-+-+-+-+-+-+

# Visualize the data as a bar model to see the closest countries to Cyprus in terms of GDP per capita (see Spain, Slovenia and Portugal)
country_stats.filter(items=['GDP per capita']).sort_values("GDP per capita", ascending=False).plot.bar()
plt.xlabel('Country')
plt.ylabel('GDP per capita')
plt.show()

#X as an independent variable
X = np.c_[country_stats['GDP per capita']]
# y as a dependent variable - predictor
y = np.c_[country_stats['Life satisfaction']]

# Select a KNeighbor model
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
## Train the model
model.fit(X, y)
#Make another prediction for Cyprus
X_new = [[22587]] # Cyprus GDP per capita

print ("Cyprus' Life satisfaction based on a KNeighborsRegressor:",model.predict(X_new))