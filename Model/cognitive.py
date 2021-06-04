import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from Model.dataset import data
from Converter.JsonConvert import arrEncoder

lr = LogisticRegression()
data = data()

class model():
    def __init__(self):
        self.df = data.preprocess(data.df_life)
        X = self.df[['GoWithoutRailing','GetupFromChair','Walk15min','WalkWOCane','ActivelyGoOut','WalkScore']]
        y = self.df['WalkEvaluate']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        lr.fit(X_train,y_train)
    
    def predicts(self, data_pred):
        y_pred = lr.predict(data_pred)
        # print(y_pred)
        obj = y_pred
        encorder = arrEncoder()
        result = encorder.encode(obj)
        return result



