from enum import Enum


class Sex(Enum):
    MEN = 'men'
    WOMEN = 'women'
    CHILD = 'child'
    UNISEX = 'unisex'


class WomenClothes(Enum):
    DRESS = 'dress'
    SKIRT = 'skirt'
    BLOUSE = 'blouse'
    PANTS = 'pants'
    JACKET = 'jacket'
    COAT = 'coat'
    SWEATER = 'sweater'
    T_SHIRT = 't-shirt'
    JUMPSUIT = 'jumpsuit'
    CARDIGAN = 'cardigan'
    TOP = 'top'


class MenClothes(Enum):
    SHIRT = 'shirt'
    PANTS = 'pants'
    JACKET = 'jacket'
    COAT = 'coat'
    SWEATER = 'sweater'
    T_SHIRT = 't-shirt'
    SUIT = 'suit'
    SHORTS = 'shorts'
    POLO = 'polo'
    HOODIE = 'hoodie'


class ChildClothes(Enum):
    T_SHIRT = 't-shirt'
    PANTS = 'pants'
    DRESS = 'dress'
    SHORTS = 'shorts'
    JACKET = 'jacket'
    SWEATER = 'sweater'
    ROMPER = 'romper'
    OVERALLS = 'overalls'


class UnisexClothes(Enum):
    T_SHIRT = 't-shirt'
    HOODIE = 'hoodie'
    SWEATSHIRT = 'sweatshirt'
    JACKET = 'jacket'
    PANTS = 'pants'
    SHORTS = 'shorts'


class WomenShoes(Enum):
    HEELS = 'heels'
    FLATS = 'flats'
    SNEAKERS = 'sneakers'
    BOOTS = 'boots'
    SANDALS = 'sandals'
    LOAFERS = 'loafers'
    ANKLE_BOOTS = 'ankle-boots'
    PUMPS = 'pumps'


class MenShoes(Enum):
    OXFORD = 'oxford'
    LOAFERS = 'loafers'
    SNEAKERS = 'sneakers'
    BOOTS = 'boots'
    SANDALS = 'sandals'
    DERBY = 'derby'
    BROGUES = 'brogues'
    CASUAL = 'casual'


class ChildShoes(Enum):
    SNEAKERS = 'sneakers'
    SANDALS = 'sandals'
    BOOTS = 'boots'
    SCHOOL_SHOES = 'school-shoes'
    SLIPPERS = 'slippers'


class UnisexShoes(Enum):
    SNEAKERS = 'sneakers'
    BOOTS = 'boots'
    SANDALS = 'sandals'
    SLIPPERS = 'slippers'


class EuSize(Enum):
    EU_19 = "19"  
    EU_20 = "20"
    EU_21 = "21"
    EU_22 = "22"
    EU_23 = "23"
    EU_24 = "24"
    EU_25 = "25"
    EU_26 = "26"
    EU_27 = "27"
    EU_28 = "28"
    EU_29 = "29"
    EU_30 = "30"
    EU_31 = "31"
    EU_32 = "32"
    EU_33 = "33"
    EU_34 = "34"
    EU_35 = "35"
    EU_35_5 = "35.5"
    EU_36 = "36"
    EU_36_5 = "36.5"
    EU_37 = "37"
    EU_37_5 = "37.5"
    EU_38 = "38"
    EU_38_5 = "38.5"
    EU_39 = "39"
    EU_39_5 = "39.5"
    EU_40 = "40"
    EU_40_5 = "40.5"
    EU_41 = "41"
    EU_41_5 = "41.5"
    EU_42 = "42"
    EU_42_5 = "42.5"
    EU_43 = "43"
    EU_43_5 = "43.5"
    EU_44 = "44"
    EU_44_5 = "44.5"
    EU_45 = "45"
    EU_45_5 = "45.5"
    EU_46 = "46"
    EU_47 = "47"
    EU_48 = "48"


class UkSize(Enum):
    UK_1 = "1"
    UK_1_5 = "1.5"
    UK_2 = "2"
    UK_2_5 = "2.5"
    UK_3 = "3"
    UK_3_5 = "3.5"
    UK_4 = "4"
    UK_4_5 = "4.5"
    UK_5 = "5"
    UK_5_5 = "5.5"
    UK_6 = "6"
    UK_6_5 = "6.5"
    UK_7 = "7"
    UK_7_5 = "7.5"
    UK_8 = "8"
    UK_8_5 = "8.5"
    UK_9 = "9"
    UK_9_5 = "9.5"
    UK_10 = "10"
    UK_10_5 = "10.5"
    UK_11 = "11"
    UK_11_5 = "11.5"
    UK_12 = "12"


