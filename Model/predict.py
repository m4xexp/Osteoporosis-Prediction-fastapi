import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from dataset import data
# from Converter.JsonConvert import arrEncoder
import pickle

lr = LogisticRegression()
data = data()

df = data.preprocess(data.df_life)
X = df[["Age", "Gender","Drink","Smoke","Drug","DailyWalking","EatingHabit","Walk15Min","GetupFromChair","WalkWORail","WalkWOCane","ActivelyGoOut"]]
y = df['Predict']
test_size = 0.3
state = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=state)

lr.fit(X_train,y_train)
# print(y_pred)


# with open('ost_model', 'wb') as f:
#     pickle.dump(lr,f)

# with open('ost_model' , 'rb') as f:
#     ost_model = pickle.load(f)

# result =ost_model.predict(df_pred)

# print(type(result[0]))

