from pydantic import BaseModel, field_validator, Field, PositiveFloat, PositiveInt
from typing import Annotated, Optional, Union, List

from .enums import *

def strip_lower(v):
    return str(v).strip().lower()


class FiltersModel(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=50)
    brand: Optional[Union[Brand, str]] = None
    sex: Optional[Sex] = None
    category: Optional[str] = Field(None) # clothes/shoes
    type_: Optional[str] = Field(None)
    size: Optional[Union[str, ClothesSize, EuSize, UkSize, UsSize]] = None
    size_by_native: Optional[str] = Field(None) # eu/uk/us
    color: Optional[Union[ColorOlx, ColorShafa, str]] = None
    price_min: Optional[PositiveFloat] = None
    price_max: Optional[PositiveFloat] = None
    state: Optional[State] = None
    material: Optional[Material] = None

    
    @field_validator('title', mode='before')
    @classmethod
    def validate_title(cls, v):
        if v:
            return strip_lower(v)
        return v

    @field_validator('brand', mode='before')
    @classmethod
    def validate_brand(cls, v):
        if v:
            brand_str = strip_lower(v)
            for brand in Brand:
                if brand.value.lower() == brand_str:
                    return brand
            return brand_str
        return v

    @field_validator('price_max')
    @classmethod
    def validate_price_max(cls, v, info):
        if v and info.data.get('price_min'):
            if v < info.data['price_min']:
                raise ValueError('"price_max" have to be more than "price_min" or eq it ')
        return v

    @field_validator('category')
    @classmethod
    def validate_category(cls, v):
        if v:
            v = strip_lower(v)
            if v not in ['clothes', 'shoes']:
                raise ValueError('category have to be "clothes" or "shoes"')
        return v

    @field_validator('size_by_native')
    @classmethod
    def validate_size_by_native(cls, v, info):
        if v:
            v = strip_lower(v)
            if info.data.get('category') == 'shoes' and v not in ['eu', 'uk', 'us']:
                raise ValueError('"size_by_native" have to be "eu", "uk" or "us"')
        return v


    @field_validator('color', mode='before')
    @classmethod
    def validate_color(cls, v):
        if v:
            v = strip_lower(v)
            for color in Color:
                if color.value == v:
                    return color
        return v

    @field_validator('material', mode='before')
    @classmethod
    def validate_material(cls, v):
        if v:
            v = strip_lower(v)
            for mat in Material:
                if mat.value == v:
                    return mat
        return v


class SearchModel(BaseModel):
    query: str = Field(min_length=1, max_length=50)
    filters: Optional[FiltersModel] = None

    @field_validator('query', mode='before')
    @classmethod
    def validate_query(cls, v):
        return strip_lower(v)


class ProductModel(BaseModel):
    id: str
    title: str
    brand: Optional[Union[BrandOlx, BrandShafa, str]] = None
    sex: Optional[Sex] = None
    category: str  # clothes or shoes
    type_: Optional[str] = Field(None)
    size: Optional[str] = None
    size_by_native: Optional[str] = None
    color: Optional[Union[ColorShafa, ColorOlx, str]] = None
    price: PositiveFloat
    state: Optional[State] = None
    material: Optional[Material] = None
    description: Optional[str] = None
    images: List[str] = Field(default_factory=list)
    url: str


    @field_validator('title', 'brand', 'description', mode='before')
    @classmethod
    def strip_strings(cls, v):
        if v:
            return str(v).strip()
        return v
    