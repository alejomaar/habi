from typing import Any, List
from utils.model_io import load_pickle
from fastapi import APIRouter


model = load_pickle('./models/XGBClassifier.pkl')
dv = load_pickle('./models/dict_vectorizer.pkl')

json = {'type_independent_activity_id': '11',
 'is_tax_return': 1,
 'region_id': '1.0',
 'name': 'manufacture',
 'name.1': 'independent',
 'year_exp_token': '2023',
 'age_section': 'more 40',
 'month_exp_token': 4,
 'terms_conditions': 1,
 'is_selected': 0,
 'has_extra_incomes': 1,
 'has_familiar_debts': 1,
 'has_region_id': True,
 'has_date_exp_token': True,
 'incomes': 16.300417291085605,
 'extra_incomes': 0.0,
 'familiar_debts': 0.0}

router = APIRouter()

@router.get("/test")
def read_users() -> Any:
    output = dv.transform([json])
    prob = model.predict_proba(output)[0][0]
    print(prob)
    return dict(pred =float(prob) )





