from flask import Flask, render_template, request
import requests
API_KEY = "af1574aa70b6c3e4712afac108f5fa44"

app = Flask(__name__)

def get_weather(city):
    if city.lower() == "paris":
        return {
            "name": "Paris",
            "weather": [{"description": "ciel dégagé", "icon": "01d"}],
            "main": {"temp": 20, "humidity": 50},
            "wind": {"speed": 3.5},
        }
    else:
        return {
            "name": city.capitalize(),
            "weather": [{"description": "nuageux", "icon": "03d"}],
            "main": {"temp": 15, "humidity": 70},
            "wind": {"speed": 2.1},
        }

def get_background_and_audio(weather):
    description = weather["weather"][0]["description"]
    if "pluie" in description:
        return "rainy-background", "rainy.gif", "rainy.mp3"
    elif "neige" in description:
        return "snowy-background", "snowy.gif", "snowy.mp3"
    elif "nuage" in description:
        return "cloudy-background", "cloudy.gif", "cloudy.mp3"
    else:
        return "sunny-background", "sunny.gif", "sunny.mp3"

@app.route("/", methods=["GET", "POST"])
def home():
    is_first_interface = True  # Première interface avec un fond d'écran par défaut
    is_second_interface = False  # Initialisation de la deuxième interface

    background_class = "sunny-background"  # Valeur par défaut pour l'arrière-plan
    weather_gif = "sunny.gif"  # Valeur par défaut pour le GIF
    weather_audio = "sunny.mp3"  # Valeur par défaut pour l'audio

    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)
        background_class, weather_gif, weather_audio = get_background_and_audio(weather)

        # Définir is_second_interface à True dans certaines conditions (par exemple, après une certaine interaction)
        if city.lower() == "paris":
            is_second_interface = True  # Exemple de condition pour définir la deuxième interface

        return render_template(
            "index.html",
            weather=weather,
            background_class=background_class,
            weather_gif=weather_gif,
            weather_audio=weather_audio,
            is_first_interface=False,
            is_second_interface=is_second_interface,  # Passer la variable ici
        )

    return render_template(
        "index.html",
        is_first_interface=is_first_interface,
        background_class=background_class,
        weather_gif=weather_gif,
        weather_audio=weather_audio,
        is_second_interface=is_second_interface,  # Passer la variable ici
    )


    # Première interface : affiche un fond et un GIF par défaut
    return render_template(
        "index.html",
        is_first_interface=is_first_interface,
        background_class=background_class,
        weather_gif=weather_gif,
        weather_audio=weather_audio,
    )

@app.route("/forecast", methods=["POST"])
def forecast():
    city = request.form.get("city")
    forecast_data = []
    background_class = "ocean-background"  # Fond par défaut "océan"
    if city:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=fr"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for forecast in data['list']:
                forecast_data.append({
                    "datetime": forecast['dt_txt'],
                    "temperature": forecast['main']['temp'],
                    "weather": forecast['weather'][0]['main'].lower()
                })
            # Choisir le fond en fonction des conditions
            weather_condition = forecast_data[0]['weather']
            if weather_condition == "clear":
                background_class = "ocean-background"
            elif weather_condition == "clouds":
                background_class = "cloudy-ocean-background"
            elif weather_condition == "rain":
                background_class = "rainy-ocean-background"
            elif weather_condition == "snow":
                background_class = "snowy-ocean-background"
        else:
            return render_template("forecast.html", error="Ville introuvable.")
    return render_template("forecast.html", forecasts=forecast_data, background_class=background_class)
@app.route('/some_route', methods=['GET', 'POST'])
def some_route():
    is_second_interface = True  # Ou une condition qui détermine si c'est la 2e interface
    return render_template('index.html', is_second_interface=is_second_interface)

if __name__ == "__main__":
    app.run(debug=True)