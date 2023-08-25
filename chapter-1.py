import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

def prepare_country_stats(a,b):
    table1 = pd.read_csv(a)
    table2 = pd.read_csv(b)
    merged = a.merged(b, on='title')
    return merged.to_csv("output.csv", index = False)


#Load data
oecd_bli = pd.read_csv('BLI.csv', thousands=',')
gdp_per_capita = pd.read_csv('WEO_Data.csv', thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')

#Preparing the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
print(country_stats)

