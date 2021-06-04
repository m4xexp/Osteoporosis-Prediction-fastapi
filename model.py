import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# from pycaret.classification import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from Model.dataset import data

lr = LogisticRegression()

data = data()

df = data.preprocess(data.df_life)

X = df[['GoWithoutRailing','GetupFromChair','Walk15min','WalkWOCane','ActivelyGoOut','WalkScore']]
y = df['WalkEvaluate']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

df_test = [[0,0,0,1,1,2]]
df_pred = pd.DataFrame(df_test, columns = ['GoWithoutRailing','GetupFromChair','Walk15min','WalkWOCane','ActivelyGoOut','WalkScore'])

lr.fit(X_train,y_train)
y_pred = lr.predict(df_pred)

print(y_pred)



