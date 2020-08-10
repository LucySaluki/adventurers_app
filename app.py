from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint
from controllers.places_controller import places_blueprint
from controllers.place_types_controller import place_types_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(places_blueprint)
app.register_blueprint(place_types_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
