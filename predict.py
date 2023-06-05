from utils.model_io import load_pickle

json = {'type_independent_activity_id': '2',
 'is_tax_return': 1,
 'region_id': '0.0',
 'name': 'others',
 'name.1': 'independent',
 'year_exp_token': '2023',
 'age_section': 'more 40',
 'month_exp_token': 3,
 'terms_conditions': 0,
 'is_selected': 0,
 'has_extra_incomes': 1,
 'has_familiar_debts': 0,
 'has_region_id': False,
 'has_date_exp_token': False,
 'incomes': 15.285262405144474,
 'extra_incomes': 0.0,
 'familiar_debts': 13.122365377402328}



model = load_pickle('./models/XGBClassifier.pkl')
dv = load_pickle('./artifacts/dict_vectorizer.pkl')
output = dv.transform([json])
prob = model.predict_proba(output)

print(prob[0][0])