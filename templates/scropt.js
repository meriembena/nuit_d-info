function updateWeatherInfo(condition) {
    const descriptionElement = document.getElementById("weather-description");
    const adviceElement = document.getElementById("weather-advice");
    const quoteElement = document.getElementById("weather-quote");
    const animalElement = document.getElementById("weather-animal");

    if (condition === "Clear") {
        descriptionElement.innerHTML = "Ensoleillé 🌞";
        adviceElement.innerHTML = "Il fait chaud aujourd'hui, n'oubliez pas de boire beaucoup d'eau et de vous protéger du soleil !";
        quoteElement.innerHTML = "Le soleil brille toujours après la pluie.";
        animalElement.src = "assets/sunny_cat.gif"; // Exemple de GIF pour la météo ensoleillée
    } else if (condition === "Rain") {
        descriptionElement.innerHTML = "Pluvieux 🌧️";
        adviceElement.innerHTML = "Il pleut, pensez à prendre un parapluie et à ne pas vous mouiller !";
        quoteElement.innerHTML = "Il pleut des idées créatives aujourd’hui.";
        animalElement.src = "assets/rainy_dog.gif"; // Exemple de GIF pour la pluie
    } else if (condition === "Snow") {
        descriptionElement.innerHTML = "Neige ❄️";
        adviceElement.innerHTML = "Il neige ! Il est temps de se blottir près du feu et de boire un chocolat chaud.";
        quoteElement.innerHTML = "Chaque flocon est une nouvelle chance.";
        animalElement.src = "assets/snowy_bear.gif"; // Exemple de GIF pour la neige
    }

    // Ajout de la musique en fonction de la météo
    const audio = document.createElement("audio");
    audio.autoplay = true;
    audio.loop = true;
    if (condition === "Clear") {
        audio.src = "assets/sunny-music.mp3"; // Musique pour le temps ensoleillé
    } else if (condition === "Rain") {
        audio.src = "assets/rainy-music.mp3"; // Musique pour la pluie
    } else if (condition === "Snow") {
        audio.src = "assets/snowy-music.mp3"; // Musique pour la neige
    }
    document.body.appendChild(audio);
}

// Carte interactive avec Leaflet
var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([51.505, -0.09]).addTo(map)
    .bindPopup('Londres')
    .openPopup();

L.marker([48.8566, 2.3522]).addTo(map)
    .bindPopup('Paris')
    .openPopup();

// Exemple de changement de météo
updateWeatherInfo("Rain");
