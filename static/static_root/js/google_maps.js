$(function() {
    // Exit if not car page
    if(!$('#car-bg').length) {
        return;
    }

    // Declare variables and instantiate geocoder
    var geocoder, location, map;
    geocoder = new google.maps.Geocoder();

    // Predefine options and position of the map
    var latlng = new google.maps.LatLng(-26.734968, 134.489563);
    var options = {
        zoom: 3,
        center:latlng, 
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    $.each($('#map-container'), function() {
        // Gather all locations and set map
        locations = document.getElementsByClassName("car-store");
        map = new google.maps.Map($(this).find('.map')[0], options);

        // Place markers on the map
        for (let location in locations){            
            geocoder.geocode( {'address': locations[location].innerText}, function(results, status) {
                if(status === google.maps.GeocoderStatus.OK) {                
                    var marker = new google.maps.Marker({
                        map: map,
                        position: results[0].geometry.location                        
                    });
                } 
            });
        }
    });
});