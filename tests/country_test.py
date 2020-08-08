import unittest

from models.countries import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo")

    def test_country_has_name(self):
        self.assertEqual("Borneo",self.country.name)