# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:38:08 2019

@author: sairam.E
"""

import pandas as pd


#reading the input csv data
air_pollution_data = pd.read_csv("air_pollution_data.csv",encoding="cp1252")

print(air_pollution_data.head())