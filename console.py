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
place_2 = Place("Sepilok","Rehabilitation centre and sactuary for Orangutans","Nature Reserve",country_1, True)
place_repository.save(place_2)
place_3=Place('Machu Picchu', "Ancient Inca City and mountain","Archaeological Site",country_2, True )
place_repository.save(place_3)
place_4 = Place("Puerto Maldanado", "Lake and reserve in the hear of the peruvian Amazon", "Nature Reserve", country_2,True)
place_repository.save(place_4)

pdb.set_trace()