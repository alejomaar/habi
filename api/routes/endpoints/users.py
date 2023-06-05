from typing import Any, List
from utils.model_io import load_pickle
from fastapi import APIRouter
from  schemas.user import UserViability, UserIsSelected
import math
from utils.preprocess import preprocess

model_viability = load_pickle('./models/XGBClassifier_viability.pkl')
dv_viability = load_pickle('./models/dict_vectorizer_viability.pkl')
model_is_selected = load_pickle('./models/XGBClassifier_is_selected.pkl')
dv_is_selected = load_pickle('./models/dict_vectorizer_is_selected.pkl')

router = APIRouter()


@router.post("/predict/viability")
def read_users(user:UserViability) -> Any:
    user = dict(user)
    user = preprocess(user) 
    output = dv_viability.transform([user])    
    prob = model_viability.predict_proba(output)[0][0]
    return dict(pred = float(prob) )


@router.post("/predict/is_selected")
def read_users(user:UserIsSelected) -> Any:
    user = dict(user)
    user = preprocess(user) 
    output = dv_is_selected.transform([user])    
    prob = model_is_selected.predict_proba(output)[0][0]
    return dict(pred = float(prob) )




