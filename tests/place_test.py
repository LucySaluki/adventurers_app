import unittest

from models.countries import Country
from models.place_type import PlaceType
from models.places import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo","Asia")
        self.place_type = PlaceType("Nature Reserve")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia", self.place_type,self.country,True)

    def test_place_has_name(self):
        self.assertEqual("Kota Kinabalu", self.place.place_name)

    def test_place_has_description(self):
        self.assertEqual(24, len(self.place.description))

    def test_place_has_type(self):
        self.assertEqual("Nature Reserve", self.place_type.type_name)

    def test_place_has_country(self):
        self.assertEqual("Borneo", self.place.country.name)

    def test_place_has_visited(self):
        self.assertEqual(True, self.place.visited)