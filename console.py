import pdb

from models.countries import Country
import repositories.country_repository as country_repository

from models.places import Place
import repositories.place_repository as place_repository

place_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Borneo")
country_repository.save(country_1)
country_2 = Country("Peru")
country_repository.save(country_2)
country_3 = Country("Ethiopia")
country_repository.save(country_3)
country_4 = Country("Botswana")
country_repository.save(country_4)

place_1 = Place("Kota Kinabalu","Moutain peak and nature reserve", "Nature Reserve", country_1, True)
place_repository.save(place_1)
place_2 = Place("Sepilok","Rehabilitation centre and sanctuary for Orangutans","Nature Reserve",country_1, True)
place_repository.save(place_2)
place_3=Place('Machu Picchu', "Ancient Inca City and mountain","Archaeological Site",country_2, True )
place_repository.save(place_3)
place_4 = Place("Puerto Maldanado", "Lake and reserve in the heart of the peruvian Amazon jungle", "Nature Reserve", country_2,True)
place_repository.save(place_4)

test_country_4 = country_repository.select(country_4.id)
print(test_country_4.name)

test_place_3 = place_repository.select(place_4.id)
print(test_place_3.description)

print(country_3.name)
country_5=Country("Madagascar",country_3.id) 
country_repository.update(country_5)
test_country_4=country_repository.select(country_3.id)
print(test_country_4.name)

print(place_2.visited)
place_5=Place(place_2.place_name,place_2.description, place_2.place_type, place_2.country, False, place_2.id)
place_repository.update(place_5)
test_place_5 = place_repository.select(place_2.id)
print(test_place_5.visited)


pdb.set_trace()