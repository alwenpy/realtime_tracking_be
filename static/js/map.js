// function initMap() {
//     var map = new google.maps.Map(document.getElementById('map'), {
//         zoom: 15,
//         center: {lat: 51.509865, lng: -0.118092}  
//     });

//     var marker = new google.maps.Marker({
//         position: {lat: 51.509865, lng: -0.118092},
//         map: map,
//         title: 'Current Location'
//     });

//     // Simulate Kafka real-time updates
//     function updateMarkerPosition(newLat, newLng) {
//         var newPosition = new google.maps.LatLng(newLat, newLng);
//         marker.setPosition(newPosition);
//         map.setCenter(newPosition);
//     }

//     // Fetch location updates (this could be updated to fetch from Kafka or your server)
//     setInterval(function() {
//         fetch('/api/get_latest_location/')
//         .then(response => response.json())
//         .then(data => {
//             var lat = parseFloat(data.latitude);
//             var lng = parseFloat(data.longitude);
//             updateMarkerPosition(lat, lng);
//         });
//     }, 5000);  // Update every 5 seconds
// }

// window.onload = initMap;
