from pydantic import BaseModel, field_validator, constr, PositiveFloat
from typing import Annotated

from .enums import *

class FiltersModel(BaseModel):
    title: Annotated[str, constr(min_length=1, max_length=50, to_lower=True)] 
    brand: Annotated[str, constr(min_length=1, max_length=20, to_lower=True)] 
    sex: Sex
    type_: Type
    size: Size
    color: Color
    price: PositiveFloat
    state: State
    material: Material    
    
    
class SearchModel(BaseModel):
    query: Annotated[str, constr(min_length=1, max_length=50, to_lower=True)] 
    filters: FiltersModel