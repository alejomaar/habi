from pydantic import BaseModel

# Shared properties
class UserBase(BaseModel):
    type_independent_activity_id: str ='11'
    is_tax_return: bool =1 
    region_id :str = '1.0'
    activity:str='manufacture'
    job_role:str='independent'
    year_exp_token:str='2023'
    age:int=60
    terms_conditions: bool=1
    has_date_exp_token:bool= True
    incomes:float = 4_325_333
    extra_incomes:float = 0.0
    familiar_debts:float = 500_000
    class Config:
        orm_mode = True

# Shared properties
class UserViability(UserBase):
    is_selected: bool= 0
        
# Shared properties
class UserIsSelected(UserBase):
    viability: bool= 0
        
