$(window).load(function() {
    // Construct the catalog query string
    url = 'https://data.kingcounty.gov/resource/gkhn-e8mn.json?$where=inspection_date%20between%20%272015-01-01T12:00:00%27%20and%20%272016-03-22T14:00:00%27';
    
    // Creating a LatLng object containing the coordinate for the center of the map 
    var center = new google.maps.LatLng(47.608013,-122.335167);

    // Creating an object literal containing the properties we want to pass to the map
    var mapOptions = {
      zoom: 14,
      center: center
    }

    // Calling the constructor to initialize the map
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
    
    // Retrieve JSON data and plot it
    $.getJSON(url, function(data, textstatus) {
        console.log(data);
        $.each(data, function(i, entry) {

      //create a string of contents to add to the InfoWindow
      var contentString = '<div><b>'+ entry.inspection_business_name +'</b></div>'+'<div>'+ entry.address +'</div>'+'<div>'+ 'Inspection Result:  ' + entry.inspection_result +'</div>'+'<div>'+ entry.violation_description +'</div>';

      // Create an InfowWindow
      var infowindow = new google.maps.InfoWindow({
        content: contentString
      });

      //Create a map marker
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(entry.latitude, entry.longitude),
        map: map,
        title: entry.inspection_business_name
      });

      // Adding a click event to the marker
      marker.addListener('click', function() {
        // Opening the InfoWindow
        infowindow.open(map, marker);});
        });
    });
});



