from enum import Enum


class Sex(Enum):
    men = 'men'
    women = 'women'
    child = 'child'
    unisex = 'unisex'
    

class Clothes(Enum):
    T_SHIRT = "t_shirt"        # футболка
    SHIRT = "shirt"            # сорочка
    BLOUSE = "blouse"          # блуза
    SWEATER = "sweater"        # светр
    HOODIE = "hoodie"          # худі
    JACKET = "jacket"          # куртка
    COAT = "coat"              # пальто
    DRESS = "dress"            # сукня
    SKIRT = "skirt"            # спідниця
    PANTS = "pants"            # штани
    JEANS = "jeans"            # джинси
    SHORTS = "shorts"          # шорти
    LEGGINGS = "leggings"      # легінси
    SUIT = "suit"              # костюм
    SWIMWEAR = "swimwear"      # купальник
    UNDERWEAR = "underwear"    # білизна
    PAJAMAS = "pajamas"        # піжама
    SPORTSWEAR = "sportswear"  # спортивний одяг
    OVERALLS = "overalls"      # комбінезон


class Shoes(Enum):
    SNEAKERS = "sneakers"      # кросівки
    BOOTS = "boots"            # чоботи
    ANKLE_BOOTS = "ankle_boots" # черевики
    SANDALS = "sandals"        # сандалі
    SLIPPERS = "slippers"      # капці
    LOAFERS = "loafers"        # лофери
    HEELS = "heels"            # підбори
    FLATS = "flats"            # балетки
    OXFORDS = "oxfords"        # оксфорди
    MOCASSINS = "mocassins"    # мокасини
    ESPADRILLES = "espadrilles"# еспадрильї
    CLOGS = "clogs"            # сабо
    FLIP_FLOPS = "flip_flops"  # в'єтнамки


    
class Type(Enum):
    clothes: Clothes
    shoes: Shoes
    
    

class Eu_size(Enum):
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

class Uk_size(Enum):
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

class Us_size(Enum):
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



    
class ShoesSize(Enum):
    eu_size: Eu_size
    uk_size: Uk_size
    us_size: Us_size




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
    _4XL = "4XL"
    _5XL = "5XL"


    
class Size(Enum):
    shoes: ShoesSize
    clothes: ClothesSize
    
    


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    WHITE = "white"
    BLACK = "black"
    YELLOW = "yellow"
    CYAN = "cyan"
    MAGENTA = "magenta"
    ORANGE = "orange"
    PURPLE = "purple"
    PINK = "pink"
    BROWN = "brown"
    GRAY = "gray"
    LIGHT_GRAY = "lightgray"
    DARK_GRAY = "darkgray"
    GOLD = "gold"
    SILVER = "silver"
    LIME = "lime"
    INDIGO = "indigo"
    VIOLET = "violet"

    
    
class State(Enum):
    new = 'new'
    used = 'used'
    
    
class Material(Enum):
    COTTON = "cotton"          # бавовна
    WOOL = "wool"              # вовна
    SILK = "silk"              # шовк
    LINEN = "linen"            # льон
    POLYESTER = "polyester"    # поліестер
    NYLON = "nylon"            # нейлон
    ACRYLIC = "acrylic"        # акрил
    RAYON = "rayon"            # віскоза
    LEATHER = "leather"        # шкіра
    DENIM = "denim"            # джинс
    FLEECE = "fleece"          # фліс
    CASHMERE = "cashmere"      # кашемір
    SPANDEX = "spandex"        # спандекс (еластан)
    HEMP = "hemp"              # конопляна тканина
    SATIN = "satin"            # атлас
