import unittest

from models.countries import Country
from models.place_type import PlaceType
from models.places import Place

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo","Asia")
        self.place_type=PlaceType("Nature Reserve")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia", self.place_type ,self.country,True)

    def test_country_has_name(self):
        self.assertEqual("Borneo",self.country.name)
    
    def test_country_has_continent(self):
        self.assertEqual("Asia",self.country.continent)

    def test_place_has_type(self):
        self.assertEqual("Nature Reserve",self.place.place_type.type_name)

        