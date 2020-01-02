# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 00:58:25 2019

@author: sairam.E
"""

import pandas as pd
public_complaints_df = pd.read_csv("cpgrams_1.csv",
                         engine='python',error_bad_lines=False)

print(public_complaints_df.info())

public_complaints_resolution_df = pd.read_csv("cpgrams_movement_1.csv",
                        engine='python',error_bad_lines=False)

print(public_complaints_resolution_df.info())

#merged_inner = pd.merge(left=public_complaints_df,right=public_complaints_resolution_df, how='inner')
merged_inner = public_complaints_df.merge(public_complaints_resolution_df)
print(merged_inner.head())

