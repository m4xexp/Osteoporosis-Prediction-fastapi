from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import pandas as pd
import pickle
import uvicorn

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


@app.get('/test/{name}')
async def test(name):
    return {'Name': {name}}

 
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
    


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
 