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
X = df[['EatingHabit','NoWeightLoss','NoWeightGain','EatHardFood','DontGetSickWhenDrinkTea','DontMindThirst','NutritionScore']]
y = df['NutritionEvaluate']
test_size = 0.3
state = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=state)

lr.fit(X_train,y_train)
y_pred = lr.predict(df_pred)

print(y_pred)


# with open('nutrition_model', 'wb') as f:
#     pickle.dump(lr,f)

# with open('nutrition_model' , 'rb') as f:
#     nutrion_model = pickle.load(f)

# result =nutrion_model.predict(df_pred)

# print(type(result[0]))



