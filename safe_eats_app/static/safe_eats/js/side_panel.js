

function slidePanel(bus_id){
	$.ajax({
        url: "/restaurants/" + bus_id, 
        success: function(data){
            $("#slide-panel").html(data); 
        }
    });

    var panel = $('#slide-panel');
	if (panel.hasClass("visible")) {
		panel.removeClass('visible').animate({'margin-right':'-300px'});
	} else {
		panel.addClass('visible').animate({'margin-right':'0px'});
	}
}