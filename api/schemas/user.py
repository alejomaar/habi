from typing import Optional

from pydantic import BaseModel


# Shared properties
class User(BaseModel):
    type_independent_activity_id: str ='11'
    is_tax_return: bool =1 
    region_id :str = '1.0'
    activity:str='manufacture'
    job_role:str='independent'
    year_exp_token:str='2023'
    age:int=60
    terms_conditions: bool=1
    is_selected: bool= 0
    has_date_exp_token:bool= True
    incomes:float = 4_325_333
    extra_incomes:float = 0.0
    familiar_debts:float = 500_000
    class Config:
        orm_mode = True
        
class User2(BaseModel):
    type_independent_activity_id: str ='11'
    is_tax_return: bool =1 
    region_id :str = '1.0'
    name:str='manufacture'
    name_1:str='independent'
    year_exp_token:str='2023'
    age_section:str='more 40'
    month_exp_token: int =4
    terms_conditions: bool=1
    is_selected: bool= 0
    has_extra_incomes: bool =1
    has_familiar_debts: bool =1
    has_region_id: bool = True
    has_date_exp_token:bool= True
    incomes:float = 16.3
    extra_incomes:float = 0.0
    familiar_debts:float = 0.0
    class Config:
        orm_mode = True