# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:44:21 2019

@author: sairam.E
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import *
public_griv_df = pd.read_csv("pg_complete_set_1.csv",
                         engine='python',error_bad_lines=False)

#print(public_griv_df.columns)

y = public_griv_df.org_name2
X = public_griv_df.subject_content

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

txt_clf=Pipeline([ ('vect',CountVectorizer()),
                  
                  ('clf',MultinomialNB())])
txt_clf.fit(X_train, y_train)
predictions = txt_clf.predict(['It is submitted that Bhagat Chandra Hospital Near Mahavir Enclave New Delhi-****** is giving facility of Pathological Tests in collaboration with Max Lab. Max Lab is providing CGHS rate for central government employees'])
print(predictions)