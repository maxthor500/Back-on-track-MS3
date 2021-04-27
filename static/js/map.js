//set my map view
const map = L.map('map').setView([52.087852, -7.619566], 12);

//render the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

//popup lat and lng with a click on the map
const popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);


//render markers with my icon
L.marker([52.087852, -7.619566]).addTo(map).bindPopup('BOT');
