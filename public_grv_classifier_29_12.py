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
from sklearn.externals import joblib
#loading the input csv data into the pandas dataframe
public_griv_df = pd.read_csv("pg_complete_set_1.csv",
                         engine='python',error_bad_lines=False)

#print(public_griv_df.columns)

y = public_griv_df.org_name
X = public_griv_df.subject_content

#splitting the data into training and testing purposes
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#pipeline for Naive Bayes algorithm
txt_clf_NB=Pipeline([ ('vect',CountVectorizer()),
                  
                  ('clf',MultinomialNB())])

#pipeline for SVM classifier algorithm
text_clf_svm = Pipeline([('vect', CountVectorizer()),
                       ('tfidf', TfidfTransformer()),
                      ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-3, random_state=42))
 ])


#fitting and measuring accuracy for SVM model
text_clf_svm.fit(X_train, y_train)

#joblib.dump(text_clf_svm, 'model.pkl')
#text_clf_svm = joblib.load('model.pkl')
#print("Model dumped!")

predictions_svm = text_clf_svm.predict(X_test)
print(np.mean(predictions_svm == y_test))
svm_accuracy = np.mean(predictions_svm == y_test)
#fitting and measuring accuracy for Naive Bayes model
txt_clf_NB.fit(X_train, y_train)
predictions_NB = txt_clf_NB.predict(X_test)
print(np.mean(predictions_NB == y_test))
NB_accuracy = np.mean(predictions_NB == y_test)

if (int(svm_accuracy))< (int(NB_accuracy)):
    print('Naive Bayes model has better accuracy and used for modelling')
    joblib.dump(txt_clf_NB, 'model.pkl')
    txt_clf_NB = joblib.load('model.pkl')
    print("Model dumped!")
    complete_df = pd.concat([y_test], axis=1)  # features and actual
    complete_df['Predicted'] = predictions_NB
    print(complete_df)


else:    
    print('svm model has better accuracy and used for modelling')
    joblib.dump(text_clf_svm, 'model.pkl')
    text_clf_svm = joblib.load('model.pkl')
    print("Model dumped!")
    complete_df = pd.concat([y_test], axis=1)  # features and actual
    complete_df['Predicted'] = predictions_svm
    print(complete_df)


