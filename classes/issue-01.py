import json
from keyword import iskeyword


class ColorizeMixin:
    """defines color of text output"""
    @property
    def get_color(self):
        repr_color_code = 33
        return f'\033[1;{repr_color_code};40m'


class MakeAttributes:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, '_'+str(k) if iskeyword(k) else k, MakeAttributes(v) if isinstance(v, dict) else v)


class Advert(ColorizeMixin, MakeAttributes):
    """creates class instance from JSON attrs"""
    def __init__(self, dictionary):
        self.price = 0
        super().__init__(dictionary)

        assert self.price >= 0

    def __repr__(self):
        return f'{ColorizeMixin().__repr__()} {self.title} | {self.price} ₽'


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
#print('\nOUT: ', lesson_ad.__dict__)


doggo_str = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
} """
doggo = json.loads(doggo_str)
doggo_ad = Advert(doggo)
print(doggo_ad)