class UsSize(Enum):
    US_2 = "2"
    US_2_5 = "2.5"
    US_3 = "3"
    US_3_5 = "3.5"
    US_4 = "4"
    US_4_5 = "4.5"
    US_5 = "5"
    US_5_5 = "5.5"
    US_6 = "6"
    US_6_5 = "6.5"
    US_7 = "7"
    US_7_5 = "7.5"
    US_8 = "8"
    US_8_5 = "8.5"
    US_9 = "9"
    US_9_5 = "9.5"
    US_10 = "10"
    US_10_5 = "10.5"
    US_11 = "11"
    US_11_5 = "11.5"
    US_12 = "12"
    US_13 = "13"
    US_14 = "14"


class ClothesSize(Enum):
    XXXS = "XXXS"
    XXS = "XXS" 
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    XXXL = "XXXL"
    XXXXL = "4XL"
    XXXXXL = "5XL"



class ColorOlx(Enum):
    ...
    
    
class ColorShafa(Enum):
    ...


Color = {
    "color_olx": ColorOlx,
    "color_shafa": ColorShafa,
}


class State(Enum):
    NEW = 'new'
    USED = 'used'


class Material(Enum):
    COTTON = "cotton"
    WOOL = "wool"
    SILK = "silk"
    LINEN = "linen"
    POLYESTER = "polyester"
    NYLON = "nylon"
    ACRYLIC = "acrylic"
    RAYON = "rayon"
    LEATHER = "leather"
    DENIM = "denim"
    FLEECE = "fleece"
    CASHMERE = "cashmere"
    SPANDEX = "spandex"
    HEMP = "hemp"
    SATIN = "satin"
    VELVET = "velvet"
    CHIFFON = "chiffon"
    TWEED = "tweed"
    CORDUROY = "corduroy"
    CANVAS = "canvas"
    SUEDE = "suede"
    FUR = "fur"
    SYNTHETIC = "synthetic"
    BAMBOO = "bamboo"
    MODAL = "modal"
    TENCEL = "tencel"
    MIXED = "mixed"


class Brand(Enum):
    NIKE = "nike"
    ADIDAS = "adidas"
    ZARA = "zara"
    H_AND_M = "h&m"
    UNIQLO = "uniqlo"
    GUCCI = "gucci"
    PRADA = "prada"
    CHANEL = "chanel"
    LOUIS_VUITTON = "louis vuitton"
    BALENCIAGA = "balenciaga"
    VERSACE = "versace"
    ARMANI = "armani"
    CALVIN_KLEIN = "calvin klein"
    TOMMY_HILFIGER = "tommy hilfiger"
    RALPH_LAUREN = "ralph lauren"
    LACOSTE = "lacoste"
    HUGO_BOSS = "hugo boss"
    BURBERRY = "burberry"
    DIESEL = "diesel"
    LEVIS = "levi's"
    GAP = "gap"
    MANGO = "mango"
    BERSHKA = "bershka"
    PULL_AND_BEAR = "pull&bear"
    STRADIVARIUS = "stradivarius"
    MASSIMO_DUTTI = "massimo dutti"
    COS = "cos"
    OTHER = "other"


CLOTHES_BY_SEX = {
    Sex.WOMEN: WomenClothes,
    Sex.MEN: MenClothes,
    Sex.CHILD: ChildClothes,
    Sex.UNISEX: UnisexClothes
}

SHOES_BY_SEX = {
    Sex.WOMEN: WomenShoes,
    Sex.MEN: MenShoes,
    Sex.CHILD: ChildShoes,
    Sex.UNISEX: UnisexShoes
}

SHOE_SIZES = {
    'eu': EuSize,
    'uk': UkSize,
    'us': UsSize,
}

SIZE_MAPPING = {
    'shoes': SHOE_SIZES,
    'clothes': ClothesSize
}

TYPE_MAPPING = {
    'clothes': CLOTHES_BY_SEX,
    'shoes': SHOES_BY_SEX
}

