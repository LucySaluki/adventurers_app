# Adventurers Travel List
A place to create and store places and countries you have visited and wish to visit with ratings and searchable by continent and those already visited and a yet to visit wish list.
## Some of the Features of the app
* Countries page and Places page where you can add edit and delete either a country or a place.
* Creating, editing and deleting your own place types.
* A country can have many place (you should add your country first).
* Automatic updating on countries as visited if a place is added that is associated with a country and has been visited.
* Star ratings for places.
* Viewing by places visited and want to visit.
* Search by continent for all places on that continent.
## You will needed:
* Postgres on your computer with a database called "adventure".
* Some kind of text editor like visual studio to run the scripts.
* Flask on your computer.
## To set up
* Download the code
* Run createdb adventure (if you havent made an empty database with that name already).
* Run psql -d adventure -f db/adventures.sql from the app location.
* Run Flask using the Flask run command.
* Open Chrome and enter localhost:5000 into the address bar.
* Optional - you can run python3 console.py to start with a basic set up.