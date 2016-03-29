$(window).load(function() {
    // Construct the catalog query string
    url = 'https://data.kingcounty.gov/resource/gkhn-e8mn.json?$where=inspection_date%20between%20%272015-01-01T12:00:00%27%20and%20%272016-03-22T14:00:00%27';
    
    // Intialize our map
    var center = new google.maps.LatLng(47.608013,-122.335167);
    var mapOptions = {
      zoom: 14,
      center: center
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
    
    // Retrieve our data and plot it
    $.getJSON(url, function(data, textstatus) {
          console.log(data);
          $.each(data, function(i, entry) {

      var contentString = '<div><b>'+ entry.inspection_business_name +'</b></div>'+'<div>'+ entry.address +'</div>'+'<div>'+ 'Inspection Result:  ' + entry.inspection_result +'</div>'+'<div>'+ entry.violation_description +'</div>';
      
      var infowindow = new google.maps.InfoWindow({
        content: contentString
        });
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(entry.latitude, entry.longitude),
        map: map,
        title: entry.inspection_business_name
              });
              marker.addListener('click', function() {infowindow.open(map, marker);});
          });
    });
});