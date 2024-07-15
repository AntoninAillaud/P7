#FAST_API
import pandas as pd
import dill as pickle
from fastapi import FastAPI
import uvicorn
import nest_asyncio

#Récupération du modèle et du seuil
best_model = pickle.load(open('./BEST_MODEL.sav', 'rb'))
f = open("./seuil.txt","r")
seuil = float(f.read())
f.close()

#Récupération des données
df = pd.read_csv('./test.csv')

app = FastAPI()

#Affichage d'un message simple pour la page d'accueuil
@app.get("/")
async def root():
    return {"message": "Hello World"}

#Affichage si pour un client donné (idx) le modèle et le seuil accepte ou non sa demande de crédit
@app.post("/predict/{idx}")
async def predict(idx: int):
    res = best_model.predict_proba(df.values[idx].reshape(1,-1))[:,1]
    return "Rejetée" if res > seuil else 'Acceptée'

if __name__ == '__main__':
    nest_asyncio.apply()
    uvicorn.run("api:app", host="0.0.0.0", port="8000", reload=False)
