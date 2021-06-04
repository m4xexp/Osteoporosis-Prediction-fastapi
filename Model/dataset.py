import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

class data():
    def __init__(self):
        self.df_attr = pd.read_csv('Data/dataset.csv', skiprows=1, low_memory=False)
        self.df = pd.DataFrame()

    def preprocess(self, df):
        df.columns = ["No", "SubjectID", "Date", "Appetite","EatingHabit","Preference","Sleep","AnxietyAboutHealth","AnxietyAboutForgetfulness","GoWithoutRailing","GetupFromChair","Walk15min","WalkWOCane","ActivelyGoOut","WalkScore","WalkEvaluate","CleanYourSelf","Shopping","PrepareMeal","WriteDocument","CanCall","LifeScore","LifeEvaluate","HaveConselor","HaveConselorWhenSick","HaveSomeoneTakeToHospital","HavePeopleTakeCareWhenSleep","RelyingOnSomeone","SocialScore","SocialEvaluate","NoWeightLoss","NoWeightGain","EatHardFood","DontGetSickWhenDrinkTea","DontMindThirst","NutritionScore","NutritionEvaluate"]

        df['EatingHabit'] = df['EatingHabit'].str.slice_replace(1, repl='')
        return df

    def train(self):
        lr = LogisticRegression()
        X = df[['GoWithoutRailing','GetupFromChair','Walk15min','WalkWOCane','ActivelyGoOut','WalkScore']]
        y = df['WalkEvaluate']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        lr.fit(X_train,y_train)
        

    def predict(self, X_test):
        result_pred = lr.predict(X_test)
        return result_pred

