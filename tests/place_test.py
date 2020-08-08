import unittest

from models.countries import Country
from models.places import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia and Nature Reserve", "Natural",self.country,True)

    def test_place_has_name(self):
        self.assertEqual("Kota Kinabalu", self.place.place_name)
