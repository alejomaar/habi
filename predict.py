from utils.model_io import load_pickle

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
 'familiar_debts': 0.0
 }




model = load_pickle('./models/XGBClassifier.pkl')
dv = load_pickle('./artifacts/dict_vectorizer.pkl')
output = dv.transform([json])
prob = model.predict_proba(output)

print(prob[0])