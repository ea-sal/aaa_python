import json
from keyword import iskeyword


class ColorizeMixin:
    """defines color of text output"""
    def get_color(self):
        repr_color_code = 33
        return repr_color_code


class MakeAttributes:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, '_'+str(k) if iskeyword(k) else k, MakeAttributes(v) if isinstance(v, dict) else v)


class Advert(ColorizeMixin, MakeAttributes):
    """creates class instance from JSON attrs"""
    def __init__(self, dictionary):
        self.price = 0
        self = MakeAttributes(dictionary)
        assert self.price >= 0


    def __repr__(self):
        return f'\033[1;{ColorizeMixin().get_color()};;47m {self.title} | {self.price} ₽'


"""
    @property
    def price_check(self):
        return self.price

    @price_check.setter
    def price_check(self, new_price):
        assert new_price >= 0
        self.price = new_price
"""

lesson_str = """{
    "title": "python",
    "price": 9,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
lesson = json.loads(lesson_str)
lesson_ad = Advert(lesson)
print('\nOUT: ', lesson_ad.__dict__)


doggo_str = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
} """
doggo = json.loads(doggo_str)
#doggo_ad = Advert(doggo)
#print('\nOUT: ', doggo_ad.__dict__)
