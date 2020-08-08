import unittest

from models.countries import Country
from models.places import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia", "Natural",self.country,True)

    def test_place_has_name(self):
        self.assertEqual("Kota Kinabalu", self.place.place_name)

    def test_place_has_description(self):
        self.assertEqual(24, len(self.place.description))

    def test_place_has_type(self):
        self.assertEqual("Natural", self.place.place_type)

    def test_place_has_country(self):
        self.assertEqual("Borneo", self.place.country.name)

    def test_place_has_visited(self):
        self.assertEqual(True, self.place.visited)