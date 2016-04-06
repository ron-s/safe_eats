

function slidePanel(bus_id) {
    if (bus_id === slidePanelId){
        slide();
    } else {

        $.ajax({
            url: "/restaurants/" + bus_id,
            success: function(data){
                var panel = $('#slide-panel');
                panel.html(data);

                slidePanelId = bus_id;
                if (panel.hasClass("visible")) {

                } else {
                    slide();
                }
                
            }
        });
    }
    
}

function slide(){
    var panel = $('#slide-panel');

    if (panel.hasClass("visible")) {
        panel.removeClass('visible').animate({'margin-right':'-300px'}, function() {panel.addClass("hidden");});
    } else {
        panel.removeClass("hidden").animate({'margin-right':'0px'}, function() {panel.addClass('visible');});
    }
}