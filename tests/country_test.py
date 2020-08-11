import unittest

from models.countries import Country
from models.place_types import PlaceType
from models.places import Place

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Borneo","Asia",False)
        self.place_type=PlaceType("Nature Reserve")
        self.place =  Place("Kota Kinabalu", "Highest Peak in Malaysia", self.place_type ,self.country,True, 3)

    # test country name added
    def test_country_has_name(self):
        self.assertEqual("Borneo",self.country.name)
    
    # test country continent added
    def test_country_has_continent(self):
        self.assertEqual("Asia",self.country.continent)

    # test country visited added
    def test_country_has_visited(self):
        self.assertEqual(False,self.country.visited)

    # test place has type
    def test_place_has_type(self):
        self.assertEqual("Nature Reserve",self.place.place_type.type_name)

        