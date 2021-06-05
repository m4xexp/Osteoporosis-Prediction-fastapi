from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form
import pandas as pd
import pickle

app = FastAPI()

#Model
pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index():
    return "Welcome to Diagnos API "


@app.post("/predict/ost/")
async def predict_walking(Age: int = Form(...),
             Gender: int = Form(...), Drink: int = Form(...), 
             Smoke: int = Form(...), Drug: int = Form(...), 
             DailyWalking: int = Form(...), EatingHabit: int = Form(...), 
             Walk15Min: int = Form(...), GetupFromChair: int = Form(...), 
             WalkWORail: int = Form(...), WalkWOCane: int = Form(...),
             ActivelyGoOut: int = Form(...)):

    data = [[Age,Gender,Drink,Smoke,Drug,DailyWalking,EatingHabit,Walk15Min,GetupFromChair,WalkWORail,WalkWOCane,ActivelyGoOut]]
    df_pred = pd.DataFrame(data, columns = ['Age','Gender','Drink','Smoke','Drug','DailyWalking','EatingHabit',
                                            'Walk15Min','GetupFromChair','WalkWORail','WalkWOCane','ActivelyGoOut'])
    predict = model.predict(df_pred)
    if predict[0] == 0:
        predict = "You don't have osteoporosis."
        advice = ''
        result = 0;

    else:
        predict = 'You have osteoporosis.'
        advice = ' Should consult a doctor to prevent and treat osteoporosis immediately.'
        result = 1;

    return {'result': predict, 'predict': result, 'advice': advice}       
    
