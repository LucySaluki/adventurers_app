import unittest

from models.countries import Country
from models.place_types import PlaceType
from models.places import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo","Asia", False)
        self.place_type = PlaceType("Nature Reserve")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia", self.place_type,self.country,True,3)

    #  test place has name
    def test_place_has_name(self):
        self.assertEqual("Kota Kinabalu", self.place.place_name)

    # test place has dsecription
    def test_place_has_description(self):
        self.assertEqual(24, len(self.place.description))

    # test place has type
    def test_place_has_type(self):
        self.assertEqual("Nature Reserve", self.place_type.type_name)

    # test place has country
    def test_place_has_country(self):
        self.assertEqual("Borneo", self.place.country.name)

    # test place has visited 
    def test_place_has_visited(self):
        self.assertEqual(True, self.place.visited)

    # test place has rating 
    def test_place_has_rating(self):
        self.assertEqual(3, self.place.rating)