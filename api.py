#FAST_API
import pandas as pd
import dill as pickle
from fastapi import FastAPI
import uvicorn
import nest_asyncio

best_model = pickle.load(open('./BEST_MODEL.sav', 'rb'))
f = open("./seuil.txt","r")
seuil = float(f.read())
f.close()

df = pd.read_csv('./test.csv')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict/{idx}")
async def predict(idx: int):
    res = best_model.predict_proba(df.values[idx].reshape(1,-1))[:,1]
    return "Rejetée" if res > seuil else 'Acceptée'

if __name__ == '__main__':
    nest_asyncio.apply()
    uvicorn.run("main:app", host="0.0.0.0", port="8000", reload=False)
