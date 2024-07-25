#FAST_API
import pandas as pd
import dill as pickle
from fastapi import FastAPI
import uvicorn
import nest_asyncio
import json
from pydantic import BaseModel

#Récupération du modèle et du seuil
best_model = pickle.load(open('./BEST_MODEL.sav', 'rb'))
f = open("./seuil.txt","r")
seuil = float(f.read())
f.close()

#Récupération des données
df = pd.read_csv('./test.csv')

class User_input(BaseModel):
    idx : int

app = FastAPI()

#Affichage d'un message simple pour la page d'accueuil
@app.get("/")
async def root():
    return {"message": "Hello World"} 

#Affichage si pour un client donné (idx) le modèle et le seuil accepte ou non sa demande de crédit
@app.post("/predict")
async def predict(input:User_input):
    res = best_model.predict_proba(df.values[input.idx].reshape(1,-1))[:,1]
    rep = "Rejetée" if res[0] > seuil else 'Acceptée'
    d = [{'rep' : rep, 'proba' : res[0]}]
    return d

if __name__ == '__main__':
    nest_asyncio.apply()
    uvicorn.run("api:app", host="0.0.0.0", port="8000", reload=False)
