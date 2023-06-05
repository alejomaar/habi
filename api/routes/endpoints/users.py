from typing import Any, List
from utils.model_io import load_pickle
from fastapi import APIRouter
from  schemas.user import User
import math

model = load_pickle('./models/XGBClassifier.pkl')
dv = load_pickle('./models/dict_vectorizer.pkl')

json = {'type_independent_activity_id': '11', 'is_tax_return': True, 'region_id': '1.0', 'activity': 'manufacture', 'job_role': 'independent', 'year_exp_token': '2023', 'age': 60, 'terms_conditions': True, 'is_selected': False, 'has_date_exp_token': True, 'incomes': 4325333.0, 'extra_incomes': 0.0, 'familiar_debts': 500000.0}

def preprocessor(data:dict):
    data['has_extra_incomes'] = data['extra_incomes'] != 0  
    data['has_familiar_debts'] = data['familiar_debts'] != 0  
    data['has_region_id'] = data['region_id'] != 0
    
    data['incomes'] = math.log1p(data['incomes'])
    data['extra_incomes'] = math.log1p(data['extra_incomes'])
    data['familiar_debts'] = math.log1p(data['familiar_debts'])
    
    if data['age'] < 20:
        data['age_section'] = 'less 20'
    elif data['age'] < 40:
        data['age_section'] = 'less 40'
    else:
        data['age_section'] = 'more 40'
    del data['age']
    
    return data
    

router = APIRouter()

@router.get("/test")
def read_users() -> Any:
    user = preprocessor(json) 
    output = dv.transform([user])
    prob = model.predict_proba(output)[0][0]
    print(prob)
    return dict(pred =float(prob) )

@router.post("/predict")
def read_users(user:User) -> Any:
    user = dict(user)
    user = preprocessor(user) 
    output = dv.transform([user])    
    prob = model.predict_proba(output)[0][0]
    return dict(pred = float(prob) )





