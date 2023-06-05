import math

def preprocess(data:dict):
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