import pdb

from models.countries import Country
import repositories.country_repository as country_repository

from models.place_types import PlaceType
import repositories.place_type_repository as place_type_repository

from models.places import Place
import repositories.place_repository as place_repository

#clear out data for testing and test delete all works
place_repository.delete_all()
place_type_repository.delete_all()
country_repository.delete_all()

# create country tables and save to database
country_1 = Country("Borneo","Asia")
country_repository.save(country_1)
country_2 = Country("Peru", "South America")
country_repository.save(country_2)
country_3 = Country("Ethiopia","Africa")
country_repository.save(country_3)
country_4 = Country("Botswana", "Africa")
country_repository.save(country_4)

#create place types and save to database
place_type_1 = PlaceType("Archaeological Site")
place_type_repository.save(place_type_1)
place_type_2= PlaceType("Nature Reserve")
place_type_repository.save(place_type_2)
place_type_3= PlaceType("Marin Reserve")
place_type_repository.save(place_type_3)

#create places and save to database
place_1 = Place('Agua Calientes', "Ancient Inca City of Machu Picchu and mountain peak",place_type_1,country_2, True, 5)
place_repository.save(place_1)
place_2 = Place("Sepilok","Rehabilitation centre and sanctuary for orangutans",place_type_2,country_1, True, 3)
place_repository. save(place_2)
place_3 = Place("Kota Kinabalu","Mountain peak and nature reserve.", place_type_2, country_1, True, 2)
place_repository.save(place_3)
place_4 = Place("Puerto Maldanado", "Lake and reserve in the heart of the peruvian Amazon jungle", place_type_2, country_2,True, 0)
place_repository.save(place_4)

# test country is saved to database and test return single country
test_country_4 = country_repository.select(country_4.id)
print(test_country_4.name)

#test place saved to database and test return single place and test it has country associated with it
test_place_3 = place_repository.select(place_4.id)
print(test_place_3.description)
country_test = country_repository.select(test_place_3.country.id)
print(country_test.name)

# test updating country
print(country_3.name)
country_5=Country("Madagascar",country_3.continent,country_3.id) 
country_repository.update(country_5)
test_country_4=country_repository.select(country_3.id)
print(test_country_4.name)

# and turning it back
print(country_3.name)
country_5=Country("Ethiopia",country_3.continent, country_3.id) 
country_repository.update(country_5)
test_country_4=country_repository.select(country_3.id)
print(test_country_4.name)

#test updating place
print(place_2.visited)
place_5=Place(place_2.place_name,place_2.description, place_2.place_type, place_2.country, False, place_2.rating, place_2.id)
place_repository.update(place_5)
test_place_5 = place_repository.select(place_2.id)
print(test_place_5.visited)

#test updating place_type
print(place_type_3.type_name)
place_type_4=PlaceType("Marine Reserve",place_type_3.id)
place_type_repository.update(place_type_4)
test_place_type_5=place_type_repository.select(place_type_3.id)
print(test_place_type_5.type_name)

pdb.set_trace()