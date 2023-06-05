from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    type_independent_activity_id: str
    is_tax_return: bool
    region_id :str
    name:str
    'name.1':str
    year_exp_token:str
    age_section:str
    month_exp_token: int
    terms_conditions: bool
    is_selected: bool
    has_extra_incomes: bool
    has_familiar_debts: bool
    has_region_id: bool
    has_date_exp_token:bool
    incomes:float
    extra_incomes:float
    familiar_debts:float