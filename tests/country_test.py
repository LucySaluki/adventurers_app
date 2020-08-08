import unittest

from models.countries import Country
from models.places import Place
from repositories.country_repository import save

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia", "Natural",self.country,True)

    def test_country_has_name(self):
        self.assertEqual("Borneo",self.country.name)

        