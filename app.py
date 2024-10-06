from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",load_cities=load_cities)

@app.route('/load_cities/')
def load_cities(filename):
    cities = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                city = parts[0].strip()
                longitude = parts[1].strip()
                latitude = parts[2].strip()
                cities[city.lower()] = (longitude, latitude)
    return cities



app.run()